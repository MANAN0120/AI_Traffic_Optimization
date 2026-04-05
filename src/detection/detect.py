#runs detection
from ultralytics import YOLO
import cv2

from vehicle_counter import count_vehicles, classify_density
from config import VEHICLE_CLASSES, LOW_THRESHOLD, MEDIUM_THRESHOLD

# Load model
model = YOLO("yolov8n.pt")

# Video input
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    # Count vehicles
    vehicle_count = count_vehicles(results, VEHICLE_CLASSES)

    # Classify density
    density = classify_density(vehicle_count, LOW_THRESHOLD, MEDIUM_THRESHOLD)

    # Draw boxes
    annotated_frame = results[0].plot()

    # Display info
    cv2.putText(annotated_frame, f"Count: {vehicle_count}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.putText(annotated_frame, f"Density: {density}",
                (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Detection System", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
