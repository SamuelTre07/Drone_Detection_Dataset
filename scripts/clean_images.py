import os
from PIL import Image

def image_standardization(folder_path, standard_name):
    # Get all files in folder
    files = sorted(os.listdir(folder_path))

    counter = 1

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Open the image
        try:
            img = Image.open(file_path)
            # Convert to RGB (needed for png/webp with alpha)
            img = img.convert("RGB")
        except Exception as e:
            print(f"Skipping {file_name}: {e}")
            continue

        # Create new name with zero-padded numbering
        new_name = f"{standard_name}_{counter:03d}.jpg"
        new_path = os.path.join(folder_path, new_name)

        # Save as JPG
        img.save(new_path, "JPEG", quality=95)
        
        # Remove the old file if different from new
        if file_path != new_path:
            os.remove(file_path)
        
        counter += 1

    print(f"Done! {counter-1} images processed and standardized.")

image_standardization(
    folder_path="clean_images/positive",
    standard_name="drone"
)

image_standardization(
    folder_path="clean_images/negative",
    standard_name="no_drone"
)