# logic for counting
from ultralytics import YOLO
import cv2

# Load model once
model = YOLO("yolov8n.pt")

# Vehicle classes in COCO dataset
VEHICLE_CLASSES = [2, 3, 5, 7]


def count_vehicles(frame):
    results = model(frame)

    vehicle_count = 0

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])

            if cls in VEHICLE_CLASSES:
                vehicle_count += 1

    return vehicle_count


def get_density(count):
    if count < 5:
        return "LOW"
    elif count < 10:
        return "MEDIUM"
    else:
        return "HIGH"


def run_detection():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        count = count_vehicles(frame)
        density = get_density(count)

        cv2.putText(frame, f"Vehicles: {count}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.putText(frame, f"Density: {density}", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow("Traffic Analysis", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_detection()
   # Separates logic from main code
    #Reusable function