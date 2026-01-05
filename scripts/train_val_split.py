import os
import random
import shutil

random.seed(42)

def Splitter(source):
    SOURCE_DIR = f"clean_images/{source}"
    TRAIN_DIR  = f"{SOURCE_DIR}/train"
    VAL_DIR    = f"{SOURCE_DIR}/val"

    os.makedirs(TRAIN_DIR, exist_ok=True)
    os.makedirs(VAL_DIR, exist_ok=True)

    images = [f for f in os.listdir(SOURCE_DIR) if f.lower().endswith(".jpg")]
    random.shuffle(images)

    split_idx = int(0.8 * len(images))
    train_images = images[:split_idx]
    val_images   = images[split_idx:]

    for img in train_images:
        shutil.move(
            os.path.join(SOURCE_DIR, img),
            os.path.join(TRAIN_DIR, img)
        )

    for img in val_images:
        shutil.move(
            os.path.join(SOURCE_DIR, img),
            os.path.join(VAL_DIR, img)
        )

    print(f"Train: {len(train_images)} images")
    print(f"Val: {len(val_images)} images")

# split drone images
Splitter(source="positive")

# split non-drone images
Splitter(source="negative")