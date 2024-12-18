import cv2
import os
from time import sleep

# Function to initialize the cameras
def initialize_cameras(left_camera_id=0, right_camera_id=1):
    left_cap = cv2.VideoCapture(left_camera_id)
    right_cap = cv2.VideoCapture(right_camera_id)
    
    if not left_cap.isOpened() or not right_cap.isOpened():
        print("Unable to open cameras. Please check the connection.")
        return None, None
    
    return left_cap, right_cap

# Function to create directories for saving images
def create_folders(left_folder='left', right_folder='right'):
    os.makedirs(left_folder, exist_ok=True)
    os.makedirs(right_folder, exist_ok=True)

# Function to capture and save images
def capture_and_save_images(left_cap, right_cap, left_folder, right_folder, image_count=50):
    for i in range(image_count):
        # Capture frames from both cameras
        ret_left, frame_left = left_cap.read()
        ret_right, frame_right = right_cap.read()

        if not ret_left or not ret_right:
            print("Unable to capture frames. Please check the cameras.")
            break

        # Save the images
        left_image_path = os.path.join(left_folder, f"left_{i+1}.jpg")
        right_image_path = os.path.join(right_folder, f"right_{i+1}.jpg")
        cv2.imwrite(left_image_path, frame_left)
        cv2.imwrite(right_image_path, frame_right)

        # Output the saved file paths
        print(f"Saved Left Image: {left_image_path}, Right Image: {right_image_path}")

        # Display images
        cv2.imshow('Left Camera', frame_left)
        cv2.imshow('Right Camera', frame_right)

        sleep(5)

# Function to release the cameras and close all windows
def release_resources(left_cap, right_cap):
    left_cap.release()
    right_cap.release()
    cv2.destroyAllWindows()

# Main function
def main():
    # Initialize cameras
    left_cap, right_cap = initialize_cameras()

    if left_cap is None or right_cap is None:
        return

    # Create folders to save images
    create_folders(left_folder='left', right_folder='right')

    # Capture and save 50 pairs of images
    capture_and_save_images(left_cap, right_cap, left_folder='left', right_folder='right', image_count=50)

    # Release resources after capturing images
    release_resources(left_cap, right_cap)

    print("Image capturing and saving completed.")

if __name__ == "__main__":
    main()
