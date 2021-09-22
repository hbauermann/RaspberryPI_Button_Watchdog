import RPi.GPIO as gpio
import time 
import os

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

directory_mp3 = "/home/pi/"

def buttons(directory_mp3):
    while True:
        if gpio.input(23) == gpio.LOW:
            player(directory_mp3, "arara-azul.mp3", 6)
            break
        if gpio.input(24) == gpio.LOW:
            player(directory_mp3, "bugio.mp3", 9)
            break
        if gpio.input(25) == gpio.LOW:
            player(directory_mp3, "cabure.mp3", 5)
            break
        if gpio.input(26) == gpio.LOW:
            player(directory_mp3, "filomedusa.mp3", 6)
            break
        if gpio.input(19) == gpio.LOW:
            player(directory_mp3, "limpafolha.mp3", 6)
            break
        if gpio.input(12) == gpio.LOW:
            player(directory_mp3, "mutumalagoas.mp3", 5)
            break
        if gpio.input(16) == gpio.LOW:
            player(directory_mp3, "onca_pintada.mp3", 6)
            break
        if gpio.input(20) == gpio.LOW:
            player(directory_mp3, "papagaio.mp3", 5)
            break
        if gpio.input(21) == gpio.LOW:
            player(directory_mp3, "picapau.mp3", 4)
            break
        if gpio.input(13) == gpio.LOW:
            player(directory_mp3, "saira_pintor.mp3", 6)
            break
        if gpio.input(6) == gpio.LOW:
            player(directory_mp3, "tucanopreto.mp3", 7)
            break
        time.sleep(.25)

def player(directory_mp3, video, time_audio):
    os.system("omxplayer -o local " + directory_mp3 + video + " &")
    time.sleep(time_audio)
    buttons(directory_mp3)

if __name__ == '__main__':
    buttons(directory_mp3)
