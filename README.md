基于onnxruntime进行推理的YOLOv7 tiny的flask封装。

## Project Structure

```
├─📄README.md                       项目简介
├─📄.gitignore                      Git忽略项配置
├─🐳Dockerfile                      镜像构建脚本
├─🐍web_launcher.py                 服务启动脚本
├─🐍video_launcher.py               摄像头启动脚本
├─🐍__init__.py        
├─💼src                             代码包
│  ├─🐍configs.py                   配置项
│  ├─🐍__init__.py        
│  ├─💼views                        视图模块    
│  │  ├─🐍yolo_views.py             yolo视图
│  │  └─🐍__init__.py
│  └─💼infer                        推理模块
|     ├─🐍yolo_infer.py             yolo推理
|     ├─📄coco.names                类别标签
│     └─🐍__init__.py
└─📁models                          模型
   └─yolov7-tiny_256x320.onnx        yolo模型    
```

## Workflow

```mermaid
flowchart TB
    front[frontend] -->|rquest: \n img & desire| yolo[YOLOv7] -->|response: \n detect result| front
```

## Build Image

```
docker build -t zeng/yolo_detect . 
```

## Quick Start

POST an image encoded by Base64 to `localhost:9006/yolo_detect`

a base64-encoded image example:
```
data:image/jpeg;base64,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
```