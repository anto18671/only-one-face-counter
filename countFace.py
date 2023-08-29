import os
import cv2
import dlib
import shutil

# Set the batch size for GPU processing
batch_size = 8

# Define the root directory and destination directory
root_dir = r""
dst_dir = r""
model_route = r""

# Load the detector
dnnFaceDetector = dlib.cnn_face_detection_model_v1(model_route)

# Get list of all directories in the root directory
dir_list = [dir for dir in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, dir))]

# Process all directories
for directory in dir_list:
    src_dir = os.path.join(root_dir, directory)

    # Get list of all .png files in the source directory
    file_list = [file for file in os.listdir(src_dir) if file.endswith(".png")]

    # Process all images
    counter = 0
    for i in range(0, len(file_list), batch_size):
        batch_files = file_list[i:i + batch_size]

        batch_images = []
        for filename in batch_files:
            img_path = os.path.join(src_dir, filename)
            img = cv2.imread(img_path)
            batch_images.append(img)

        # Convert batch images to RGB for dlib
        batch_rgb_images = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB) for img in batch_images]

        # Perform batch face detection
        batch_faces = dnnFaceDetector(batch_rgb_images, batch_size=batch_size)

        for j, faces in enumerate(batch_faces):
            # If the number of detected faces is not exactly one, move the file
            if len(faces) > 1:
                img_path = os.path.join(src_dir, batch_files[j])
                shutil.move(img_path, os.path.join(dst_dir, batch_files[j]))
                print(f"Moved file {batch_files[j]} to {dst_dir}")
            else:
                counter += 1
                print(f"Processed file count: {counter}")

    print(f"Total number of files processed in {src_dir}: {counter}")
