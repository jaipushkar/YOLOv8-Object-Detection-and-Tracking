# YOLOv8-Object-Detection-and-Tracking

**Overview**
This project demonstrates object detection and tracking using the YOLOv8 (You Only Look Once) model for real-time video processing. The application detects various objects in both images and videos, tracks their movements, and counts specific object classes such as cars, trucks, buses, and motorbikes.

**Features**
Real-Time Object Detection: Detects multiple objects using pre-trained YOLOv8 models on static images and video streams.
Object Tracking: Uses SORT (Simple Online and Realtime Tracking) to track the detected objects and assign unique IDs for each.
Object Counting: Counts selected object classes as they cross predefined regions in the video frame.
Mask Region of Interest (ROI): Applies a custom mask to focus detection on specific regions of the frame.

**Dependencies**
To run this project, you will need the following libraries and frameworks:
YOLOv8: For object detection.
OpenCV: For video stream processing and displaying output.
cvzone: For drawing bounding boxes and displaying text on the video frames.
NumPy: For efficient matrix operations.
SORT: For tracking detected objects across frames.

**How it Works**
Load Pre-trained YOLOv8 Model: The project uses a pre-trained YOLOv8 model to detect objects such as cars, motorbikes, buses, and more.
Video and Image Processing: The application supports processing both images and video files or live webcam streams.
Tracking and Counting: The system tracks and counts vehicles as they pass through a specified region of the video.
Visualization: Bounding boxes and tracking IDs are drawn on the detected objects in real-time.

**Applications**
Traffic Analysis: Detect and count vehicles on a busy road, track their movements, and analyze traffic flow.
Security Monitoring: Track people and objects across video feeds in real-time for surveillance.
Retail Analytics: Count and monitor foot traffic in retail environments.

**Future Improvements**
Integrating other object detection models.
Enhancing the tracking and detection performance in low-light conditions.
Adding support for more object classes.
