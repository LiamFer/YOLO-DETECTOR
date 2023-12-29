import os
from ultralytics import YOLO
import cv2

VIDEOS_DIR = os.path.abspath("C:\\Users\\Pichau\\Documents\\studies\\YOLO-DETECTOR")

video_path = os.path.join(VIDEOS_DIR, 'videos', 'construction.mp4')
video_path_out = '{}_out.mp4'.format(video_path)

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open the video.")
else:
    ret, frame = cap.read()
    H, W, _ = frame.shape  # Correct indentation

out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

model_path = os.path.abspath("C:\\Users\\Pichau\\Documents\\studies\\YOLO-DETECTOR\\runs\\detect\\train4\\weights\\last.pt")
print(model_path)

# Load a model
try:
    model = YOLO(model_path)  # load a custom model
except Exception as e:
    print(f"Error loading the YOLO model: {e}")

threshold = 0.5

while ret:
    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    out.write(frame)
    ret, frame = cap.read()

cap.release()
out.release()
cv2.destroyAllWindows()