import cv2

def list_cameras():
    """
    List all available camera IDs.
    """
    cameras = []
    for camera_id in range(10):  # Test for camera IDs from 0 to 9
        cap = cv2.VideoCapture(camera_id)
        if cap.isOpened():
            cameras.append(camera_id)
            cap.release()
    return cameras

def display_camera(camera_id):
    """
    Display the live feed from the specified camera ID.
    """
    cap = cv2.VideoCapture(camera_id)
    if cap.isOpened():
        print(f"Displaying camera {camera_id}. Press 'q' to close.")
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow(f"Camera {camera_id}", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    else:
        print(f"Camera {camera_id} could not be opened.")

def main():
    """
    Main function to list cameras and display each one.
    """
    cameras = list_cameras()
    if cameras:
        print(f"Found {len(cameras)} camera(s):")
        for camera_id in cameras:
            print(f"Camera ID: {camera_id}")
            display_camera(camera_id)  # Display the camera feed
    else:
        print("No cameras found!")

if __name__ == "__main__":
    main()
