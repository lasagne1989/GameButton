#!/usr/bin/env python

import asyncio
import websockets
import threading

def sockSVR():
    async def handler(websocket):
        name = await websocket.recv()
        print(f"<<< {name}")

        greeting = f"Hello {name}!"

        await websocket.send(greeting)
        print(f">>> {greeting}")
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    start_server= websockets.serve(handler, "localhost", 8765)
    loop.run_until_complete(start_server)
    loop.run_forever()


#if __name__ == "__main__":
#    asyncio.run(sockSVR())
