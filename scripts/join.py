import os
import shutil

TRAIN_DIR = "train"
VAL_DIR = "val"

os.makedirs(TRAIN_DIR, exist_ok=True)
os.makedirs(VAL_DIR, exist_ok=True)

def MoveImages(source_path, destination_path):
    images = [f for f in os.listdir(source_path) if f.lower().endswith(".jpg")]
    print(f"Moving {len(images)} images from {source_path} to {destination_path}")

    for image in images:
        shutil.move(
            os.path.join(source_path, image),
            os.path.join(destination_path, image)
        )

MoveImages("clean_images/positive/train", TRAIN_DIR)
MoveImages("clean_images/negative/train", TRAIN_DIR)
MoveImages("clean_images/positive/val", VAL_DIR)
MoveImages("clean_images/negative/val", VAL_DIR)

print(f"Done! Total images in train: {len(os.listdir(TRAIN_DIR))}, val: {len(os.listdir(VAL_DIR))}")