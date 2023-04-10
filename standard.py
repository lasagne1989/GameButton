#!/usr/bin/env python

from time import sleep
from press import Button
import RPi.GPIO as GPIO
from random import randint
from itertools import cycle
from tkinter import *

root = Tk()

class Standard:
    def __init__(self, time_limit, players, master):
        self.master = master
        #set up screen
        root.config(cursor="none")
        #root.geometry("320x240")
        root.attributes('-fullscreen', True)
        root['bg'] = 'grey9'
        root.attributes("-topmost", True)
        #set up labels
        self.playing = Label(master, fg='white', bg='grey9', font=("Ariel", 32), wraplength=318)
        self.playing.place(relx=.5, rely=.5, anchor="s")
        self.timer = Label(master, fg='white', bg='grey9', font=("Ariel", 35), wraplength=318)
        self.timer.place(relx=.5, rely=.5, anchor="n")
        #initialise variables
        self.time_limit = time_limit
        self.time_text = DoubleVar()
        self.player_text = DoubleVar()
        self.player = None
        self.next_player = []
        self.time_limit = time_limit
        self.players = players
        #update screen
        #root.update()
        #select first player
        self.first_player()
        self.player = next(self.next_player)
        self.player_text.set(self.player)
        self.playing['textvariable'] = self.player_text
        self.playing['text'] = f"{self.player}, You Go First!"
        self.timer['text'] = "You Go First"
        reg_event = Button(GPIO.IN, GPIO.PUD_DOWN, GPIO.FALLING, self.countdown)
        reg_event.setup()
        reg_event.event()
        #self.countdown()

    def countdown(self):
        time_left = self.time_limit
        self.time_text.set(time_left)
        self.player = self.next_player[1]
        self.player_text.set(self.player)
        self.playing['textvariable'] = self.player_text
        print(self.player)
        while time_left != 0:
            # add button press to call restart()
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
        wait_event = Button(GPIO.IN, GPIO.PUD_DOWN, GPIO.FALLING, self.countdown())
        wait_event.wait()

    def first_player(self):
        player_cycle = []
        player_count = len(self.players)
        player_number = randint(0, player_count - 1)
        for i in range(player_count):
            player_cycle.append(self.players[player_number % player_count])
            player_number += 1
            self.next_player = cycle(player_cycle)



if __name__ == "__main__":
    app = Standard(time_limit, players, root)
    root.mainloop()
