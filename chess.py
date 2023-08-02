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


class Chess:
    def __init__(self, time_limit, players, master):
        self.master = master

        root.config(cursor="none")
        #root.geometry("320x240")
        root.attributes('-fullscreen', True)
        root['bg'] = 'grey9'
        root.attributes("-topmost", True)

        self.playing = Label(master, fg='white', bg='grey9', font=("Ariel", 32), wraplength=318)
        self.playing.place(relx=.5, rely=.5, anchor="s")
        self.timer = Label(master, fg='white', bg='grey9', font=("Ariel", 35), wraplength=318)
        self.timer.place(relx=.5, rely=.5, anchor="n")
        self.time_limit = time_limit
        self.time_left = None
        self.time_text = DoubleVar()
        self.player_text = DoubleVar()
        self.player = None
        self.next_player = []
        self.time_limit = time_limit
        self.players = players
        self.dict = {}
        root.update()
        self.dictionary()
        self.first_player()
        GPIO.add_event_detect(10, GPIO.FALLING, bouncetime=500)
        GPIO.wait_for_edge(12, GPIO.FALLING, bouncetime=500)
        self.countdown(10)

    def dictionary(self):
        for p in self.players:
            self.dict.update({p: self.time_limit})

    def countdown(self, channel):
        self.player = next(self.next_player)

        self.time_left: int = self.dict[self.player]
        self.time_text.set(self.time_left)

        self.player_text.set(self.player)
        self.playing['textvariable'] = self.player_text
        print(self.player)
        while self.time_left != 0:
            if GPIO.event_detected(10):
                print("beep")
                self.countdown(10)
            self.timer['textvariable'] = self.time_text
            root.update()
            self.time_left -= 1
            self.time_text.set(self.time_left)
            print(self.time_left)
            sleep(1)
        self.time_text.set("You Dumb Bitch!!!")
        self.timer['textvariable'] = self.time_text
        root.update()
        print("You Dumb Bitch")
        self.restart()

    def restart(self):
        GPIO.wait_for_edge(12, GPIO.FALLING, bouncetime=500)
        self.dict[self.player] = self.time_left
        # add await button press
        sleep(1)
        self.countdown(10)

    def first_player(self):
        player_cycle = []
        player_count = len(self.players)
        player_number = randint(0, player_count - 1)
        for i in range(player_count):
            player_cycle.append(self.players[player_number % player_count])
            player_number += 1
            self.next_player = cycle(player_cycle)


def start_chess(time_limit, players):
    pin_setup()
    app = Chess(time_limit, players, master=None)
    root.mainloop()


if __name__ == '__main__':
    start_chess(time_limit, players)
