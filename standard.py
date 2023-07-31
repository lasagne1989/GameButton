#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO
from random import randint
from itertools import cycle
from tkinter import *

root = Tk()


def pin_setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


class Standard:
    def __init__(self, time_limit, players, master):
        self.master = master
        # set up screen
        root.config(cursor="none")
        root.geometry("320x240")
        #root.attributes('-fullscreen', True)
        root['bg'] = 'grey9'
        root.attributes("-topmost", True)
        # set up labels
        self.playing = Label(master, fg='white', bg='grey9', font=("Ariel", 32), wraplength=318)
        self.playing.place(relx=.5, rely=.5, anchor="s")
        self.timer = Label(master, fg='white', bg='grey9', font=("Ariel", 35), wraplength=318)
        self.timer.place(relx=.5, rely=.5, anchor="n")
        # initialise variables
        self.time_limit = time_limit
        self.time_text = DoubleVar()
        self.player_text = DoubleVar()
        self.player = None
        self.player_cycle = []
        self.next_player = []
        self.time_limit = time_limit
        self.players = players
        # select first player
        self.first_player()
        self.player = self.player_cycle[1]
        self.player_text.set(self.player)
        self.playing['textvariable'] = self.player_text
        self.playing['text'] = self.player
        self.timer['text'] = "You Go First"
        # set up buttons
        GPIO.add_event_detect(10, GPIO.FALLING, bouncetime=500)
        GPIO.wait_for_edge(12, GPIO.FALLING, bouncetime=500)
        self.countdown(10)


    def countdown(self, channel):
        time_left = self.time_limit
        self.time_text.set(time_left)
        self.player = next(self.next_player)
        self.player_text.set(self.player)
        self.playing['textvariable'] = self.player_text
        print(self.player)
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
        self.time_text.set('You Dumb Bitch!!!')
        self.timer['textvariable'] = self.time_text
        root.update()
        print("You Dumb Bitch")
        self.restart()

    def restart(self):
        GPIO.wait_for_edge(12, GPIO.FALLING, bouncetime=500)
        self.countdown(10)

    def first_player(self):
        self.player_cycle = []
        player_count = len(self.players)
        player_number = randint(0, player_count - 1)
        for i in range(player_count):
            self.player_cycle.append(self.players[player_number % player_count])
            player_number += 1
            self.next_player = cycle(self.player_cycle)


def start_standard(time_limit, players):
    pin_setup()
    app = Standard(time_limit, players, master=None)
    root.mainloop()


if __name__ == '__main__':
    start_standard(time_limit, players)
