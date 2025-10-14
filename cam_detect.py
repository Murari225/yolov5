from ultralytics import YOLO

# Load the YOLOv8 model (you can use 'yolov5s.pt' or 'yolov8n.pt')
model = YOLO("yolov8n.pt")  # 'n' = nano, fast and light

# Run detection on webcam (0 = default webcam)
model.predict(source=0, show=True, conf=0.5)
