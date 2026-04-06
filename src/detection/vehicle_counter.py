from ultralytics import YOLO
import cv2

# RL model import
from src.rl_model.use_model import get_signal_from_rl

# Load YOLO model
model = YOLO("yolov8n.pt")

# Vehicle classes (COCO dataset)
VEHICLE_CLASSES = [2, 3, 5, 7]  # car, motorbike, bus, truck


def count_vehicles(frame):
    results = model(frame)

    vehicle_count = 0

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])

            if cls in VEHICLE_CLASSES:
                vehicle_count += 1

    return vehicle_count


def count_vehicles_per_lane(frame):
    height, width, _ = frame.shape

    # Split frame into 3 lanes
    lane1 = frame[:, :width // 3]
    lane2 = frame[:, width // 3: 2 * width // 3]
    lane3 = frame[:, 2 * width // 3:]

    lane_counts = [
        count_vehicles(lane1),
        count_vehicles(lane2),
        count_vehicles(lane3)
    ]

    return lane_counts


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

        # Multi-lane counting
        lane_counts = count_vehicles_per_lane(frame)
        total_count = sum(lane_counts)

        # Density
        density = get_density(total_count)

        # RL-based signal decision
        signal = get_signal_from_rl(total_count)

        # ---------------- DISPLAY ----------------

        # Total vehicles
        cv2.putText(frame, f"Total Vehicles: {total_count}",
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2)

        # Density
        cv2.putText(frame, f"Density: {density}",
                    (20, 80), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2)

        # Signal
        cv2.putText(frame, f"Signal: {signal['action']}",
                    (20, 120), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

        # Time
        cv2.putText(frame, f"Green Time: {signal['duration']} sec",
                    (20, 160), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

        # Lane counts
        cv2.putText(frame, f"Lane1: {lane_counts[0]}",
                    (20, 200), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (255, 255, 0), 2)

        cv2.putText(frame, f"Lane2: {lane_counts[1]}",
                    (20, 230), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (255, 255, 0), 2)

        cv2.putText(frame, f"Lane3: {lane_counts[2]}",
                    (20, 260), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (255, 255, 0), 2)

        # Draw lane separators
        height, width, _ = frame.shape
        cv2.line(frame, (width // 3, 0), (width // 3, height), (255, 255, 255), 2)
        cv2.line(frame, (2 * width // 3, 0), (2 * width // 3, height), (255, 255, 255), 2)

        # Show output
        cv2.imshow("AI Traffic System (Multi-Lane + RL)", frame)

        # Exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_detection()