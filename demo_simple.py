"""Simple YOLOv5 Object Detection Demo This script demonstrates object detection on sample images."""

from pathlib import Path

import torch

print("=" * 60)
print("YOLOv5 Object Detection Demo")
print("=" * 60)

# Load YOLOv5 model
print("\n[1/3] Loading YOLOv5s model...")
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)
print("✓ Model loaded successfully!")

# Define image sources
images = ["data/images/bus.jpg", "data/images/zidane.jpg"]

print(f"\n[2/3] Running inference on {len(images)} images...")

# Run inference
results = model(images)

print("✓ Inference complete!")

# Display results
print("\n[3/3] Detection Results:")
print("-" * 60)

for i, img_path in enumerate(images):
    img_name = Path(img_path).name
    detections = results.pandas().xyxy[i]

    print(f"\n📷 Image: {img_name}")
    print(f"   Objects detected: {len(detections)}")

    if len(detections) > 0:
        # Count objects by class
        object_counts = detections["name"].value_counts()
        for obj_name, count in object_counts.items():
            print(f"   - {count}x {obj_name}")
    else:
        print("   - No objects detected")

print("\n" + "=" * 60)
print("Demo Complete!")
print("=" * 60)

# Save results
print("\n💾 Saving results to 'runs/detect/demo'...")
results.save(save_dir="runs/detect/demo")
print("✓ Results saved!")

print("\n📊 To view detailed results, check:")
print("   - runs/detect/demo/ (annotated images)")
print("\n🎯 Next steps:")
print("   - Run webcam detection: python cam_detect.py")
print("   - See RUN_DEMO.md for more options")
