import numpy as np
from PIL import Image, ImageFilter
import os

def extract_parts(image_path, output_dir):
    # Create output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Loading {image_path}...")
    try:
        img = Image.open(image_path).convert("RGBA")
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    # Convert to numpy array
    arr = np.array(img)
    
    # Calculate brightness to separate foreground (parts) from background
    # Assuming background is darker than the metallic parts
    gray = np.mean(arr[:,:,:3], axis=2)
    threshold = 60 # Adjust based on image contrast
    mask = gray > threshold

    # rudimentary connected components using simple scanning
    # We will find bounding boxes of "islands"
    
    # Fast way: Find rows and cols with pixels
    # This assumes parts are somewhat separated.
    # To do this properly without scipy/cv2 is hard, so we'll do a simple "grid chop"
    # or identify distinct regions by projecting the mask.
    
    # Better approach given constraints:
    # 1. Blur the mask to connect nearby pixels of the same object
    # 2. Find bounding boxes of white regions manually
    
    rows, cols = mask.shape
    visited = np.zeros((rows, cols), dtype=bool)
    
    part_count = 0
    min_part_area = 500 # Ignore small noise
    
    # We will assume parts are distinct. 
    # To avoid recursion depth issues with flood fill, we use a stack-based fill or just scan.
    # Given the complexity, let's try a simplified approach:
    # We will walk through the image, find a start pixel, and expand a box around it.
    
    # Optimization: Downscale for detection
    scale = 4
    small_mask = mask[::scale, ::scale]
    s_rows, s_cols = small_mask.shape
    s_visited = np.zeros_like(small_mask, dtype=bool)
    
    boundingBoxes = []
    
    for r in range(s_rows):
        for c in range(s_cols):
            if small_mask[r, c] and not s_visited[r, c]:
                # Found a new part, flood fill to find extents
                stack = [(r, c)]
                s_visited[r, c] = True
                min_r, max_r = r, r
                min_c, max_c = c, c
                
                pixel_count = 0
                
                while stack:
                    curr_r, curr_c = stack.pop()
                    pixel_count += 1
                    
                    # Update bounding box
                    min_r = min(min_r, curr_r)
                    max_r = max(max_r, curr_r)
                    min_c = min(min_c, curr_c)
                    max_c = max(max_c, curr_c)
                    
                    # Check neighbors
                    neighbors = [
                        (curr_r-1, curr_c), (curr_r+1, curr_c),
                        (curr_r, curr_c-1), (curr_r, curr_c+1)
                    ]
                    
                    for nr, nc in neighbors:
                        if 0 <= nr < s_rows and 0 <= nc < s_cols:
                            if small_mask[nr, nc] and not s_visited[nr, nc]:
                                s_visited[nr, nc] = True
                                stack.append((nr, nc))
                
                # If distinct enough
                if pixel_count > (min_part_area / (scale*scale)):
                    # Scale back up
                    boundingBoxes.append((
                        min_r * scale, 
                        min_c * scale, 
                        (max_r + 1) * scale, 
                        (max_c + 1) * scale
                    ))

    print(f"Found {len(boundingBoxes)} potential parts.")
    
    for i, bbox in enumerate(boundingBoxes):
        r1, c1, r2, c2 = bbox
        # Add padding
        pad = 10
        r1 = max(0, r1 - pad)
        c1 = max(0, c1 - pad)
        r2 = min(rows, r2 + pad)
        c2 = min(cols, c2 + pad)
        
        # Crop
        crop = img.crop((c1, r1, c2, r2))
        
        # Make transparent?
        # A simple transparency mask: brightness -> alpha
        # We can just make the dark background transparent in the crop
        crop_arr = np.array(crop)
        c_gray = np.mean(crop_arr[:,:,:3], axis=2)
        # Create alpha channel: if dark, alpha = 0, else 255
        # Soft transition
        alpha = np.clip((c_gray - 30) * 5, 0, 255).astype(np.uint8)
        
        crop_arr[:,:,3] = alpha
        final_part = Image.fromarray(crop_arr)
        
        output_path = os.path.join(output_dir, f"part_{i}.png")
        final_part.save(output_path)
        print(f"Saved {output_path}")

    print("Extraction complete.")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Extract distinct parts from an image.")
    parser.add_argument("image_path", nargs="?", help="Path to the source image")
    parser.add_argument("--output", default="output_parts", help="Output directory")
    
    args = parser.parse_args()
    
    if args.image_path:
        if os.path.exists(args.image_path):
            extract_parts(args.image_path, args.output)
        else:
            print(f"Error: Image not found at {args.image_path}")
    else:
        print("Usage: python extract_parts.py <image_path> [--output <output_dir>]")
        print("Please provide an image path to run the extraction.")
