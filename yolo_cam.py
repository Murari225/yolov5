from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # or yolov5s.pt if you have it

# Run real-time detection from webcam
model.predict(source=0, show=True, conf=0.5)
