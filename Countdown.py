#push test
import time
import random
import RPi.GPIO as GPIO
from tkinter import *

# creating Tk window
root = Tk()

# setting geometry of tk window
root.geometry("320x240")

# Declaration of variables
buttonPress = False  #has the button been pressed - for long press
countPress= 0  #has the game been started
starttime = StringVar()   #time each layer will have
startMessage= StringVar()    #the message after the first player is selected
firstPlayer= str()     #the first player (who will be slected in intialiseGame below)
players = ["Gordon", "Claire", "Emma", "Steve"]    #array of the players

#count the number of players for the randomisation
numPlayers=len(players)

#Define Labels 
timeframe = Label(root, textvariable=starttime) #label conatining the countdown
timeframe.pack()
timeframe.place(x=180, y=20)
whosfirst = Label(root, textvariable=startMessage) #label contining the stating message - to be shown after first long press
whosfirst.pack()
whosfirst.place(x=180, y=20)

#label clearers
def clear_widget(widget):
    widget.destroy()

#set up GPIO
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# operation to perform when start game is pressed (to be replaced by long press)
def intialiseGame():
    global countPress
    global firstPlayer
    #if not countPress:  #only to happen when the button is pressed for the first time
    firstPlayer = players[random.randint(0,numPlayers-1)]    #find the first player from 'players' array randomly
    startMessage.set('%s You Go First!' %firstPlayer)
    countPress = 1  #add one to countPress so the loop doesnt run again
    sleep(5)
    print (countPress)

 
def fuckedIt():
        var = IntVar()
        timeup = Label(root, text='%s You Fucked It!' %firstPlayer)
        timeup.pack()
        timeup.place(x=180, y=30)
        btn3 = Button(root, text='Countdown', bd='5',  #button to be replaced by next button press
                        command=lambda : var.set(1))
        btn3.place(x=70, y=120)
        tn3.wait_variable(var)
        clear_widget(timeup)
        clear_widget(btn3)
        del var
        submit()

def countdown():
        clear_widget(whosfirst)
        print("yes")
        starttime.set("5")   #deines how much time each player has - '5' to be a variable
        temp = int(starttime.get())
        while temp > -1:
            if buttonPressed:
                    break;
        # two decimal places
            starttime.set("{0:2d}".format(temp))
        # updating the GUI window after decrementing the temp value every time
            root.update()
            time.sleep(1)
        # when temp value = 0; then a message pop's up
        # after every one sec the value of temp will be decremented by one
            temp -= 1
            if temp == -1:
                fuckedIt()
      


def submit(channel):#change to wait til press.
    print(countPress)
    if countPress == 0:
        intialiseGame()
    if countPress > 0:
        countdown()

setup()
GPIO.add_event_detect(10,GPIO.FALLING,callback = submit,bouncetime=1000)
#start the game - to be replaced with long press then 'are you ready'
#btn1 = Button(root, text='start the game', bd='5',
#                 command=intialiseGame)
#btn1.place(x=70, y=160)

#reset the timer when your go is done
#btn = Button(root, text='Countdown', bd='5',
#             command=lambda : [clear_widget(whosfirst),submit()])
#btn.place(x=70, y=120)
# until an interrupt occurs
root.mainloop()
