# 📹 Live Camera Detection - User Guide

## 🎥 Real-Time Object Detection with Your Webcam

Your YOLOv5 web application now includes **live camera detection** for real-time object detection!

---

## 🚀 How to Use

### **Step 1: Start the Web Application**

```bash
python app.py
```

### **Step 2: Open the Camera Page**

```
http://localhost:5000/camera
```

### **Step 3: Start Detection**

1. Click **"🎥 Start Camera"** button
2. Allow camera permissions when prompted
3. Watch real-time object detection!

---

## ✨ Features

### **Real-Time Detection**

- 📹 Live video feed from your webcam
- 🎯 Objects detected and highlighted in real-time
- 📊 Live statistics (FPS, object count, classes)
- 🔄 Updates every 500ms (2 detections per second)

### **Visual Feedback**

- **Bounding Boxes**: Purple boxes around detected objects
- **Labels**: Object name + confidence percentage
- **Overlay**: Quick summary of detected objects
- **Status Indicator**: Shows camera active/inactive

### **Live Statistics**

- **FPS**: Frames per second
- **Objects Detected**: Total number of objects in current frame
- **Unique Classes**: Number of different object types

### **Controls**

- **🎥 Start Camera**: Activate webcam and begin detection
- **⏹️ Stop Camera**: Stop detection and turn off camera
- **📸 Capture Frame**: Save current frame with detections

---

## 🎨 Interface Elements

### **Header**

- Navigation between Upload and Camera modes
- Status indicator (green = active, red = inactive)

### **Live Stats Cards**

```
┌──────────┐  ┌──────────┐  ┌──────────┐
│    30    │  │    5     │  │    3     │
│   FPS    │  │ Objects  │  │ Classes  │
└──────────┘  └──────────┘  └──────────┘
```

### **Video Feed**

- Live camera stream
- Bounding boxes drawn on detected objects
- Labels with confidence scores
- Bottom overlay with quick summary

### **Detection List**

- Real-time list of currently detected objects
- Sorted by count (most detected first)
- Updates automatically

---

## 🎯 Detection Process

1. **Camera Capture**: Video stream from webcam
2. **Frame Extraction**: Captures frame every 500ms
3. **AI Processing**: YOLOv5 analyzes the frame
4. **Drawing**: Bounding boxes and labels added
5. **Display**: Results shown in real-time

---

## 📊 Performance

- **Detection Rate**: 2 FPS (every 500ms)
- **Video FPS**: 30 FPS (smooth video)
- **Latency**: ~500ms from capture to display
- **Accuracy**: Same as YOLOv5s model

---

## 🎨 Visual Design

### **Bounding Boxes**

