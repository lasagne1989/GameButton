import press
import firstplayer
from tkinter import *
import RPi.GPIO as GPIO

root = Tk()


class Timer:
    def __init__(self, master):
        self.master = master
        root.geometry("320x240")
        self.display = Label(master, font=("Arial", 25))
        self.display.place(relx=.5, rely=.5, anchor=CENTER)
        self.display1 = Label(master, font=("Arial", 25))
        self.display1.place(relx=.5, rely=.5, anchor=S)
        self.display2 = Label(master, font=("Arial", 25))
        self.display2.place(relx=.5, rely=.5, anchor=N)
        reg_event = press.Button(GPIO.IN, GPIO.PUD_DOWN, GPIO.FALLING, self.start)
        reg_event.setup()
        reg_event.event()
        self.timeit = False
        self.press_count = 0
        self.people = ['Gordon', 'Claire', 'Emma', 'Steve']
        self.playerCount = len(self.people)

    def start(self, channel):
        if self.press_count == 0:
            pick = firstplayer.playerPicker(self.people, 0)
            self.playerNum = pick.firstPlayer()
            self.player = self.people[self.playerNum]
            self.press_count += 1
            print(self.press_count)
        elif self.press_count == 1:
            self.timeit = not self.timeit
            self.display.destroy()
            self.timertext = DoubleVar()
            self.timertext.set(5 + 1)
            text=self.player
            textvariable=self.timertext
            self.increment_timer()
            self.press_count += 1
            print(self.press_count)
        else:
            self.timeit = not self.timeit
            self.timertext = DoubleVar()
            self.timertext.set(5 + 1)
            text=self.player
            textvariable=self.timertext
            self.increment_timer()
            self.press_count += 1
            print(self.press_count)

    def increment_timer(self):
        ctr = int(self.timertext.get())
        if ctr > 0:
            self.timertext.set(ctr - 1)
            if self.timeit:
                self.master.update()
                self.master.after(1000, self.increment_timer)
            else:
                #self.timertext.set(5)
                #root.update()
                pick = firstplayer.playerPicker(self.people, self.playerNum)
                self.playerNum = pick.nextPlayer()
                self.player = self.people[self.playerNum]
                self.timeit = not self.timeit
        else:
            self.display3 = text="You Fucked It!"
            root.update()
            wait_event = press.Button(GPIO.IN, GPIO.PUD_DOWN, GPIO.FALLING, 0)
            #wait_event.setup()
            wait_event.wait()
            self.timeit = not self.timeit
            #self.start(12)

app = Timer(root)
root.mainloop()

