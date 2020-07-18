from picamera import PiCamera
from time import sleep

camera = PiCamera()

#camera.resolution = (2592, 1944)
camera.vflip = True

camera.sharpness = 0 

camera.start_preview()

sleep(1000)
#camera.capture('/home/pi/Desktop/image.jpg')


#camera.start_recording('/home/pi/Desktop/video.h264')
#sleep(180)
#camera.stop_recording()

camera.stop_preview()
