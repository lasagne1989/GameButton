#!/usr/bin/env python
from websocket import sockSVR
from data import Data
from tkinter import *

#fixes:
#"you got first" name incorrect
#button not stopping loop, needs to be called in the loop?

root = Tk()


class GameButton:
    def __init__(self, master):
        self.master = master
        # Set up screen
        root.config(cursor="none")
        root.geometry("320x240")
        #root.attributes('-fullscreen', True)
        root['bg'] = 'grey9'
        root.attributes("-topmost", True)

        # Set up label
        self.display1 = Label(master, fg='white', bg='grey9', font=("Ariel", 35), wraplength=318)
        self.display1.place(relx=.5, rely=.5, anchor="center")
        self.display1['text'] = 'Connect Phone'
        # Update screen
        root.update()
        # Initiate variables
        self.msg = None
        self.dob = None
        self.players = None
        self.time_limit = None
        self.mode = None
        # Start Websocket
        self.sockSVR()
        #self.msg = '{"players":["Gordon", "Claire", "Steve", "Emma"], "time_limit": 3, "mode": "Chess","dob": ["1989-08-31 00:00:00.000", "1991-07-24 00:00:00.000", "1991-07-03 00:00:00.000", "2023-03-1800:00:00.000"]}'
        #Process data
        self.data()
        # Run game
        self.pickMode()

    def sockSVR(self):
        self.msg = sockSVR()

    def data(self):
        self.mode, self.time_limit, self.players, self.dob = Data(self.msg)

    def pickMode(self):
        if self.mode == "Standard":
            root.destroy()
            from standard import start_standard
            start_standard(self.time_limit, self.players)
        if self.mode == "Nameless":
            root.destroy()
            from nameless import start_nameless
            start_nameless(self.time_limit)
        if self.mode == "Chess":
            root.destroy()
            from chess import start_chess
            start_chess(self.time_limit, self.players)


if __name__ == "__main__":
    app = GameButton(root)
    root.mainloop()
