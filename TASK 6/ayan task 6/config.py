# Configuration file for Object Counter Project

# Flask Configuration
FLASK_DEBUG = True
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 5000

# File Upload Configuration
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500MB in bytes
ALLOWED_VIDEO_FORMATS = ['mp4', 'avi', 'mov', 'mkv', 'flv', 'wmv']

# YOLOv8 Model Configuration
MODEL_NAME = 'yolov8n.pt'  # n=nano, s=small, m=medium, l=large, x=xlarge
CONFIDENCE_THRESHOLD = 0.5  # Minimum confidence score

# Folder Paths
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'static/outputs'
TEMP_FOLDER = 'temp'

# Video Processing
FPS_OUTPUT = None  # None = auto (use original FPS)
RESIZE_WIDTH = None  # None = auto (keep original)
RESIZE_HEIGHT = None  # None = auto (keep original)

# Features
DRAW_BOUNDING_BOXES = True
DRAW_CONFIDENCE_SCORES = True
DRAW_FRAME_COUNT = True

# Advanced
USE_GPU = True  # Use GPU if available
NUM_WORKERS = 4  # Number of processing workers
BATCH_SIZE = 1  # Batch size for processing
