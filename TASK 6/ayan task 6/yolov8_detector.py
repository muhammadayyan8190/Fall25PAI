import cv2
from ultralytics import YOLO
from collections import defaultdict

model = YOLO('yolov8n.pt')
def detect_objects_in_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    
    if not cap.isOpened():
        raise Exception("Cannot open video")
    
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if output_path:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    object_count = defaultdict(int)
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1
        results = model(frame)
        
        current_frame_objects = defaultdict(int)
        for result in results:
            for box in result.boxes:
                cls_id = int(box.cls[0])
                class_name = result.names[cls_id]
                current_frame_objects[class_name] += 1
                
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = float(box.conf[0])
                
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f"{class_name} {confidence:.2f}"
                cv2.putText(frame, label, (x1, y1 - 10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.putText(frame, f"Frame: {frame_count}/{total_frames}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        for obj_type, count in current_frame_objects.items():
            if object_count[obj_type] == 0 or count > object_count[obj_type]:
                object_count[obj_type] = count
        
        if output_path:
            out.write(frame)
    
    cap.release()
    if output_path:
        out.release()
    
    return dict(object_count)
