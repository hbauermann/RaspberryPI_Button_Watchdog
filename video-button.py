import RPi.GPIO as gpio
import time 
import os

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN, gpio.PUD_DOWN)
gpio.setup(27, gpio.IN, gpio.PUD_DOWN)
gpio.setup(22, gpio.IN, gpio.PUD_DOWN)
gpio.setup(23, gpio.IN, gpio.PUD_DOWN)


directory = "/home/pi/"


def button():
    while True:
        if gpio.input(17) == gpio.HIGH:
            player("/Videos/FINAL/CARNE LEGENDA.mp4", 65)
            break
        if gpio.input(27) == gpio.HIGH:
            player("/Videos/FINAL/CELULAR LEGENDA.mp4", 77)
            break
        if gpio.input(22) == gpio.HIGH:
            player("/Videos/FINAL/PAPEL LEGENDA.mp4", 66)
            break
        if gpio.input(23) == gpio.HIGH:
            player("/Videos/FINAL/PLASTICO LEGENDA.mp4", 73)
            break
        time.sleep(.25)


def player(video, tempo):
    global directory
    os.system("omxplayer " + directory + video + " &")
    time.sleep(tempo)
    button()


os.system("unclutter -display :0.0 -idle 2 &")
os.system("xdotool mousemove_relative --polar 0 1000 &")
button()
