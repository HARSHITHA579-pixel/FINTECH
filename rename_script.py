import os
import shutil

mapping = {
    "media__1772385210446.png": "logo.png",
    "media__1772385210503.png": "inspection_height_gauge.png",
    "media__1772385210529.png": "profile_projector.png",
    "media__1772385210576.png": "vmc_cosmos.png",
    "media__1772385210621.png": "cnc_lathe_lmw.png",
}

image_dir = "d:/software/anti/images"

for old_name, new_name in mapping.items():
    old_path = os.path.join(image_dir, old_name)
    new_path = os.path.join(image_dir, new_name)
    if os.path.exists(old_path):
        print(f"Renaming {old_name} to {new_name}")
        # Use shutil.move to rename/move the file safely
        shutil.move(old_path, new_path)
    else:
        print(f"Skipping {old_name}, not found.")
