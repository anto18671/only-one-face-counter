# face-counter

=========================

Overview
--------
This script processes images in batches to detect faces using a CNN face detection model from dlib. If an image contains more than one face, it is moved to a different directory. The script can process images with the extensions .png, .jpg, and .jpeg located within subdirectories of a specified root directory.

Requirements
------------
- Python
- dlib
- cv2 (OpenCV)
- os
- shutil

Setup
-----
1. Install the required packages:
    pip install dlib opencv-python

2. Set the following paths in the code:
    - root_dir: Path to the root directory containing subdirectories of images.
    - dst_dir: Destination directory where the images with more than one face will be moved.
    - model_route: Path to the trained model file for dlib's CNN face detector.

Functionality
-------------
- Uses dlib's CNN face detector for face detection.
- Processes images in batches (default batch size is 8) for efficiency.
- Can handle multiple image formats, including .png, .jpg, and .jpeg.
- For each image:
  - If more than one face is detected, the image is moved to the destination directory.
  - If only one face or no faces are detected, it remains in the source directory, and the processed counter is incremented.
- After processing all images in a subdirectory, the script prints the number of images processed.

Output
------
- Files with more than one detected face are moved to dst_dir.
- Status messages are printed to the console, including:
  - Notification for each file moved to the destination directory.
  - The count of processed files for each subdirectory.
  - The total number of files processed in each subdirectory.

Notes
-----
- Ensure the destination directory (dst_dir) exists, or else there might be an error when moving files.
- The code is structured to easily support more image formats. To add support for another format, simply add its extension to the valid_extensions list. However, make sure that OpenCV (cv2) can handle the format natively.