import RPi.GPIO as gpio
import time 
import os

## PINS SETUP ##
gpio.setmode(gpio.BCM)
gpio.setup(23, gpio.IN, gpio.PUD_UP)
gpio.setup(24, gpio.IN, gpio.PUD_UP)
gpio.setup(25, gpio.IN, gpio.PUD_UP)
gpio.setup(26, gpio.IN, gpio.PUD_UP)
gpio.setup(19, gpio.IN, gpio.PUD_UP)
gpio.setup(12, gpio.IN, gpio.PUD_UP)
gpio.setup(16, gpio.IN, gpio.PUD_UP)
gpio.setup(20, gpio.IN, gpio.PUD_UP)
gpio.setup(21, gpio.IN, gpio.PUD_UP)
gpio.setup(13, gpio.IN, gpio.PUD_UP)
gpio.setup(6, gpio.IN, gpio.PUD_UP)


directory_mp3 = "mp3_directory/"
pin_directory = [
    {'pin': 23, 'file': 'arara-azul.mp3', 'audio_time': 6},
    {'pin': 24, 'file': 'bugio.mp3', 'audio_time': 9},
    {'pin': 25, 'file': 'cabure.mp3', 'audio_time': 5},
    {'pin': 26, 'file': 'filomedusa.mp3', 'audio_time': 6},
    {'pin': 19, 'file': 'limpafolha.mp3', 'audio_time': 6},
    {'pin': 12, 'file': 'mutumalagoas.mp3', 'audio_time': 5},
    {'pin': 16, 'file': 'onca_pintada.mp3', 'audio_time': 6},
    {'pin': 20, 'file': 'papagaio.mp3', 'audio_time': 5},
    {'pin': 21, 'file': 'picapau.mp3', 'audio_time': 4},
    {'pin': 13, 'file': 'saira_pintor.mp3', 'audio_time': 6},
    {'pin': 6, 'file': 'tucanopreto.mp3', 'audio_time': 7}
    ]


def buttons():
    while True:
        for a in range(pin_directory):
            if gpio.input(pin_directory[a]['pin']) == gpio.LOW:
                player(pin_directory[a]['file'], pin_directory[a]['audio_time'])
                break
        time.sleep(.25)


def player(video, time_audio, directory_mp3 = directory_mp3):
    os.system("omxplayer -o local " + directory_mp3 + video + " &")
    time.sleep(time_audio)
    buttons()


if __name__ == '__main__':
    buttons()
