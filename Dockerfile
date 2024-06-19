FROM python:3.10-slim
COPY src /home/zeng/src/
COPY models /home/zeng/models/
COPY web_launcher.py /home/zeng/web_launcher.py
EXPOSE 9006
WORKDIR /home/zeng
RUN rm -rf src/__pycache__ \
    && pip install opencv-python-headless -i https://pypi.tuna.tsinghua.edu.cn/simple \
    # pip install opencv-contrib-python -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install onnxruntime -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install flask gevent -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && rm -r ~/.cache/pip
CMD python3 web_launcher.py
