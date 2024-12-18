# Binocular-Stereo 🎥👓
![Project Status](https://img.shields.io/badge/status-active-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Contributors](https://img.shields.io/badge/contributors-3+-orange.svg)

Welcome to the **Stereo Camera 3D Reconstruction Project**! 
---

This project focuses on leveraging stereo camera technology to achieve real-time depth stream capturing and full 3D object reconstruction. It includes modules for camera calibration, real-time depth stream generation, 3D point cloud visualization, and multi-view 3D reconstruction.

## 📂 Project Structure

```plaintext
📦 Binocular-Stereo
├── 📁 Calibration/               
│      # Stereo camera calibration scripts and tools
├── 📁 RealTimeDepthStream/       
│      # Real-time depth stream capture and processing
├── 📁 PointCloudVisualization/   
│      # Generate and visualize 3D point clouds
├── 📁 MultiView3DReconstruction/ 
│      # Multi-view 3D object reconstruction
├── 📄 REPORT.md 
└── 📄 README.md                  
```
---
## 🚀 Features

1. **Stereo Camera Calibration**
   - Accurately calibrate stereo cameras to ensure optimal depth computation.

2. **Real-Time Depth Stream**
   - Capture and process real-time depth streams using the calibrated stereo camera.

3. **3D Point Cloud Visualization**
   - Capture a single stereo frame and generate the corresponding 3D point cloud for visualization.

4. **Multi-View 3D Reconstruction**
   - Reconstruct the full 3D model of an object using multi-view stereo frames.

---

## 🛠 Environment Setup

### 📌 Python Version  
To check your Python version, run the following command:  
```bash
python --version
```
Expected output:
```bash
Python 3.9.20
```
### 📌 OpenCV Version
```bash
import cv2
print(cv2.__version__)   
```
Expected output:
```bash
4.10.0
```
---
## 📸 Notes
1. Ensure that the entire calibration grid is visible in the captured photo.
2. If the grid is cropped or incomplete, the photo cannot be imported into MATLAB for calibration.
3. Ideal Reprojection Error Range:
   - ✅ Less than 0.5 Pixels (Excellent):  
     Highly accurate calibration parameters, suitable for high-precision applications, such as:
     - Industrial measurement
     - 3D reconstruction
   - ✅ Between 0.5 to 1 Pixel (Good):  
     Generally acceptable for most computer vision tasks, including:
     - Stereo vision
     - Object detection
   - ✅ Between 1 to 2 Pixels (Acceptable):  
     Suitable for low-resolution images or less demanding scenarios, such as general image correction.
   - ✅ Greater than 2 Pixels (Needs Improvement):  
     May indicate problems with the calibration process, such as:
     - Poor chessboard detection
     - Low-quality calibration images
     - Insufficient coverage of the field of view (not all areas captured)
     - Incorrect chessboard size settings
4. **Camera Support Package Installation and Testing**  
   To ensure your camera is properly set up and ready for calibration, follow these steps:

   ### 📦 Installing the Support Package:
   1. Open **MATLAB**.
   2. Go to the menu bar and select **Add-Ons > Get Hardware Support Packages**.
   3. Search for **MATLAB Support Package for USB Webcams**.
   4. Click **Install** and follow the prompts to complete the installation.
   5. After installation, verify the setup by running:
      ```matlab
      imaqhwinfo
      ```
      Check that the `InstalledAdaptors` list includes `winvideo` or another adapter. If so, the installation was successful.

   ### ✅ Checking Camera Functionality:
   #### **On the Operating System:**
   - **Windows:** Use the built-in **Camera** app to ensure the webcam is functional.  
   - **macOS:** Open **Photo Booth** to check the camera's operation.  

   #### **In MATLAB:**
   Use the following code to test if the camera is working correctly:
   ```matlab
   cam = webcam;          % Connect to the camera
   frame = snapshot(cam); % Capture an image frame
   imshow(frame);         % Display the image
   clear cam;             % Clear the camera object

## In order to learn more about the overall process of our project, I recommend reading [REPORT.pdf ](REPORT.pdf)!

