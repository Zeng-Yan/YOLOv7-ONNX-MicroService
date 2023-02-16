FROM python:3.10.0-slim
RUN pip install opencv-python-headless -i https://pypi.tuna.tsinghua.edu.cn/simple \
    # pip install opencv-contrib-python -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install onnxruntime -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install flask gevent -i https://pypi.tuna.tsinghua.edu.cn/simple 
EXPOSE 9006
COPY src /home/zeng/src/
COPY models /home/zeng/models/
COPY web_launcher.py /home/zeng/web_launcher.py
WORKDIR /home/zeng
CMD python3 web_launcher.py
