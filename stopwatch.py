import press
import firstplayer
from tkinter import *
import RPi.GPIO as GPIO

root = Tk()


class Timer:
    def __init__(self, master):
        self.master = master
        root.geometry("320x240")
        self.display = Label(master, text="We're going to play a little game", font=("Arial", 25))
        self.display.place(relx=.5, rely=.5, anchor=CENTER)
        reg_event = press.Button(GPIO.IN, GPIO.PUD_DOWN, GPIO.FALLING, self.start)
        reg_event.setup()
        reg_event.event()
        self.timeit = False
        self.started = False
        self.firstrun=True
        self.people = ['Gordon', 'Claire', 'Emma', 'Steve']
        self.playerCount = len(self.people)

    def players(self):
        if not self.started:
            pick = firstplayer.playerPicker(self.people, 0)
            self.playerNum = pick.firstPlayer()
            self.player = self.people[self.playerNum]
        else:
            pick = firstplayer.playerPicker(self.people, self.playerNum)
            self.playerNum = pick.nextPlayer()
            self.player = self.people[self.playerNum]

    def start(self, channel):
        if not self.started:
            self.display.destroy()
            self.players()
            self.display1 = Label(self.master, text=(self.player + ', You Go First!'), font=("Arial", 25))
            self.display1.place(relx=.5, rely=.5, anchor=CENTER)
            self.started = not self.started
        else:
            if self.firstrun:
                self.timeit = not self.timeit
                self.display1.destroy()
                self.timertext = DoubleVar()
                self.timertext.set(5 + 1)
                self.display2 = Label(root, text=self.player, font=("Arial", 25))
                self.display2.place(relx=.5, rely=.5, anchor=S)
                self.display3 = Label(root, textvariable=self.timertext, font=("Arial", 25))
                self.display3.place(relx=.5, rely=.5, anchor=N)
                self.firstrun = not self.firstrun
                self.increment_timer()
            else:
                self.timertext = DoubleVar()
                self.timertext.set(5 + 1)


    def increment_timer(self):
        ctr = int(self.timertext.get())
        if ctr > 0:
            self.timertext.set(ctr - 1)
            self.master.update()
            self.master.after(1000, self.increment_timer)
        else:
            self.display2.destroy()
            self.display3.destroy()
            self.display4 = Label(root, text=self.player + ", You Fucked It!", font=("Arial", 25))
            self.display4.place(relx=.5, rely=.5, anchor=N)
            self.master.update()
            wait_event = press.Button(GPIO.IN, GPIO.PUD_DOWN, GPIO.FALLING, 0)
            wait_event.setup()
            wait_event.wait()
            self.display4.destroy()
            self.firstrun = not self.firstrun
            self.players()
            #self.start(12)

app = Timer(root)
root.mainloop()