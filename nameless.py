#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO
from tkinter import *

root = Tk()


def pin_setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


class Nameless:
    def __init__(self, time_limit, master):
        self.master = master
        # Set up screen
        root.config(cursor="none")
        #root.geometry("320x240")
        root.attributes('-fullscreen', True)
        root['bg'] = 'grey9'
        root.attributes("-topmost", True)

        self.timer = Label(master, fg='white', bg='grey9', font=("Ariel", 38), wraplength=318)
        self.timer.place(relx=.5, rely=.5, anchor="center")
        self.timer['text'] = "Press the Button to Start"
        self.time_limit = time_limit
        self.time_text = DoubleVar()
        root.update()
        # set up buttons
        GPIO.add_event_detect(10, GPIO.FALLING, bouncetime=500)
        GPIO.wait_for_edge(12, GPIO.FALLING, bouncetime=500)
        self.countdown(10)

    def countdown(self, channel):
        time_left = self.time_limit
        self.time_text.set(time_left)
        while time_left != 0:

            if GPIO.event_detected(10):
                print("beep")
                self.countdown(10)
            self.timer['textvariable'] = self.time_text
            root.update()
            time_left -= 1
            self.time_text.set(time_left)
            print(time_left)
            sleep(1)
        self.time_text.set("You Dumb Bitch!!!")
        self.timer['textvariable'] = self.time_text
        root.update()
        print("You Dumb Bitch")
        self.restart()

    def restart(self):
        GPIO.wait_for_edge(12, GPIO.FALLING, bouncetime=500)
        sleep(1)
        self.countdown(10)


def start_nameless(time_limit):
    pin_setup()
    app = Nameless(time_limit, master=None)
    root.mainloop()


if __name__ == '__main__':
    start_nameless(time_limit)
