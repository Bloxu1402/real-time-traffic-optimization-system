import cv2
from ultralytics import YOLO

# Load a pre-trained, lightweight YOLOv8 model (automatically downloads on first run)
model = YOLO('yolov8n.pt') 

# Open video stream (Use 0 for webcam, or a path to a traffic video file like 'traffic.mp4')
cap = cv2.VideoCapture(0)

# Define a Region of Interest (ROI) polygon coordinates [x, y] to monitor a specific lane
# Adjust these coordinates to fit your specific video feed frame
roi_points = [(100, 400), (500, 400), (600, 700), (50, 700)]

def is_inside_roi(x, y, roi):
    # Quick geometric check to see if vehicle center is inside our target lane box
    return cv2.pointPolygonTest(roi, (x, y), False) >= 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO object tracking on the frame
    results = model(frame, verbose=False)[0]
    
    vehicle_count = 0
    
    # Draw the ROI tracking zone on the screen (Blue Box)
    import numpy as np
    cv2.polylines(frame, [np.array(roi_points, np.int32)], True, (255, 0, 0), 3)

    for box in results.boxes:
        # Get coordinates of detected object
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        class_id = int(box.cls[0])
        
        # Class IDs for vehicles in COCO dataset: 2=car, 3=motorcycle, 5=bus, 7=truck
        if class_id in [2, 3, 5, 7]:
            # Find the center point of the vehicle
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            
            # Check if the vehicle is inside our lane zone
            if is_inside_roi(cx, cy, np.array(roi_points, np.int32)):
                vehicle_count += 1
                # Draw green box around tracked vehicles
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    # Save the current count to a temporary local text file (Inter-process communication)
    with open("live_traffic_data.txt", "w") as f:
        f.write(str(vehicle_count))

    # Display the live feed
    cv2.putText(frame, f"Vehicles in Lane: {vehicle_count}", (50, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Smart Traffic Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
