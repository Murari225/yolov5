# 🎯 YOLOv5 Object Detection - Complete Guide

## 🌟 What You Have

A complete YOLOv5 object detection system with:

1. ✅ **Command-line detection** (images, videos, webcam)
2. ✅ **Web application** (upload and detect via browser)
3. ✅ **Pre-trained models** (ready to use)
4. ✅ **Sample images** (for testing)

---

## 🚀 Quick Start Options

### Option 1: Web Application (Recommended for Beginners)

**Start the web server:**
```bash
# Double-click this file:
start_webapp.bat

# OR run:
python app.py
```

**Then open your browser:**
```
http://localhost:5000
```

**Features:**
- 📤 Drag & drop file upload
- 🖼️ Detect objects in images
- 🎥 Process videos
- 📊 View statistics
- 💾 Download results
- 🎨 Beautiful modern UI

---

### Option 2: Command Line Detection

**Detect in sample images:**
```bash
python detect.py --weights yolov5s.pt --source data/images/bus.jpg
```

**Webcam detection:**
```bash
python cam_detect.py
```

**Video detection:**
```bash
python detect.py --weights yolov5s.pt --source video.mp4
```

**Simple demo:**
```bash
python demo_simple.py
```

---

## 📁 Project Files

### Web Application Files
- **`app.py`** - Flask web server
- **`start_webapp.bat`** - Easy startup script
- **`templates/index.html`** - Web interface
- **`static/style.css`** - Styling
- **`static/script.js`** - Frontend logic

### Detection Scripts
- **`detect.py`** - Main detection script
- **`cam_detect.py`** - Webcam detection
- **`cam_detect_save.py`** - Webcam with logging
- **`demo_simple.py`** - Simple demo

### Documentation
- **`START_HERE.md`** - This file (overview)
- **`README_WEBAPP.md`** - Web app quick start
- **`WEB_APP_GUIDE.md`** - Complete web app guide
- **`QUICK_START.txt`** - Command reference
- **`RUN_DEMO.md`** - Detailed examples

### Sample Data
- **`data/images/bus.jpg`** - Test image 1
- **`data/images/zidane.jpg`** - Test image 2

---

## 🎯 Choose Your Path

### For Non-Technical Users
👉 **Use the Web Application**
1. Run `start_webapp.bat`
2. Open http://localhost:5000
3. Upload images/videos
4. Download results

### For Developers
👉 **Use Command Line**
1. See `QUICK_START.txt` for commands
2. Modify `detect.py` for custom needs
3. Check `RUN_DEMO.md` for examples

### For Integration
👉 **Use the API**
1. Start web app: `python app.py`
2. POST files to `/upload` endpoint
3. See `WEB_APP_GUIDE.md` for API docs

---

## 📊 What Can You Detect?

YOLOv5 can detect **80 different object classes** including:

**People & Animals:**
- person, cat, dog, horse, sheep, cow, elephant, bear, zebra, giraffe

**Vehicles:**
- bicycle, car, motorcycle, airplane, bus, train, truck, boat

**Indoor Objects:**
- chair, couch, bed, dining table, tv, laptop, mouse, keyboard, cell phone, book

**Outdoor Objects:**
- traffic light, fire hydrant, stop sign, parking meter, bench

**Sports:**
- sports ball, baseball bat, skateboard, surfboard, tennis racket

**Food:**
- banana, apple, sandwich, orange, broccoli, carrot, hot dog, pizza, donut, cake

...and many more!

---

## ⚙️ Available Models

| Model | Speed | Accuracy | Size | Use Case |
|-------|-------|----------|------|----------|
| yolov5n | ⚡⚡⚡⚡⚡ | ⭐⭐ | 1.9M | Real-time, mobile |
| yolov5s | ⚡⚡⚡⚡ | ⭐⭐⭐ | 7.2M | **Default, balanced** |
| yolov5m | ⚡⚡⚡ | ⭐⭐⭐⭐ | 21M | Better accuracy |
| yolov5l | ⚡⚡ | ⭐⭐⭐⭐⭐ | 46M | High accuracy |
| yolov5x | ⚡ | ⭐⭐⭐⭐⭐ | 87M | Best accuracy |

---

## 🎨 Example Workflows

### Workflow 1: Quick Image Detection
```bash
# 1. Run demo
python demo_simple.py

# 2. Check results in runs/detect/demo/
```

### Workflow 2: Web Upload
```bash
# 1. Start server
python app.py

# 2. Open browser: http://localhost:5000
# 3. Upload image
# 4. Download result
```

### Workflow 3: Batch Processing
```bash
# Detect all images in a folder
python detect.py --weights yolov5s.pt --source path/to/images/
```

### Workflow 4: Real-time Webcam
```bash
# Live detection from webcam
python cam_detect.py
# Press 'q' to quit
```

---

## 🔧 Common Tasks

### Change Detection Confidence
```bash
# Lower = more detections (may include false positives)
# Higher = fewer detections (more confident)
python detect.py --source image.jpg --conf 0.3  # Low confidence
python detect.py --source image.jpg --conf 0.7  # High confidence
```

### Use Different Model
```bash
# Faster (less accurate)
python detect.py --weights yolov5n.pt --source image.jpg

# More accurate (slower)
python detect.py --weights yolov5l.pt --source image.jpg
```

### Save Detection Labels
```bash
# Save text files with detection coordinates
python detect.py --source image.jpg --save-txt
```

### View Results While Detecting
```bash
python detect.py --source image.jpg --view-img
```

---

## 📚 Learn More

### Documentation Files
1. **README_WEBAPP.md** - Web app quick start
2. **WEB_APP_GUIDE.md** - Complete web app documentation
3. **QUICK_START.txt** - Command reference
4. **RUN_DEMO.md** - Detailed examples and tutorials

### Online Resources
- [YOLOv5 Official Docs](https://docs.ultralytics.com/yolov5/)
- [Training Custom Models](https://docs.ultralytics.com/yolov5/tutorials/train_custom_data/)
- [Model Export](https://docs.ultralytics.com/yolov5/tutorials/model_export/)

---

## 🆘 Troubleshooting

### Web App Won't Start
```bash
# Install Flask
pip install flask

# Or install all requirements
pip install -r requirements.txt
```

### Model Not Loading
- Ensure internet connection (downloads on first use)
- Check disk space (~14MB for yolov5s)

### Webcam Not Working
- Check if camera is connected
- Try different source: `--source 1` or `--source 2`
- Close other apps using the camera

### Slow Processing
- Use smaller model: `yolov5n.pt`
- Reduce image size
- Use GPU if available

---

## 🎉 You're Ready!

### To start detecting objects:

**Web Interface (Easiest):**
```bash
start_webapp.bat
```
Then open: http://localhost:5000

**Command Line:**
```bash
python demo_simple.py
```

**Webcam:**
```bash
python cam_detect.py
```

---

## 💡 Next Steps

1. ✅ Try the web application
2. ✅ Test with your own images
3. ✅ Experiment with different models
4. ✅ Adjust confidence thresholds
5. ✅ Process videos
6. ✅ Try real-time webcam detection

---

**Happy Detecting!** 🚀

For questions, check the documentation files or visit the YOLOv5 GitHub repository.
