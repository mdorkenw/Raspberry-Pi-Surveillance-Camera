from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.vflip = True

camera.start_preview()
camera.exposure_mode = 'nightpreview'

sleep(1000)

# camera.capture('/home/pi/Desktop/image.jpg')

#camera.start_recording('/home/pi/Desktop/video.h264')
#sleep(180)
#camera.stop_recording()

camera.stop_preview()
