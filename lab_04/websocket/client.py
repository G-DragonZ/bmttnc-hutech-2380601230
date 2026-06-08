import tornado.ioloop
import tornado.websocket
from tornado import gen

RECONNECT_DELAY_SECONDS = 3
SERVER_URL = "ws://localhost:8888/websocket"

class WebSocketClient:
    def __init__(self, server_url):
        self.server_url = server_url
        self.websocket = None
        self.connected = False

    async def connect(self):
        while True:
            try:
                print(f"Connecting to {self.server_url}...")
                self.websocket = await tornado.websocket.websocket_connect(self.server_url)
                self.connected = True
                print("Connected to server")
                tornado.ioloop.IOLoop.current().spawn_callback(self.receive_messages)
                return
            except Exception as exc:
                self.connected = False
                print(f"Connection failed: {exc}")
                print(f"Retrying in {RECONNECT_DELAY_SECONDS} seconds...")
                await gen.sleep(RECONNECT_DELAY_SECONDS)

    async def receive_messages(self):
        while self.connected and self.websocket is not None:
            try:
                message = await self.websocket.read_message()
                if message is None:
                    raise ConnectionError("Server closed the connection")
                print("Received message:", message)
            except Exception as exc:
                self.connected = False
                print("Connection lost:", exc)
                self.websocket = None
                await self.connect()
                break

    async def send_message(self, message):
        if not self.connected or self.websocket is None:
            print("Not connected. Waiting to reconnect...")
            return
        try:
            await self.websocket.write_message(message)
        except Exception as exc:
            print("Send failed:", exc)
            self.connected = False
            self.websocket = None
            await self.connect()

    def close(self):
        if self.websocket is not None:
            self.websocket.close()
            self.connected = False


async def main():
    client = WebSocketClient(SERVER_URL)
    await client.connect()

    while True:
        message = await tornado.ioloop.IOLoop.current().run_in_executor(None, input, "Enter message to send: ")
        if message == "exit":
            client.close()
            break
        await client.send_message(message)


if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)
