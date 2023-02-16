import os

MY_PORT = 9006

MODEL_PATH = f'{os.getcwd()}/models/yolov7-tiny_256x320.onnx'
ANNOTATION = f'{os.getcwd()}/src/infer/coco.names'
CLASS_CONFIDENCE_THRESH = 0.3
NMS_IOU_THRESH = 0.5