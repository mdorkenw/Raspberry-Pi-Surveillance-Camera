# Raspberry-Pi-Surveillance-Camera


## Getting Started

### Raspberry Pi Set up
Here a great [step by step guide](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up) for setting up the raspberry pi and [here](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera) for the camera. 

### SSH 
As a next step, the Raspberry pi is accsed remotely via secure shell [guide](https://www.raspberrypi.org/documentation/remote-access/ssh/). I also recommend setting up ssh keys for that [this](https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md) might be useful. Please use ssh-keygen -f specification for changing the default name. After that add these two lines to your .bashrc for making life easier:
```bash
alias mountpi='sshfs pi@192.168.1.X:/home/pi/ PI/'

alias spi='ssh pi@192.168.1.X'
```
### Install Packages (Python, Opencv and Picamera)
Next, python, opencv and picamera are installed by following this [guide](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/).

### Telegram bot
To set up the telegram bot we have to create bot from [botfather](https://telegram.me/botfather). For writing your first bot this [guide](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot) may be useful.

### Setting up Telegram Bot
https://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/
https://ginolhac.github.io/posts/diy-raspberry-monitored-via-telegram/#materials


