#!/usr/bin/env python

from time import sleep
from tkinter import *

root = Tk()


class Nameless:
    def __init__(self, time_limit, master):
        self.master = master
        # Set up screen
        root.config(cursor="none")
        root.geometry("320x240")
        #root.attributes('-fullscreen', True)
        root['bg'] = 'grey9'
        root.attributes("-topmost", True)

        self.timer = Label(master, fg='white', bg='grey9', font=("Ariel", 38), wraplength=318)
        self.timer.place(relx=.5, rely=.5, anchor="center")
        self.time_limit = time_limit
        self.time_text = DoubleVar()
        root.update()
        self.countdown()

    def countdown(self):
        time_left = self.time_limit
        self.time_text.set(time_left)
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
        # add await button press
        sleep(1)
        self.countdown()

if __name__ == "__main__":
    app = Nameless(time_limit, root)
    root.mainloop()