# 🌐 YOLOv5 Object Detection Web Application

A modern, user-friendly web application for object detection using YOLOv5. Users can upload images or videos and get instant detection results with beautiful visualizations.

## ✨ Features

- 📤 **Drag & Drop Upload** - Easy file upload interface
- 🖼️ **Image Detection** - Detect objects in JPG, PNG, GIF, BMP images
- 🎥 **Video Detection** - Process MP4, AVI, MOV, MKV videos
- 📊 **Real-time Statistics** - View detection counts and statistics
- 💾 **Download Results** - Save processed images/videos
- 🎨 **Modern UI** - Beautiful, responsive design
- ⚡ **Fast Processing** - Powered by YOLOv5s model

## 🚀 Quick Start

### 1. Install Flask (if not already installed)

```bash
pip install flask
```

Or install from requirements:

```bash
pip install -r requirements.txt
```

### 2. Run the Web Application

```bash
python app.py
```

### 3. Open Your Browser

Navigate to: **http://localhost:5000**

The server will start and you'll see:

```
YOLOv5 Object Detection Web Application
========================================
Starting server...
Access the application at: http://localhost:5000
```

## 📖 How to Use

### Upload an Image or Video

1. **Click** the upload box or **drag & drop** a file
2. Wait for processing (progress bar will show status)
3. View results with:
   - Annotated image/video with bounding boxes
   - Detection statistics
   - List of detected objects with counts
4. **Download** the result or **upload another file**

### Supported Formats

**Images:**

- JPG/JPEG
- PNG
- GIF
- BMP

**Videos:**

- MP4
- AVI
- MOV
- MKV

**Max File Size:** 100MB

## 🏗️ Project Structure

```
yolov5/
├── app.py                  # Flask backend application
├── templates/
│   └── index.html         # Main HTML template
├── static/
│   ├── style.css          # Modern CSS styling
│   ├── script.js          # Frontend JavaScript
│   └── results/           # Processed results (auto-created)
└── uploads/               # Temporary uploads (auto-created)
```

## 🎯 API Endpoints

### `GET /`

Main application page

### `POST /upload`

Upload and process file

**Request:**

- Method: POST
- Content-Type: multipart/form-data
- Body: file (image or video)

**Response:**

```json
{
  "success": true,
  "type": "image",
  "filename": "detected_20250114_143022_image.jpg",
  "result_url": "/static/results/detected_20250114_143022_image.jpg",
  "data": {
    "total_objects": 5,
    "object_counts": {
      "person": 4,
      "bus": 1
    },
    "detections": [...]
  }
}
```

### `GET /results/<filename>`

Download processed result file

## ⚙️ Configuration

Edit `app.py` to customize:

```python
# Maximum file size (default: 100MB)
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024

# Server host and port
app.run(debug=True, host="0.0.0.0", port=5000)

# Model selection (default: yolov5s)
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)
```

### Available Models

- `yolov5n` - Nano (fastest, least accurate)
- `yolov5s` - Small (balanced) ⭐ **Default**
- `yolov5m` - Medium
- `yolov5l` - Large
- `yolov5x` - Extra Large (slowest, most accurate)

## 🎨 Customization

### Change Colors

Edit `static/style.css`:

```css
:root {
  --primary-color: #4f46e5; /* Main color */
  --primary-dark: #4338ca; /* Hover color */
  --success-color: #10b981; /* Success messages */
}
```

### Modify Detection Confidence

Edit `app.py`:

```python
# In detect_image() or detect_video()
results = model(image_path, conf=0.5)  # Change 0.5 to desired threshold
```

## 🔧 Troubleshooting

### Port Already in Use

Change the port in `app.py`:

```python
app.run(debug=True, host="0.0.0.0", port=5001)  # Use different port
```

### Model Not Loading

The model downloads automatically on first run. Ensure:

- Internet connection is active
- Sufficient disk space (~14MB for yolov5s)

### Upload Fails

Check:

- File size is under 100MB
- File format is supported
- Sufficient disk space for processing

### Video Processing is Slow

- Use smaller videos or lower resolution
- Consider using `yolov5n` (faster model)
- Process fewer frames (modify `app.py`)

## 🌐 Deploy to Production

### Using Gunicorn (Linux/Mac)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Using Waitress (Windows)

```bash
pip install waitress
waitress-serve --host=0.0.0.0 --port=5000 app:app
```

### Environment Variables

```bash
export FLASK_ENV=production
export FLASK_DEBUG=0
```

## 📊 Performance Tips

1. **Use GPU** - Install PyTorch with CUDA for faster processing
2. **Reduce Video FPS** - Process every Nth frame for faster results
3. **Use Smaller Model** - yolov5n is 5x faster than yolov5x
4. **Limit File Size** - Smaller files process faster

## 🔒 Security Notes

For production deployment:

- Set `debug=False` in `app.run()`
- Add file validation and sanitization
- Implement rate limiting
- Use HTTPS
- Add authentication if needed

## 📝 Example Usage

### Python API Call

```python
import requests

url = "http://localhost:5000/upload"
files = {"file": open("image.jpg", "rb")}
response = requests.post(url, files=files)
result = response.json()

print(f"Detected {result['data']['total_objects']} objects")
print(f"Result URL: {result['result_url']}")
```

### cURL

```bash
curl -X POST -F "file=@image.jpg" http://localhost:5000/upload
```

## 🎓 Advanced Features

### Add Custom Classes

Modify the model to detect custom objects by training on your dataset. See YOLOv5 training documentation.

### Batch Processing

Extend `app.py` to accept multiple files and process them in parallel.

### Real-time Webcam

Add a webcam endpoint using WebRTC or streaming.

## 📚 Resources

- [YOLOv5 Documentation](https://docs.ultralytics.com/yolov5/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [PyTorch Hub](https://pytorch.org/hub/)

## 🆘 Support

If you encounter issues:

1. Check the console output for error messages
2. Verify all dependencies are installed
3. Ensure the model loaded successfully
4. Check file permissions for uploads and results folders

---

**Enjoy detecting objects with YOLOv5!** 🎉
