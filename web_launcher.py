from flask import Flask

from src.configs import MY_PORT

# 初始化
app = Flask(__name__)


if __name__ == '__main__':
    from gevent import pywsgi

    with app.app_context():
        from src.views import yolo_views
        
        app.run(host='0.0.0.0', port=MY_PORT, debug=True)
        # server = pywsgi.WSGIServer(('0.0.0.0', MY_PORT), app)
        # server.serve_forever()

# http://192.168.1.221:9980/zengyan/yolo_detect.git
