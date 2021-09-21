import RPi.GPIO as gpio
import time, os

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN, gpio.PUD_DOWN)
gpio.setup(27, gpio.IN, gpio.PUD_DOWN)
gpio.setup(22, gpio.IN, gpio.PUD_DOWN)
gpio.setup(23, gpio.IN, gpio.PUD_DOWN)


directory_video = "video/"
pin_directory = [
    {'pin': 17, 'file': 'video_1.mp4', 'video_time': 65},
    {'pin': 27, 'file': 'video_2.mp4', 'video_time': 77},
    {'pin': 22, 'file': 'video_3.mp3', 'video_time': 66},
    {'pin': 23, 'file': 'video_4.mp3', 'video_time': 73}
    ]

def button():
    while True:
        for a in range(pin_directory):
            if gpio.input(pin_directory[a]['pin']) == gpio.LOW:
                player(pin_directory[a]['file'], pin_directory[a]['video_time'])
                break
        time.sleep(.25)



def player(video, video_time, directory_video = directory_video):
    global directory
    os.system("omxplayer " + directory_video + video + " &")
    time.sleep(video_time)
    button()



if __name__ == '__main__':
    os.system("unclutter -display :0.0 -idle 2 &") ## do not enter iddle mode
    os.system("xdotool mousemove_relative --polar 0 1000 &") ## move mouse to hide place
    button()
