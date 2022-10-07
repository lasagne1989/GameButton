#!/usr/bin/env python
#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

#py files
import press
import myIP
#libraries
import json
import websockets
import asyncio
import random
import subprocess
import itertools
from tkinter import *
from threading import *
import RPi.GPIO as GPIO

from GameButton import sounds

root = Tk()


class Timer:
    def __init__(self, master):
        self.master = master
        # Set up screen
        root.geometry("320x240")
        #root.attributes('-fullscreen', True)
        root['bg']='grey9'
        self.display1 = Label(master, fg='white', bg='grey9', font=("Ariel", 24))
        self.display1.place(relx=.5, rely=.5, anchor=S)
        self.display2 = Label(master, fg='white', bg='grey9', font=("Ariel", 35))
        self.display2.place(relx=.5, rely=.5, anchor=N)
        self.display1['text'] = 'Wait for Phone Connection'
        # Press count variable
        self.time_limit = 5
        self.press_count = 0
        # Start Websocket
        t = Thread(target=self.sockSVR).start()  
        # Pick first player and set up cycle
        self.players = []
        self.player_cycle = []
    
    def connection(self):
        self.display1['text'] = 'Connected and Ready, Press the Button'
        # Set up main button press
        reg_event = press.Button(GPIO.IN, GPIO.PUD_DOWN, GPIO.FALLING, self.start)
        reg_event.setup()
        reg_event.event()
        # Pick first player and set up cycle
        #people = [self.players]
        player_count = len(self.players)
        player_num = random.randint(0, player_count - 1)
        self.player_cycle = []
        for i in range(player_count):
            self.player_cycle.append(self.players[player_num % player_count])
            player_num += 1
        self.next_players = itertools.cycle(self.player_cycle)    
    
    def start(self, channel):
        # Show randomised First player on first press
        if self.press_count == 0:
            self.player = next(self.next_players)
            self.display1['text'] = self.player + ", You Go First!"
            self.press_count += 1
        elif self.press_count == 1:
            # Start the countdown for first player
            self.timer_text = DoubleVar()
            self.timer_text.set(self.time_limit + 1)
            self.display1['text'] = self.player
            self.display2['textvariable'] = self.timer_text
            self.increment_timer()
            self.press_count += 1
        # Restart the countdown and get the next player
        else:
            self.player = next(self.next_players)
            self.timer_text = DoubleVar()
            self.timer_text.set(self.time_limit)
            self.display1['text'] = self.player
            self.display2['textvariable'] = self.timer_text
            self.press_count += 1

    def increment_timer(self):
        self.ctr = int(self.timer_text.get())
        # countdown -1 second every second until we hit zero
        if self.ctr > 0:
            self.timer_text.set(self.ctr - 1)
            self.master.update()
            self.master.after(1000, self.increment_timer)
        # on zero give shit to the loser
        else:
            self.display1['text'] = self.player + ', You Dumb Bitch!'
            root.update()
            #sounds.gimmeSomeBanter()
            # wait for the button to be pressed again
            wait_event = press.Button(GPIO.IN, GPIO.PUD_DOWN, GPIO.FALLING, self.start)
            wait_event.wait()
            # sends us back to the middle condition on start and progresses us to the next player
            #Move these above wait?
            self.player = next(self.next_players)
            self.press_count = 1
    
    def sockSVR(self):
        async def handler(websocket):
            msg = await websocket.recv()
            if msg == 'beep':
                self.start()
            else:
                #print(msg)
                dict = json.loads(msg)
                #print(dict)
                #print(dict['time_limit'])
                #print(dict['players'])
                self.time_limit = dict['time_limit']
                self.players = dict['players']
                #print(f"{self.players}")
                start = f"start"
                await websocket.send(start)
                self.connection()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
        start_server= websockets.serve(handler, myIP.IPAddr, 8765)
        loop.run_until_complete(start_server)
        loop.run_forever()

if __name__=="__main__":
    app = Timer(root)
    root.mainloop()
