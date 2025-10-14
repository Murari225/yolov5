from ultralytics import YOLO
import cv2
from datetime import datetime

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

# Open file to save detected object names
output_file = open("detected_objects_log.txt", "w")
output_file.write("Timestamp\t\tDetected Objects\n")
output_file.write("=====================================\n")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run prediction on the current frame
    results = model.predict(source=frame, conf=0.5, save=False, show=False)

    # Get names of detected objects
    names = set()
    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            cls_name = model.names[cls_id]
            names.add(cls_name)

    # Show detections on screen
    annotated_frame = results[0].plot()
    cv2.imshow("YOLOv8 Live Detection", annotated_frame)

    # Save to file
    if names:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output_file.write(f"{timestamp}\t{', '.join(names)}\n")

    # Exit with 'q' key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
output_file.close()
print("Detection log saved as 'detected_objects_log.txt'")
