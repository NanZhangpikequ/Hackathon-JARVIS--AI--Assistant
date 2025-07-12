import os
import shutil
from sklearn.model_selection import train_test_split
from pathlib import Path

# ====== Set your absolute paths below ======
original_dataset_dir = Path("C:/Users/Nanzh/PycharmProjects/pythonProject6/cnnapp/raw-img")
output_base_dir = Path("C:/Users/Nanzh/PycharmProjects/pythonProject6/cnnapp/animals10-split-70-15-15")

# Create train/val/test directory structure
splits = ['train', 'val', 'test']
for split in splits:
    for category in os.listdir(original_dataset_dir):
        split_path = output_base_dir / split / category
        split_path.mkdir(parents=True, exist_ok=True)

# Set split ratios
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

random_state = 42  # To ensure reproducibility

# ====== Process each category folder ======
for category in os.listdir(original_dataset_dir):
    category_path = original_dataset_dir / category
    if not category_path.is_dir():
        continue

    images = list(category_path.glob("*"))  # Match all files in the folder
    if not images:
        continue

    # First split: train vs (val + test)
    train_imgs, temp_imgs = train_test_split(
        images, test_size=(1 - train_ratio), random_state=random_state
    )

    # Second split: val vs test (split the remaining 30% equally)
    val_imgs, test_imgs = train_test_split(
        temp_imgs, test_size=0.5, random_state=random_state
    )

    # Copy function to move images to split directories
    def copy_images(img_list, split_name):
        for img_path in img_list:
            dest = output_base_dir / split_name / category / img_path.name
            shutil.copy(img_path, dest)

    copy_images(train_imgs, 'train')
    copy_images(val_imgs, 'val')
    copy_images(test_imgs, 'test')

print("✅ Dataset split complete!")
