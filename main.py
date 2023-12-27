from ultralytics import YOLO



model = YOLO("yolov8l.yaml")  # build a new model from scratch


model.train(data="config.yaml", epochs=15)  # train the model