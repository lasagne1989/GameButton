import press
import firstplayer
from tkinter import *
import RPi.GPIO as GPIO


root = Tk()

class Timer:
    def __init__(self, master):
        self.master=master
        root.geometry("320x240")
        self.display = Label(master, text = "We're going to play a little game", font=("Arial", 25))
        self.display.place(relx=.5, rely=.5,anchor= CENTER)   
        regEvent = press.button(10, GPIO.IN, GPIO.PUD_DOWN)      
        regEvent.setup()
        GPIO.add_event_detect(10,GPIO.FALLING,callback=self.start,bouncetime=1000)
        self.timeit=False
        self.started=False
        self.people = ['Gordon','Claire','Emma','Steve']
        self.playerCount = len(self.people)

    def increment_timer(self):
        ctr=int(self.timertext.get())
        self.timertext.set(ctr - 1)
        
        if self.timeit:
            self.master.update()
            self.master.after(1000, self.increment_timer)
        else:
            self.timertext.set(20)
            pick = firstplayer.playerPicker(self.people,self.playerNum)
            self.playerNum = pick.nextPlayer()
            self.player = self.people[self.playerNum]
            print(self.player)
            self.timeit= not self.timeit

    def start(self,channel):
        if not self.started:
            self.display.destroy()
            pick = firstplayer.playerPicker(self.people,0)
            self.playerNum = pick.firstPlayer()
            self.player = self.people[self.playerNum]
            self.display1 = Label(self.master, text = (self.player + ', You Go First!'), font=("Arial", 25))
            self.display1.place(relx=.5, rely=.5,anchor= CENTER) 
            self.started = not self.started
        else:
            self.timeit = not self.timeit
            self.timertext = DoubleVar()
            self.timertext.set(20+1)
            self.display1.destroy()
            self.display2 = Label(root, text = self.player, font=("Arial", 25))
            self.display2.place(relx=.5, rely=.5,anchor= N) 
            self.display3 = Label(root, textvariable = self.timertext, font=("Arial", 25))
            self.display3.place(relx=.5, rely=.5,anchor= S)        
            self.increment_timer()

app = Timer(root)
root.mainloop()