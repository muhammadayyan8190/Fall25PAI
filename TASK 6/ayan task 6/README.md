# Object Counting Video Project 🎬

A Flask-based web application for automatic object detection and counting in video files using YOLOv8.

## Features ✨

- **Video Upload**: Drag & drop or click to upload video files
- **Object Detection**: YOLOv8 powered real-time object detection
- **Count Display**: Shows detected objects and their counts
- **Video Playback**: Watch processed video with bounding boxes
- **Beautiful UI**: Modern, responsive web interface
- **Supported Formats**: MP4, AVI, MOV, MKV, FLV, WMV
- **Large File Support**: Up to 500MB video files

## Project Structure 📁

```
ayan task 6/
├── app.py                 # Flask main application
├── yolov8_detector.py     # Object detection logic
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Frontend HTML/CSS/JS
├── static/
│   └── outputs/           # Processed videos (auto-created)
└── uploads/               # Uploaded videos (auto-created)
```

## Installation & Setup 🚀

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- **Flask**: Web framework
- **OpenCV**: Video processing
- **YOLOv8**: Object detection model
- **PyTorch**: Deep learning framework
- **NumPy**: Numerical computing

### 2. Run the Application

```bash
python app.py
```

The application will start on: **http://localhost:5000**

## How to Use 🎯

1. **Open Browser**: Go to http://localhost:5000
2. **Upload Video**: 
   - Click the upload area or drag & drop a video
   - Select from your computer
3. **Analyze**: Click "Analyze Video" button
4. **View Results**: 
   - See detected objects count on the right
   - Watch processed video with bounding boxes
5. **Download**: Video is saved in `static/outputs/folder`

## What Gets Detected 🔍

YOLOv8 can detect 80+ object types including:
- **People**: person
- **Vehicles**: car, bus, truck, motorcycle, bicycle
- **Animals**: dog, cat, bird, horse, cow, sheep, elephant
- **Furniture**: chair, table, bed, couch, desk
- **Electronics**: laptop, monitor, keyboard, mouse
- **Food**: apple, banana, orange, pizza, cake
- **Kitchen**: bottle, cup, knife, fork, spoon
- **Sports**: baseball, soccer ball, tennis racket
- **And many more...**

## Troubleshooting 🔧

### Issue: YOLOv8 model not downloading
- **Solution**: First run will auto-download the model (~50MB). Ensure internet connection.

### Issue: Video processing is slow
- **Solution**: Use smaller videos or nano model is already optimized for speed.

### Issue: Port 5000 already in use
- **Solution**: Edit `app.py` and change `port=5000` to another port like `port=5001`

### Issue: Out of memory error
- **Solution**: Process smaller videos or reduce file size before uploading

## Performance Tips ⚡

1. **Video Size**: Use videos under 100MB for faster processing
2. **Resolution**: Lower resolution videos process faster
3. **Format**: MP4 format works best
4. **GPU**: If you have NVIDIA GPU, it will auto-use CUDA for faster GPU processing

## API Endpoints 📡

### POST /upload
Upload and process video
- Form Data: `file` (video file)
- Returns: JSON with detected objects and output video path

### GET /
Main page with upload interface

## Notes 📝

- Processed videos are saved in `static/outputs/`
- Original uploads are in `uploads/`
- First detection takes longer (YOLOv8 model loading)
- Each detection displays confidence scores for accuracy

## Requirements 💻

- Python 3.8+
- 2GB RAM minimum
- GPU recommended for faster processing (optional)
- Modern web browser

## Author

Created for object detection and counting analysis

---

**Enjoy analyzing your videos!** 🎥✨
