# 🎯 YOLOv5 Object Detection Web Application

A modern, feature-rich web application for real-time object detection using YOLOv5. Upload images/videos or use live camera detection with a beautiful, premium UI.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.7-red)
![Flask](https://img.shields.io/badge/Flask-3.1-green)
![YOLOv5](https://img.shields.io/badge/YOLOv5-Latest-orange)

## ✨ Features

### 🎯 Dual Detection Modes

#### 📤 **Upload Mode**
- Upload images (JPG, PNG, GIF, BMP)
- Upload videos (MP4, AVI, MOV, MKV)
- Drag & drop support
- Batch processing
- Download processed results

#### 📹 **Live Camera Mode**
- Real-time webcam detection
- Multi-colored bounding boxes
- Object numbering and confidence scores
- Live statistics (FPS, object count, classes)
- Capture frames
- Format: `object_name - number - (confidence)`

### 🎨 Premium UI/UX Design
- **Modern dark theme** with cyan & pink gradients
- **Glassmorphism effects** with backdrop blur
- **Smooth animations** (floating icons, rotating borders, shimmer effects)
- **Responsive design** (mobile & desktop)
- **Multi-colored detections** for better visibility

### 🔍 Detection Capabilities
- **80+ object classes** (COCO dataset)
- People, vehicles, animals, furniture, electronics, food, sports equipment
- High accuracy with YOLOv5s model
- Adjustable confidence threshold

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/yolov5-web-app.git
cd yolov5-web-app

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Then open your browser and navigate to:
- **Upload Mode**: http://localhost:5000
- **Live Camera**: http://localhost:5000/camera

## 📖 Usage

### Upload Mode
1. Go to http://localhost:5000
2. Drag & drop or click to select an image/video
3. Wait for processing
4. View results with statistics
5. Download processed file

### Live Camera Mode
1. Go to http://localhost:5000/camera
2. Click "🎥 Start Camera"
3. Allow camera permissions
4. Watch real-time detection with colored bounding boxes
5. Capture frames if needed
6. Click "⏹️ Stop Camera" when done

## 🎨 Detection Visualization

Live camera shows detections in this format:
```
person - 1 - (0.98)
person - 2 - (0.95)
car - 1 - (0.92)
```

Each object type gets:
- Unique color coding
- Sequential numbering
- Confidence score in parentheses
- Colored bounding box

## 🛠️ Technology Stack

- **Backend**: Flask 3.1.2
- **AI Model**: YOLOv5s (PyTorch)
- **Frontend**: HTML5, CSS3, JavaScript
- **Camera**: WebRTC API
- **Styling**: Custom CSS with glassmorphism

## 📁 Project Structure

```
yolov5/
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── templates/
│   ├── index.html             # Upload mode page
│   └── camera.html            # Live camera page
├── static/
│   ├── style_premium.css      # Premium UI styles
│   ├── script.js              # Upload mode JS
│   └── results/               # Processed files
├── uploads/                   # Temporary uploads
├── data/
│   └── images/                # Sample images
└── docs/                      # Documentation files
```

## 🎯 Detected Objects

The system can detect 80+ object classes including:

**People & Animals**: person, dog, cat, horse, cow, elephant, bear, zebra, giraffe

**Vehicles**: car, bus, truck, motorcycle, bicycle, airplane, train, boat

**Indoor**: chair, couch, bed, dining table, tv, laptop, mouse, keyboard, cell phone

**Outdoor**: traffic light, fire hydrant, stop sign, parking meter, bench

**Food**: banana, apple, sandwich, orange, pizza, donut, cake

**Sports**: sports ball, baseball bat, skateboard, surfboard, tennis racket

## ⚙️ Configuration

### Change Detection Model
Edit `app.py`:
```python
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
# Options: yolov5n, yolov5s, yolov5m, yolov5l, yolov5x
```

### Adjust Confidence Threshold
Edit `app.py`:
```python
results = model(img_array, conf=0.5)  # Change 0.5 (0.0-1.0)
```

### Change Port
Edit `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change port
```

### Customize Colors
Edit `static/style_premium.css`:
```css
:root {
    --primary-gradient: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
    --secondary-gradient: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
}
```

## 📊 Performance

- **Image Detection**: 1-2 seconds
- **Video Processing**: Depends on length
- **Live Camera**: 2 FPS detection rate, 30 FPS video
- **Model**: YOLOv5s (7.2M parameters)

## 🎨 UI Features

- **Dark Theme**: Cyan & pink gradient accents
- **Glassmorphism**: Frosted glass cards with blur
- **Animations**: Floating icons, rotating borders, shimmer effects
- **Responsive**: Works on mobile and desktop
- **Accessibility**: High contrast, readable fonts

## 🔧 Troubleshooting

### Camera Not Working
- Ensure camera permissions are granted
- Check if another app is using the camera
- Try different browser (Chrome recommended)
- Change source from 0 to 1 or 2

### Model Not Loading
- Ensure internet connection (downloads on first use)
- Check disk space (~14MB needed)
- Verify PyTorch installation

### Upload Fails
- Check file size (max 100MB)
- Verify file format is supported
- Ensure sufficient disk space

## 📚 Documentation

- **START_HERE.md** - Complete overview
- **LIVE_CAMERA_GUIDE.md** - Camera mode guide
- **WEB_APP_GUIDE.md** - Full web app documentation
- **CREATIVE_UI_COMPLETE.md** - UI/UX details
- **COMPLETE_FEATURES.txt** - Feature list

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the GPL-3.0 License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5) - Object detection model
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [PyTorch](https://pytorch.org/) - Deep learning framework

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**⭐ Star this repo if you find it useful!**

Made with ❤️ using YOLOv5
