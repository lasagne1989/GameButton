import time
import random
import press
import RPi.GPIO as GPIO

buttonPress = False  #has the button been pressed 
countPress= 0  #has the game been started
#starttime = str()   #time each layer will have
#startMessage= StringVar()    #the message after the first player is selected
firstPlayer= str()     #the first player (who will be slected in intialiseGame below)
temp=int()
stop = false
player=int()
pin = [10, 12, 18]
channel = pin[0]
players = ["Gordon", "Claire", "Emma", "Steve"]    #array of the players

#count the number of players for the randomisation
numPlayers=len(players)

def intialiseGame():
    global countPress
    global firstPlayer
    global player
    player = random.randint(0,numPlayers-1)
    firstPlayer = players[player]    #find the first player from 'players' array randomly
    startMessage =('%s You Go First!' %firstPlayer)
    countPress = 1  #add one to countPress so the loop doesnt run again
    print (startMessage)
    
def fuckedIt():
    global player
    global players
    global firstPlayer
    global pin
    print('%s You Fucked It!' %firstPlayer)
    GPIO.wait_for_edge(pin[1],GPIO.FALLING,bouncetime=1000)
    if player == (numPlayers-1):
        player = 0
    else:
        player += 1
    firstPlayer = players[player]
    submit(channel)
    
        
def loop_stop():
    global stop
    stop= not stop

def submit(channel):#change to wait til press.
    global temp
    global stop
    stop = False
    if countPress == 0:
        intialiseGame()
    else:
        GPIO.add_event_detect(pin[2],GPIO.FALLING, callback=loop_stop, bouncetime=1000)
        temp=5
        while temp>-1 and stop=False:
            if temp > -1:
                print(temp, end='\r')
                #root.update()
                time.sleep(1)
                temp -= 1
            if temp== -1:
                fuckedIt()
        else:
            submit(channel)


regEvent = press.button(pin, GPIO.IN, GPIO.PUD_DOWN)      
regEvent.setup()
#while True:
GPIO.add_event_detect(channel,GPIO.FALLING,callback=submit,bouncetime=1000)
    #submit()
    #if GPIO.event_detected(pin[0]):
     #   submit()
#GPIO.cleanup()