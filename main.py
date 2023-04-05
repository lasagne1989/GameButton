#!/usr/bin/env python

from _socket import gethostname, gethostbyname
from websockets import serve
from threading import Thread
import asyncio
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
        #Set up label
        self.display1 = Label(master, fg='white', bg='grey9', font=("Ariel", 35), wraplength=318)
        self.display1.place(relx=.5, rely=.5, anchor="center")
        self.display1['text'] = 'Connect Phone'
        #Update screen
        #root.update()
        #Initiate variables
        self.msg = None
        self.dob = None
        self.players = None
        self.time_limit = None
        self.mode = None
        # Start Websocket
        t = Thread(target=self.sockSVR).start()

    def sockSVR(self):
        print("running...")
        hostname = gethostname()
        hnlocal = f"{hostname}.local"
        ip_addr = gethostbyname(hnlocal)
        print(ip_addr)

        async def handler(websocket):
            self.msg = await websocket.recv()
            print(self.msg)
            start = f"start"
            await websocket.send(start)
            self.data()
            self.pickMode()

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        start_server = serve(handler, "%s" % ip_addr, 8765)
        loop.run_until_complete(start_server)
        loop.run_forever()

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
