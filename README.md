# Chemistry Lab Detection System 🔬

A computer vision system for real-time detection and analysis of laboratory vessels and equipment.

## Project Overview ✨

This project employs a cascade detection approach to identify laboratory vessels and determine their pose/orientation. The system utilizes **two-stage detection**:
1. First detecting the vessel's boundary box
2. Then analyzing the vessel's precise pose and orientation

## Key Features 🚀

- **Real-time vessel detection** in video streams
- Advanced cascade detection framework (boundary box → pose detection)
- Performance monitoring with FPS calculation and display
- Comprehensive support for **multiple vessel types**
- High accuracy pose estimation

## Project Structure 📁

```
Chem_Lab_detect/
├── models/                  # Trained ML models
│   ├── vessels-bbox-nano.pt # Vessel boundary box detection model
│   └── vessel-pose-nano.pt  # Vessel pose detection model
├── vessel_detect/           # Core detection modules
│   ├── vessel_bbox.py       # Boundary box detection
│   ├── vessel_pose.py       # Pose detection
│   └── vessel_cascade.py    # Cascade detection pipeline
├── utils/                   # Utility functions
│   ├── fps_calculator.py    # FPS calculation
│   └── draw_fps.py          # FPS display functions
```

## Usage 💻

Basic usage example:

```python
from vessel_detect.vessel_cascade import VesselCascadeDetector

# Initialize the detector with default models
detector = VesselCascadeDetector()

# Process video from webcam
detector.process_video(0)  # Use camera index 0

# Process a video file
detector.process_video("path/to/video.mp4")

# Process a single frame
processed_frame, detection_info = detector.detect_frame(image)
```

## Requirements ⚙️

- OpenCV 4.5+
- NumPy 1.20+
- PyTorch 1.8+ (for the detection models)

## Installation 📋

Clone the repository and ensure you have the **required models** in the `models/` directory:

```bash
git clone https://github.com/yourusername/Chem_Lab_detect.git
cd Chem_Lab_detect
```

---

## A Light Moment 🌸

```
試験管と
カメラの目が
見つめ合う
```

*Test tubes and flasks  
The camera's watchful eye  
They meet in silence*
