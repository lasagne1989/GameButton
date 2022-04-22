import press
import random
import itertools
from tkinter import *
import RPi.GPIO as GPIO

root = Tk()


class Timer:
    def __init__(self, master):
        self.master = master
        root.geometry("320x240")
        self.display1 = Label(master, font=("Arial", 25))
        self.display1.place(relx=.5, rely=.5, anchor=S)
        self.display2 = Label(master, font=("Arial", 25))
        self.display2.place(relx=.5, rely=.5, anchor=N)
        # self.display = Label(master, font=("Arial", 25))
        # self.display.place(relx=.5, rely=.5, anchor=CENTER)
        self.display1['text'] = 'Game On!'
        reg_event = press.Button(GPIO.IN, GPIO.PUD_DOWN, GPIO.FALLING, self.start)
        reg_event.setup()
        reg_event.event()
        self.timeit = False
        self.press_count = 0
        people = ['Gordon', 'Claire', 'Emma', 'Steve']
        playerCount = len(people)
        playerNum = random.randint(0, playerCount - 1)
        player_cycle = []
        for i in range(playerCount):
            player_cycle.append(people[playerNum % playerCount])
            playerNum += 1
        self.next_players = itertools.cycle(player_cycle)

    def start(self, channel):
        if self.press_count == 0:
            self.player = next(self.next_players)
            self.display1['text'] = self.player + ", You Go First!"
            # self.display2['text'] = "You Go First!"
            self.press_count += 1
            print(self.press_count)
        elif self.press_count == 1:
            self.timer_text = DoubleVar()
            self.timer_text.set(5 + 1)
            self.display1['text'] = self.player
            self.display2['textvariable'] = self.timer_text
            self.increment_timer()
            self.press_count += 1
            print(self.press_count)
        else:
            self.player = next(self.next_players)
            self.timer_text = DoubleVar()
            self.timer_text.set(5 + 1)
            self.display1['text'] = self.player
            self.display2['textvariable'] = self.timer_text
            # self.increment_timer()
            self.press_count += 1
            print(self.press_count)

    def increment_timer(self):
        ctr = int(self.timer_text.get())
        if ctr > 0:
            self.timer_text.set(ctr - 1)
            self.master.update()
            self.master.after(1000, self.increment_timer)
        else:
            self.display1['text'] = self.player + ', You Fucked It!'
            root.update()
            wait_event = press.Button(GPIO.IN, GPIO.PUD_DOWN, GPIO.FALLING, self.start)
            #wait_event.setup()
            wait_event.wait()
            self.player = next(self.next_players)
            self.press_count = 1
            print(self.press_count)
            # self.start(10)


app = Timer(root)
root.mainloop()
