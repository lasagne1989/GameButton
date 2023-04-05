#!/usr/bin/env python
# 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

from _socket import gethostname, gethostbyname
from websockets import serve
import asyncio

msg = str


def sockSVR():
    print("running...")
    hostname = gethostname()
    hnlocal = f"{hostname}.local"
    ip_addr = gethostbyname(hnlocal)
    print(ip_addr)

    async def handler(websocket):
        global msg
        msg = await websocket.recv()
        print(msg)
        start = f"start"
        await websocket.send(start)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start_server = serve(handler, "%s" % ip_addr, 8765)
    loop.run_until_complete(start_server)
    loop.run_forever()
    return msg


if __name__ == "__main__":
    sockSVR()
