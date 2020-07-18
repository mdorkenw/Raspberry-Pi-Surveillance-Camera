from picamera import PiCamera
import time, cv2, glob, os

from telegram.ext import Updater
updater = Updater(token='', use_context=True)
dispatcher = updater.dispatcher
bot = CallbackContext(dispatcher)
chat_id = 

camera = PiCamera()
camera.resolution = (1280, 720)
camera.framerate = 32

rawCapture = picamera.array.PiRGBArray(camera)
old_image = 0
counter = len(glob.glob('/home/pi/Pictures/detect/*.jpg'))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    
    image = frame.array 
    diff = np.mean(np.abs(image- old_image))
    print(diff)
    
    if diff > 120:
        cv2.imwrite(f'/home/pi/Pictures/detect/image{counter}.jpg')
        bot.send_photo(chat_id, photo=open('', 'rb'))
        bot.send_message(chat_id, 'Bewegung detected')
        camera.start_recording(f'/home/pi/Videos/vid{counter}.h264')
        time.sleep(10)
        camera.stop_recording()   
        counter += 1
    exit()