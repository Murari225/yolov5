# YOLOv5 Object Detection - Quick Start Guide

## ✅ Environment Status
- **Python Version**: 3.12.10
- **PyTorch**: 2.7.1 (CPU)
- **Ultralytics**: 8.3.151
- **OpenCV**: 4.11.0.86
- All dependencies are installed and ready!

## 🚀 Running Object Detection

### 1. Detect Objects in Images

Run detection on sample images:

```bash
# Detect objects in bus image
python detect.py --weights yolov5s.pt --source data/images/bus.jpg --conf 0.5

# Detect objects in zidane image
python detect.py --weights yolov5s.pt --source data/images/zidane.jpg --conf 0.5

# View results while detecting
python detect.py --weights yolov5s.pt --source data/images/bus.jpg --conf 0.5 --view-img
```

Results are saved to: `runs/detect/exp/`

### 2. Webcam Detection (Real-time)

You have 3 webcam detection scripts available:

#### Option A: Simple Webcam Detection
```bash
python yolo_cam.py
```

#### Option B: Basic Webcam Detection
```bash
python cam_detect.py
```

#### Option C: Webcam Detection with Logging
```bash
python cam_detect_save.py
```
This saves detected objects to `detected_objects_log.txt`

#### Option D: Using detect.py with webcam
```bash
python detect.py --weights yolov5s.pt --source 0 --conf 0.5
```

**Note**: Press 'q' to quit webcam detection

### 3. Detect Objects in Videos

```bash
python detect.py --weights yolov5s.pt --source path/to/video.mp4 --conf 0.5
```

### 4. Different Model Sizes

YOLOv5 offers different model sizes (speed vs accuracy trade-off):

```bash
# Nano (fastest, least accurate)
python detect.py --weights yolov5n.pt --source data/images/bus.jpg

# Small (default, balanced)
python detect.py --weights yolov5s.pt --source data/images/bus.jpg

# Medium (slower, more accurate)
python detect.py --weights yolov5m.pt --source data/images/bus.jpg

# Large (slowest, most accurate)
python detect.py --weights yolov5l.pt --source data/images/bus.jpg
```

## 📊 Recent Test Results

✅ Successfully detected:
- **Image**: `data/images/bus.jpg`
- **Objects Found**: 4 persons, 1 bus
- **Inference Time**: 289.0ms
- **Model**: YOLOv5s (7.2M parameters)

## 🎯 Available Models

The project includes:
- **YOLOv5 models**: yolov5n, yolov5s, yolov5m, yolov5l, yolov5x
- **YOLOv8 model**: yolov8n.pt (already downloaded)

## 📁 Project Structure

```
yolov5/
├── detect.py              # Main detection script
├── train.py               # Training script
├── val.py                 # Validation script
├── cam_detect.py          # Simple webcam detection
├── cam_detect_save.py     # Webcam detection with logging
├── yolo_cam.py            # Basic webcam detection
├── data/
│   └── images/            # Sample images (bus.jpg, zidane.jpg)
├── models/                # Model configurations
├── runs/
│   └── detect/            # Detection results saved here
└── requirements.txt       # Dependencies
```

## 🔧 Troubleshooting

### If webcam doesn't work:
1. Make sure your webcam is connected
2. Try changing source from `0` to `1` or `2`
3. Check if another application is using the webcam

### If models don't download:
Models are automatically downloaded on first use. Make sure you have internet connection.

## 📖 Additional Resources

- [YOLOv5 Documentation](https://docs.ultralytics.com/yolov5/)
- [Training Custom Data](https://docs.ultralytics.com/yolov5/tutorials/train_custom_data/)
- [Model Export](https://docs.ultralytics.com/yolov5/tutorials/model_export/)

---

**Ready to detect objects!** 🎉
