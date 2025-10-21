# 🎯 YOLOv5 Web Application - Quick Start

## 🚀 Start the Web Application

### Option 1: Double-click the batch file (Easiest)

```
start_webapp.bat
```

### Option 2: Command line

```bash
# Activate virtual environment (if using venv)
venv\Scripts\activate

# Run the app
python app.py
```

### Option 3: Without virtual environment

```bash
python app.py
```

## 🌐 Access the Application

Once started, open your browser and navigate to:

**http://localhost:5000**

You'll see a beautiful web interface where you can:

- 📤 Upload images or videos
- 🔍 Detect objects automatically
- 📊 View detection statistics
- 💾 Download results

## 📸 How to Use

1. **Upload a File**
   - Click the upload box or drag & drop
   - Supports: JPG, PNG, GIF, BMP, MP4, AVI, MOV
   - Max size: 100MB

2. **Wait for Processing**
   - Progress bar shows upload and processing status
   - YOLOv5 analyzes your image/video

3. **View Results**
   - See annotated image/video with bounding boxes
   - Check detection statistics
   - View list of detected objects

4. **Download or Upload Another**
   - Download the processed file
   - Upload another file to detect more objects

## 🎨 Features

✅ **Drag & Drop Upload** - Easy file upload  
✅ **Image Detection** - Detect objects in photos  
✅ **Video Detection** - Process entire videos  
✅ **Real-time Stats** - See detection counts  
✅ **Modern UI** - Beautiful, responsive design  
✅ **Download Results** - Save processed files

## 📁 File Structure

```
yolov5/
├── app.py                 # Main Flask application
├── start_webapp.bat       # Easy startup script
├── templates/
│   └── index.html        # Web interface
├── static/
│   ├── style.css         # Styling
│   ├── script.js         # Frontend logic
│   └── results/          # Processed files (auto-created)
└── uploads/              # Temp uploads (auto-created)
```

## ⚙️ Configuration

### Change Port

Edit `app.py`, line at the bottom:

```python
app.run(debug=True, host="0.0.0.0", port=5000)  # Change 5000 to desired port
```

### Change Model

Edit `app.py`, in `load_model()` function:

```python
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)
# Options: yolov5n, yolov5s, yolov5m, yolov5l, yolov5x
```

### Adjust Confidence Threshold

Edit `app.py`, in detection functions:

```python
results = model(image_path, conf=0.5)  # Change 0.5 (0.0-1.0)
```

## 🔧 Troubleshooting

### "Port already in use"

- Change the port number in `app.py`
- Or stop other applications using port 5000

### "Module not found: flask"

```bash
pip install flask
```

### Model not loading

- Ensure internet connection (downloads on first run)
- Check disk space (~14MB needed)

### Upload fails

- Check file size (max 100MB)
- Verify file format is supported
- Ensure sufficient disk space

## 📊 Example Results

### Image Detection

- Input: `bus.jpg`
- Output: Detected 4 persons, 1 bus
- Processing: ~1-2 seconds

### Video Detection

- Input: `video.mp4` (30 seconds)
- Output: Annotated video with detections
- Processing: ~30-60 seconds (depends on length)

## 🎓 Advanced Usage

### API Access

```python
import requests

url = "http://localhost:5000/upload"
files = {"file": open("image.jpg", "rb")}
response = requests.post(url, files=files)
print(response.json())
```

### Custom Detection

See `WEB_APP_GUIDE.md` for detailed customization options.

## 📚 Documentation

- **WEB_APP_GUIDE.md** - Complete guide with API docs
- **QUICK_START.txt** - General YOLOv5 commands
- **RUN_DEMO.md** - Detection demos and examples

## 🆘 Need Help?

1. Check console output for errors
2. Verify all dependencies installed: `pip install -r requirements.txt`
3. Ensure model loaded successfully
4. Check `WEB_APP_GUIDE.md` for detailed troubleshooting

---

**Ready to detect objects!** 🎉

Just run `start_webapp.bat` or `python app.py` and open http://localhost:5000
