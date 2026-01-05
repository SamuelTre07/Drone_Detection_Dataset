# Drone Detection Dataset

This is a curated dataset for drone detection tasks, ready for object detection models (e.g., YOLO). This repository contains cleaned, annotated images of drones and non-drone scenes, along with scripts used for preprocessing and splitting.

## Dataset Structure
```
Drone_Detection_Dataset/
├── train/           # Training set
│   ├── *.jpg        # Drone and non-drone images
│   ├── *.txt        # Corresponding YOLO-format annotations
│   └── classes.txt  # Class list (currently only 'drone')
├── val/             # Validation set
│   ├── *.jpg        # Images
│   ├── *.txt        # Annotations
│   └── classes.txt  # Class list
├── scripts/         # Preprocessing and dataset preparation scripts
│   ├── clean_images.py
│   ├── download.py
│   ├── download_images.py
│   ├── join.py
│   └── train_val_split.py
└── .gitignore
```

## Dataset Details

- **Training set:** **`183 drone`** images (with YOLO annotations) + **`65 non-drone`** images  
- **Validation set:** **`46 drone`** images (with YOLO annotations) + **`13 non-drone`** images  
- All images have been manually reviewed, filtered for duplicates, watermarks, and irrelevant images.  
- Annotations are in YOLO format (`<class_id> <x_center> <y_center> <width> <height>` normalized to image size).  

> Note: Non-drone images do not have `.txt` annotation files, as they contain no objects.

## Usage

1. Clone the repository:  
   ```bash
   git clone https://github.com/SamuelTre07/Drone_Detection_Dataset.git
   cd Drone_Detection_Dataset
   ```

2. The dataset can be used directly with YOLO or other object detection pipelines. For YOLO, ensure your data.yaml points to the train and val folders and includes the correct class names.

3. The scripts/ folder contains code used to clean, filter, and split the original dataset. Running these scripts may produce slightly different splits or file orders.

## Notes

- This repo contains only the processed images and annotations. Original raw images are **not included**.
- All steps of preprocessing, filtering, and annotation will be documented in a future blog post.

## License & Usage

- The images in this dataset were collected from publicly available sources on the internet.
- This dataset is provided for research and educational purposes only (e.g., training object detection models for academic projects or experiments).
- Redistribution, commercial use, or claiming ownership of the original images is not permitted.
- Users should ensure compliance with copyright laws of the original image sources.