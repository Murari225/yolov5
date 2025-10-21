"""YOLOv5 Object Detection Web Application Upload images or videos for real-time object detection."""

import os
from datetime import datetime

import cv2
import torch
from flask import Flask, jsonify, render_template, request, send_from_directory, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = "uploads"
RESULTS_FOLDER = "static/results"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "bmp", "mp4", "avi", "mov", "mkv"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["RESULTS_FOLDER"] = RESULTS_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024  # 100MB max file size

# Create necessary folders
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

# Load YOLOv5 model (cached globally)
print("Loading YOLOv5 model...")
model = None


def load_model():
    global model
    if model is None:
        model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)
        print("✓ Model loaded successfully!")
    return model


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def is_video(filename):
    video_extensions = {"mp4", "avi", "mov", "mkv"}
    return "." in filename and filename.rsplit(".", 1)[1].lower() in video_extensions


def detect_image(image_path, output_path):
    """Run detection on an image."""
    model = load_model()

    # Run inference
    results = model(image_path)

    # Get detection data
    detections = results.pandas().xyxy[0]

    # Count objects
    object_counts = {}
    if len(detections) > 0:
        object_counts = detections["name"].value_counts().to_dict()

    # Save annotated image
    results.save(save_dir=os.path.dirname(output_path))

    # Rename to expected output path
    saved_path = os.path.join(os.path.dirname(output_path), os.path.basename(image_path))
    if os.path.exists(saved_path):
        os.replace(saved_path, output_path)

    return {
        "total_objects": len(detections),
        "object_counts": object_counts,
        "detections": detections.to_dict("records"),
    }


def detect_video(video_path, output_path):
    """Run detection on a video."""
    model = load_model()

    # Open video
    cap = cv2.VideoCapture(video_path)

    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    frame_count = 0
    all_detections = []

    print(f"Processing video: {total_frames} frames at {fps} FPS")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Run detection on frame
        results = model(frame)

        # Get annotated frame
        annotated_frame = results.render()[0]

        # Write frame
        out.write(annotated_frame)

        # Collect detection stats (sample every 30 frames to avoid too much data)
        if frame_count % 30 == 0:
            detections = results.pandas().xyxy[0]
            if len(detections) > 0:
                all_detections.extend(detections["name"].tolist())

        frame_count += 1

    cap.release()
    out.release()

    # Calculate statistics
    object_counts = {}
    if all_detections:
        from collections import Counter

        object_counts = dict(Counter(all_detections))

    return {
        "total_frames": total_frames,
        "processed_frames": frame_count,
        "fps": fps,
        "object_counts": object_counts,
        "total_detections": len(all_detections),
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/camera")
def camera():
    return render_template("camera.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify(
            {"error": "Invalid file type. Allowed: images (jpg, png, etc.) and videos (mp4, avi, etc.)"}
        ), 400

    try:
        # Save uploaded file
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_filename = f"{timestamp}_{filename}"

        upload_path = os.path.join(app.config["UPLOAD_FOLDER"], unique_filename)
        file.save(upload_path)

        # Prepare output path
        output_filename = f"detected_{unique_filename}"
        output_path = os.path.join(app.config["RESULTS_FOLDER"], output_filename)

        # Run detection
        if is_video(filename):
            print(f"Processing video: {filename}")
            result_data = detect_video(upload_path, output_path)
            result_type = "video"
        else:
            print(f"Processing image: {filename}")
            result_data = detect_image(upload_path, output_path)
            result_type = "image"

        # Clean up uploaded file
        os.remove(upload_path)

        return jsonify(
            {
                "success": True,
                "type": result_type,
                "filename": output_filename,
                "result_url": url_for("static", filename=f"results/{output_filename}"),
                "data": result_data,
            }
        )

    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return jsonify({"error": f"Error processing file: {str(e)}"}), 500


@app.route("/results/<filename>")
def get_result(filename):
    return send_from_directory(app.config["RESULTS_FOLDER"], filename)


@app.route("/detect_frame", methods=["POST"])
def detect_frame():
    try:
        data = request.get_json()
        image_data = data.get("image", "")

        # Decode base64 image
        if "," in image_data:
            image_data = image_data.split(",")[1]

        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))

        # Convert to numpy array
        img_array = np.array(image)

        # Load model
        model = load_model()

        # Run detection
        results = model(img_array)

        # Get detections
        detections = results.pandas().xyxy[0]

        # Convert to list of dicts
        detection_list = []
        if len(detections) > 0:
            for _, row in detections.iterrows():
                detection_list.append(
                    {
                        "xmin": float(row["xmin"]),
                        "ymin": float(row["ymin"]),
                        "xmax": float(row["xmax"]),
                        "ymax": float(row["ymax"]),
                        "confidence": float(row["confidence"]),
                        "class": int(row["class"]),
                        "name": row["name"],
                    }
                )

        return jsonify({"success": True, "detections": detection_list, "count": len(detection_list)})

    except Exception as e:
        print(f"Error in detect_frame: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
    print("=" * 60)
    print("YOLOv5 Object Detection Web Application")
    print("=" * 60)
    print("\nStarting server...")
    print("Access the application at: http://localhost:5000")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 60)

    app.run(debug=True, host="0.0.0.0", port=5000)
