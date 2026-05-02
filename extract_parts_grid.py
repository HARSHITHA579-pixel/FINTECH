import numpy as np
from PIL import Image, ImageOps
import os

def extract_parts_grid(image_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Loading {image_path}...")
    try:
        img = Image.open(image_path).convert("RGBA")
    except Exception as e:
        print(f"Error: {e}")
        return

    width, height = img.size
    # Grid size
    rows = 4
    cols = 4
    
    w_step = width // cols
    h_step = height // rows
    
    count = 0
    
    for r in range(rows):
        for c in range(cols):
            # Crop
            left = c * w_step
            top = r * h_step
            right = left + w_step
            bottom = top + h_step
            
            crop = img.crop((left, top, right, bottom))
            
            # Check if empty (mostly black/dark)
            # Resize for quick check
            small = crop.resize((50, 50))
            arr = np.array(small)
            # Mean brightness
            mean_brightness = np.mean(arr[:,:,:3])
            
            # If brightness is too low, skip (background)
            if mean_brightness < 40: 
                print(f"Skipping part {r},{c} (too dark)")
                continue
                
            # Apply a soft radial mask to edges to hide the square cut
            # Create radial gradient
            mk = Image.new('L', crop.size, 0)
            # Draw circle
            import math
            # We can manipulate pixel data for mask
            # Center
            cx, cy = w_step / 2, h_step / 2
            max_dist = min(cx, cy)
            
            # Actually, simpler: just feather edges
            # Or assume the part is centered in the grid cell (unlikely).
            # Let's just save it as is but maybe make black transparent.
            
            # Transparency logic:
            data = np.array(crop)
            # Calculate brightness
            brightness = np.mean(data[:,:,:3], axis=2)
            # Alpha: linear ramp from brightness. Dark = transparent.
            # < 30 => 0 opacity
            # > 80 => 255 opacity
            alpha = np.clip((brightness - 30) * 5, 0, 255).astype(np.uint8)
            data[:,:,3] = alpha
            
            final_part = Image.fromarray(data)
            
            output_path = os.path.join(output_dir, f"part_{count}.png")
            final_part.save(output_path)
            print(f"Saved {output_path}")
            count += 1

    print(f"Extracted {count} parts.")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Extract parts from an image grid.")
    parser.add_argument("image_path", nargs="?", help="Path to the source image")
    parser.add_argument("--output", default="output_parts", help="Output directory")
    
    args = parser.parse_args()
    
    if args.image_path:
        if os.path.exists(args.image_path):
            extract_parts_grid(args.image_path, args.output)
        else:
            print(f"Error: Image not found at {args.image_path}")
    else:
        print("Usage: python extract_parts_grid.py <image_path> [--output <output_dir>]")
        print("Please provide an image path to run the extraction.")
