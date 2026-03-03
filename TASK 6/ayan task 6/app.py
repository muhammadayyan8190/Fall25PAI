from flask import Flask, render_template, request, jsonify, Response
import cv2
import os
from werkzeug.utils import secure_filename
import numpy as np
from yolov8_detector import detect_objects_in_video

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'static/outputs'
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv', 'flv', 'wmv'}
processing_status = {'status': 'idle', 'progress': 0}
# frame_queue and object_counts no longer needed for asynchronous streaming

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    return jsonify(processing_status)

# streaming endpoint is no longer used after simplifying workflow

@app.route('/objects')
def get_objects():
    # for backwards compatibility, report empty or last processed data
    return jsonify({})

@app.route('/upload', methods=['POST'])
def upload_video():
    global processing_status, object_counts
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file format'}), 400
        
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)
        
        processing_status = {'status': 'processing', 'progress': 0}
        
        output_filename = f"detected_{filename}"
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
        
        try:
            # perform detection synchronously and return counts
            counts = detect_objects_in_video(input_path, output_path)
            processing_status = {'status': 'complete', 'progress': 100}
        except Exception as e:
            processing_status = {'status': 'error', 'progress': 0}
            return jsonify({'error': str(e)}), 500
        
        return jsonify({
            'success': True,
            'message': 'Processing complete',
            'video': f'/static/outputs/{output_filename}',
            'original_file': filename,
            'objects': counts
        })
    
    except Exception as e:
        processing_status = {'status': 'error', 'progress': 0}
        return jsonify({'error': str(e)}), 500


@app.errorhandler(404)
def not_found(e):
    return render_template('index.html')

if __name__ == '__main__':
    print('\n' + '='*60)
    print('  🎬 Object Counter - Web Server')
    print('='*60)
    print('\n  🌐 http://localhost:5000')
    print('  📹 Upload video to count objects!\n')
    app.run(debug=True, host='0.0.0.0', port=5000)
