from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
labels = [1, 16, 17]

print('Loading Model ...')
model = cv2.dnn.readNetFromTensorflow(
        'detection/frozen_inference_graph.pb',
        'detection/ssd_mobilenet.pbtxt')


rawCapture = PiRGBArray(camera, size=(640, 480))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    
    image = frame.array
    (h, w) = image.shape[:2]

    model.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True, crop=False))
    pred = model.forward()[0, 0, labels]

    thres = False
    for conf in pred[:, 2]:
        if conf > 0.3:
            thres = True

    if thres:
        for detection in pred:
            score = float(detection[2])
            if score > 0.3:
                bbox = detection[3:7]
                x = bbox[1] * h
                y = bbox[0] * w
                right = bbox[3] * h
                bottom = bbox[2] * w
                cv2.rectangle(image, (int(x), int(y)), (int(right), int(bottom)), (125, 255, 51), thickness=2)

    cv2.imwrite('/home/pi/Pictures/image.jpg', image)
    exit()