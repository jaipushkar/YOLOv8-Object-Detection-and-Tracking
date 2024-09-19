from ultralytics import YOLO
import cv2
model=YOLO('../YOLO-Weights/yolov8l.pt')
result=model("Images/school_bus.jpg",show=True )
cv2.waitKey(0)
