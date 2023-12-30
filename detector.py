from ultralytics import *
import cv2


# Pegando o arquivo
model_path = r"runs/detect/train/weights/last.pt"
model = YOLO(model_path)

# Source 0 pra usar a webcam
results = model.predict(source='0',show=True)

print(results)