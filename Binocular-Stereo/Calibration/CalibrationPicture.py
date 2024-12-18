import cv2
import os
print("OpenCV version:", cv2.__version__)

# Get the current directory of the script
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
print("Current script directory:", current_dir)

# Create folders (if not exist)
def create_folders(left_folder, right_folder):
    os.makedirs(left_folder, exist_ok=True)
    os.makedirs(right_folder, exist_ok=True)

# Get the next image index
def get_next_image_index(left_folder, right_folder):
    # Get all files from both folders
    left_files = os.listdir(left_folder)
    right_files = os.listdir(right_folder)

    # Extract image file numbers from both folders
    left_indices = [int(file.split('.')[0]) for file in left_files if file.endswith('.jpg') and file.split('.')[0].isdigit()]
    right_indices = [int(file.split('.')[0]) for file in right_files if file.endswith('.jpg') and file.split('.')[0].isdigit()]

    # Get the maximum number
    left_max = max(left_indices) if left_indices else 0
    right_max = max(right_indices) if right_indices else 0

    # Raise an error if the maximum numbers in both folders are different
    if left_max != right_max:
        return 0

    # Return the next index
    return left_max + 1


# Initialize cameras
def initialize_cameras(left_camera_id, right_camera_id):
    left_cap = cv2.VideoCapture(left_camera_id)
    right_cap = cv2.VideoCapture(right_camera_id)
    
    #left_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    #left_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    #right_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    #right_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    if not left_cap.isOpened() or not right_cap.isOpened():
        print("Failed to open cameras. Please check the connection.")
        left_cap.release()
        right_cap.release()
        return None, None

    return left_cap, right_cap

# Capture and save images
def capture_and_save_images(left_cap, right_cap, left_folder, right_folder, next_index):
    ret_left, frame_left = left_cap.read()
    ret_right, frame_right = right_cap.read()

    if ret_left and ret_right:
        # Save the images
        left_path = os.path.join(left_folder, f"{next_index}.jpg")
        right_path = os.path.join(right_folder, f"{next_index}.jpg")
        cv2.imwrite(left_path, frame_left)
        cv2.imwrite(right_path, frame_right)

        print(f"Saved successfully: Left Image {left_path}, Right Image {right_path}")
    else:
        print("Failed to capture images. Please check the cameras.")

# Main function
def capture_stereo_images():
    # Set paths
    left_folder = os.path.join(current_dir, "stereo-imgs-480P/left")
    right_folder = os.path.join(current_dir, "stereo-imgs-480P/right")

    # Create folders
    create_folders(left_folder, right_folder)

    # Initialize cameras
    # If there are more than two network heads, change id to try
    left_camera_id = 1  # Left camera ID
    right_camera_id = 2  # Right camera ID
    left_cap, right_cap = initialize_cameras(left_camera_id, right_camera_id)
    if not left_cap or not right_cap:
        print("Error: Camera not connected.")
        return

    # Get the next image index
    next_index = get_next_image_index(left_folder, right_folder)
    if next_index == 0:
        print("Error: The image indices in left and right folders are not consistent.")
        return

    # Capture and save images
    capture_and_save_images(left_cap, right_cap, left_folder, right_folder, next_index)

    # Release resources
    left_cap.release()
    right_cap.release()
    cv2.destroyAllWindows()

# Call the main function
if __name__ == "__main__":
    capture_stereo_images()
