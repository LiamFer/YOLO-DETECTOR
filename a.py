import os

from ultralytics import YOLO
import cv2


VIDEOS_DIR = os.path.join('.', 'videos')

print(os.listdir(VIDEOS_DIR))