- Color: Purple (#667eea)
- Width: 3px
- Style: Solid line

### **Labels**

- Background: Purple gradient
- Text: White
- Format: "object_name confidence%"

### **Overlay**

- Background: Semi-transparent black
- Position: Bottom of video
- Content: "Detected: 4x person, 1x bus"

---

## 🔧 Browser Requirements

### **Supported Browsers**

- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Opera

### **Required Permissions**

- Camera access (will prompt on first use)

### **Recommended**

- Modern browser (latest version)
- Good internet connection (for loading)
- Decent webcam (720p or better)

---

## 💡 Tips for Best Results

### **Lighting**

- Use good lighting for better detection
- Avoid backlighting
- Natural light works best

### **Camera Position**

- Position camera at eye level
- Keep objects in center of frame
- Maintain reasonable distance

### **Performance**

- Close other camera-using apps
- Use Chrome for best performance
- Ensure good CPU/GPU

---

## 🎯 Use Cases

### **Security**

- Monitor room for people
- Detect unauthorized objects
- Track movement

### **Inventory**

- Count items in real-time
- Verify product presence
- Monitor stock levels

### **Education**

- Demonstrate AI capabilities
- Interactive learning
- Object recognition training

### **Fun**

- Show off to friends
- Test different objects
- Explore AI capabilities

---

## 🔄 Workflow

```
1. Start Camera
   ↓
2. Grant Permissions
   ↓
3. Camera Activates
   ↓
4. Detection Begins
   ↓
5. View Real-Time Results
   ↓
6. Capture Frames (Optional)
   ↓
7. Stop Camera
```

---

## 📸 Capture Feature

### **How to Capture**

1. Click **"📸 Capture Frame"** button
2. Current frame with detections is saved
3. File downloads automatically
4. Filename: `detection_[timestamp].jpg`

### **What's Captured**

- Current video frame
- All bounding boxes
- All labels
- Timestamp in filename

---

## 🎨 UI Features

### **Premium Design**

- Dark theme with gradients
- Glassmorphism cards
- Smooth animations
- Responsive layout

### **Status Indicator**

- **Green pulsing dot**: Camera active
- **Red static dot**: Camera inactive
- Text shows current status

### **Navigation**

- Switch between Upload and Camera modes
- Active mode highlighted
- Smooth transitions

---

## 🔧 Troubleshooting

### **Camera Not Starting**

- Check browser permissions
- Ensure camera is not in use by another app
- Try different browser
- Refresh the page

### **No Detections Showing**

- Ensure good lighting
- Check if objects are in frame
- Wait a few seconds for processing
- Try different objects

### **Low FPS**

- Close other applications
- Use Chrome browser
- Check CPU usage
- Reduce video quality

### **Permission Denied**

- Click the camera icon in address bar
- Allow camera access
- Refresh the page
- Check browser settings

---

## 🌟 Advanced Features

### **Adjustable Detection Rate**

Edit `camera.html` to change detection frequency:

```javascript
detectionInterval = setInterval(async () => {
  await detectFrame();
}, 500); // Change 500 to desired milliseconds
```

### **Custom Confidence Threshold**

Modify server-side detection in `app.py`:

```python
results = model(img_array, conf=0.5)  # Change 0.5
```

---

## 📊 Statistics Explained

### **FPS (Frames Per Second)**

- Video playback rate
- Higher = smoother video
- Typically 25-30 FPS

### **Objects Detected**

- Total objects in current frame
- Updates in real-time
- Includes duplicates

### **Unique Classes**

- Number of different object types
- Example: 4 persons + 1 bus = 2 classes

---

## 🎯 Detected Objects

The system can detect **80+ object classes**:

**Common Objects:**

- 👥 People
- 🚗 Vehicles (car, bus, truck, motorcycle)
- 🐾 Animals (dog, cat, horse, etc.)
- 🪑 Furniture (chair, couch, table)
- 📱 Electronics (laptop, phone, TV)
- 🍕 Food items
- ⚽ Sports equipment

---

## 🔐 Privacy & Security

### **Data Handling**

- Video processed locally in browser
- Frames sent to server for detection only
- No video recording
- No data storage

### **Camera Access**

- Only used when you click "Start Camera"
- Stops when you click "Stop Camera"
- Browser controls access
- Can revoke anytime

---

## 🎉 Benefits

### **Real-Time**

- Instant feedback
- No upload needed
- Live monitoring

### **Interactive**

- Move objects around
- See detection change
- Immediate results

### **Educational**

- Learn about AI
- See how detection works
- Experiment with objects

### **Practical**

- Security monitoring
- Inventory counting
- Object tracking

---

## 🚀 Next Steps

1. **Try It Out**: Start camera and test with different objects
2. **Experiment**: Try various lighting and angles
3. **Capture**: Save interesting detections
4. **Share**: Show friends and colleagues
5. **Customize**: Adjust settings for your needs

---

## 📚 Related Features

- **Upload Mode**: Detect objects in images/videos
- **Batch Processing**: Process multiple files
- **Download Results**: Save processed files
- **API Access**: Integrate with other apps

---

## 💡 Pro Tips

1. **Best Lighting**: Natural daylight or bright room lights
2. **Camera Angle**: Straight-on view works best
3. **Object Size**: Medium-sized objects detect better
4. **Background**: Plain backgrounds improve accuracy
5. **Distance**: 1-3 meters from camera is optimal

---

## 🎊 Enjoy Live Detection!

Your YOLOv5 web application now has **real-time camera detection**!

**Start detecting:**

```bash
python app.py
# Open: http://localhost:5000/camera
```

**Experience AI-powered live object detection!** 📹✨
