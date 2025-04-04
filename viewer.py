import socket
import asyncio
import websockets

clients = set()

async def sender(websocket):
    # Removed the 'path' parameter that was causing the error
    clients.add(websocket)
    try:
        await asyncio.Future()  # Keep the connection alive
    finally:
        clients.remove(websocket)

def recv_udp(sock):
    try:
        return sock.recvfrom(1024)
    except BlockingIOError:
        return None, None

async def udp_listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 5005))
    sock.setblocking(False)
    loop = asyncio.get_event_loop()

    while True:
        data, addr = await loop.run_in_executor(None, recv_udp, sock)
        if data:
            try:
                message = data.decode().strip()
                for ws in clients.copy():
                    try:
                        await ws.send(message)
                    except:
                        clients.discard(ws)
            except Exception as e:
                print("Error decoding/sending:", e)
        await asyncio.sleep(0.01)

async def main():
    print("✅ WebSocket server starting at ws://localhost:6789")
    async with websockets.serve(sender, "0.0.0.0", 6789):
        await udp_listener()

if __name__ == "__main__":
    asyncio.run(main())