from ultralytics import YOLO

# Carregar o modelo
model = YOLO("yolov8n.yaml")
# Treinar
model.train(data="config.yaml", epochs=100) 
