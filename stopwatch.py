import press
import time
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
        self.people = ['Gordon', 'Claire', 'Emma', 'Steve']
        self.playerCount = len(self.people)

    def increment_timer(self):
        ctr = int(self.timertext.get())
        if ctr > 0:
            self.timertext.set(ctr - 1)
            if self.timeit:
                root.update()
                self.master.after(1000, self.increment_timer)
            else:
                self.timertext.set(5)
                pick = firstplayer.playerPicker(self.people, self.playerNum)
                self.playerNum = pick.nextPlayer()
                self.player = self.people[self.playerNum]
                self.timeit = not self.timeit
        else:
            #self.display3.destroy()
            #self.display3 = Label(root, text="You Fucked It!", font=("Arial", 25))
            self.timertext.set(1000000)
            time.sleep(3)
            #self.display3.place(relx=.5, rely=.5, anchor=N)
            wait_event = press.Button(GPIO.IN, GPIO.PUD_DOWN, GPIO.FALLING, 0)
            wait_event.setup()
            wait_event.wait()
            #self.display4.destroy()
            pick = firstplayer.playerPicker(self.people, self.playerNum)
            self.playerNum = pick.nextPlayer()
            self.player = self.people[self.playerNum]
            self.timeit = not self.timeit
            self.start(12)

    def start(self, channel):
        if not self.started:
            self.display.destroy()
            pick = firstplayer.playerPicker(self.people, 0)
            self.playerNum = pick.firstPlayer()
            self.player = self.people[self.playerNum]
            self.display1 = Label(self.master, text=(self.player + ', You Go First!'), font=("Arial", 25))
            self.display1.place(relx=.5, rely=.5, anchor=CENTER)
            self.started = not self.started
        else:
            self.timeit = not self.timeit
            self.timertext = DoubleVar()
            self.timertext.set(5 + 1)
            self.display1.destroy()
            self.display2 = Label(root, text=self.player, font=("Arial", 25))
            self.display2.place(relx=.5, rely=.5, anchor=S)
            self.display3 = Label(root, textvariable=self.timertext, font=("Arial", 25))
            self.display3.place(relx=.5, rely=.5, anchor=N)
            self.increment_timer()


app = Timer(root)
root.mainloop()