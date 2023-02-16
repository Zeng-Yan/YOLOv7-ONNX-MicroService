import cv2
import base64
import json
import numpy as np
from flask import request, jsonify
from flask import current_app as app

from src.infer.yolo_infer import YOLOv7
import src.configs as cfg


@app.route(f'/yolo_detect', methods=['GET', 'POST'])
def yolo_detect():
    """
    """
    response = {'status': 202, 'result': None, 'info': None}

    if request.method not in ['GET', 'POST']:
        response['info'] = '[ERROR] wrong http meathod.'
        return jsonify(response)
    
    
    # data = request.get_data()
    # data = json.loads(data)
    # bs64_img = data['img'].split(',')[1]

    bs64_img: str = request.values.get('img').split(',')[1].replace(' ', '')
    desire = request.values.get('desire')

    if request.method == 'GET' and bs64_img.find('/') != -1:
        response['info'] = '[ERROR] Not a urlsafe base64 encoding for using http GET method.'
        return response
    
    bytes_img = base64.urlsafe_b64decode(bs64_img)
    array_img = np.frombuffer(bytes_img, np.uint8)
    array_img = cv2.imdecode(array_img, cv2.IMREAD_COLOR)
    
    try:
        yolov7_detector = YOLOv7(cfg.MODEL_PATH, conf_thres=cfg.CLASS_CONFIDENCE_THRESH, iou_thres=cfg.NMS_IOU_THRESH)  # Initialize YOLOv7 object detector
        boxes, scores, class_ids = yolov7_detector.detect(array_img)  # Detect Objects
        dstimg = yolov7_detector.draw_detections(array_img, boxes, scores, class_ids)  # Draw detections

        _, output_img = cv2.imencode('.jpg', dstimg)
        bytes_img = output_img.tobytes()
        bs64_img = base64.b64encode(bytes_img).decode('utf8')
    except Exception as e:
        print(e)
    else:
        response['result'] = bs64_img
        response['status'] = 200
    
    if desire == 'bs64':
        return jsonify(response)
    else:
        html_src = f'<img src="data:image/jpg;base64, {bs64_img}"/>'
        return html_src
