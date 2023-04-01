#!/usr/bin/env python

from websocket import sockSVR
from data import Data
from standard import Standard
from nameless import Nameless
from tkinter import *

root = Tk()


class GameButton:
    def __init__(self, master):
        self.master = master
        # Set up screen
        root.config(cursor="none")
        #root.geometry("320x240")
        root.attributes('-fullscreen', True)
        root['bg'] = 'grey9'
        root.attributes("-topmost", True)

        self.display1 = Label(master, fg='white', bg='grey9', font=("Ariel", 24), wraplength=318)
        self.display1.place(relx=.5, rely=.5, anchor=S)
        self.display2 = Label(master, fg='white', bg='grey9', font=("Ariel", 35))
        self.display2.place(relx=.5, rely=.5, anchor=N)
        self.display1['text'] = 'Connect Phone'
        root.update()
        # Start Websocket
        #self.sockSVR()
        self.msg = '{"players":["Gordon", "Claire", "Steve", "Emma"], "time_limit": 3, "mode": "Standard", "dob": ["1989-08-31 00:00:00.000", "1991-07-24 00:00:00.000", "1991-07-03 00:00:00.000", "2023-03-18 00:00:00.000"]}'
        # sleep(3)
        # procoss Data
        self.data()
        # Run game
        self.pickMode()

        # t = Thread(target=sockSVR(self).start())
        # msg = sockSVR(self)

    def sockSVR(self):
        self.msg = sockSVR()

    def data(self):
        self.mode, self.time_limit, self.players, self.dob = Data(self.msg)

    def pickMode(self):
        if self.mode == "Standard":
            root.destroy()
            Standard(self.time_limit, self.players, master=None)
        if self.mode == "Nameless":
            root.destroy()
            Nameless(self.time_limit, master=None)


if __name__ == "__main__":
    app = GameButton(root)
    root.mainloop()
