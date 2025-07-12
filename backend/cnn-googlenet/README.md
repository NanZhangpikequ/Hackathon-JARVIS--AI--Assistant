# CNN-GoogLeNet Module

## Overview
This folder contains the backend implementation for animal image recognition based on a customized GoogLeNet (Inception v1) architecture. It includes scripts for dataset organization, model training, and saving trained models.

## Files
- `split_dataset.py` or `animals10split.py` : Script to split the original dataset into training, validation, and testing sets.
- `googlenettrain.py` : Main script to train the GoogLeNet model on the Animal-10 dataset and save the trained model.
- `model_save/` : Directory to store the trained model files (e.g., `.h5` format).

## Features
- Customized GoogLeNet architecture for image classification
- Data preprocessing and augmentation
- Training history logging
- Model saving for future inference

## Usage
1. Split your dataset by running:
   ```bash
   python split_dataset.py
Train the GoogLeNet model by running:

bash
Copy
Edit
python googlenettrain.py
The trained model will be saved under the model_save/ directory.
