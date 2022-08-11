import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        players = ("Tom, Dick, Harry")
        await websocket.send(players)

        start = await websocket.recv()
        print(f"{start}")

if __name__ == "__main__":
    asyncio.run(hello())
