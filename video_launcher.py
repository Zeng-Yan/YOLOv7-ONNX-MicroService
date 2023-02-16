import cv2
from src.infer.yolo_infer import YOLOv7
import src.configs as cfg

DETECT_FPS = 10


def detect_on_frame(array_img):
    try:
        yolov7_detector = YOLOv7(cfg.MODEL_PATH, conf_thres=cfg.CLASS_CONFIDENCE_THRESH, iou_thres=cfg.NMS_IOU_THRESH)  # Initialize YOLOv7 object detector
        boxes, scores, class_ids = yolov7_detector.detect(array_img)  # Detect Objects
        dstimg = yolov7_detector.draw_detections(array_img, boxes, scores, class_ids)  # Draw detections
    except Exception as e:
        print(e)
        dstimg = array_img
    return dstimg


def videocapture():
    cap=cv2.VideoCapture(0)     #生成读取摄像头对象
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  #获取视频的宽度
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  #获取视频的高度
    cap_fps = cap.get(cv2.CAP_PROP_FPS) #获取视频的帧率
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))    #视频的编码
    
    # writer = cv2.VideoWriter("video_result.mp4", fourcc, DETECT_FPS, (width, height))  #定义视频对象输出
    while cap.isOpened():
        if cap_fps % DETECT_FPS != 0:
            break
        if cv2.waitKey(24) == ord('q'):  # 按Q退出
            break

        ret, frame = cap.read() #读取摄像头画面
        frame = detect_on_frame(frame)  # 处理帧
        cv2.imshow('video', frame) #显示画面
        # writer.write(frame)  #视频保存
        
    cap.release()         #释放摄像头
    cv2.destroyAllWindows() #释放所有显示图像窗口
 

if __name__ == '__main__' :
 
    videocapture()