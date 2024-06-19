# import base64
# import cv2 
# import numpy as np
# import matplotlib.pyplot as plt


# def img_bs64_to_ndarray(bs64_img):
#     if len(bs64_img) % 3 == 1:
#         bs64_img += '=='
#     elif len(bs64_img) % 3 == 2:
#         bs64_img += '='
    
#     bytes_img = base64.b64decode(bs64_img)
#     array_img = np.frombuffer(bytes_img, np.uint8)
#     array_img = cv2.imdecode(array_img, cv2.IMREAD_COLOR)

#     return array_img

# bs64_img = 'data:image/jpeg;base64,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'
# bs64_img = bs64_img.split(',')[1]
# img = img_bs64_to_ndarray(bs64_img)
# plt.imshow(img)
# plt.show()
# print(len(bs64_img))





# import cv2

# import numpy as np

# face_cascade = cv2.CascadeClassifier('D:/Softwares/anaconda/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
#         cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break