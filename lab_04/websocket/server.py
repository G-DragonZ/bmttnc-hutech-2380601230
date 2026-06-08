import random
import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketServer(tornado.websocket.WebSocketHandler):
    clients = set()

    def open(self):
        self.__class__.clients.add(self)
        print("WebSocket connection opened")

    def on_message(self, message: str):
        print("Received message:", message)
        self.write_message(f"Echo: {message}")

    def on_close(self):
        self.__class__.clients.discard(self)
        print("WebSocket connection closed")

    @classmethod
    def send_message(cls, message: str):
        for client in cls.clients:
            client.write_message(message)

class RandomWordSelector:
    def __init__(self, word_list):
        self.word_list = word_list

    def sample(self):
        return random.choice(self.word_list)


def main():
    word_list = [
        "apple", "banana", "cherry", "date", "elderberry",
        "fig", "grape", "honeydew", "kiwi", "lemon",
    ]
    app = tornado.web.Application([
        (r"/websocket", WebSocketServer),
    ])
    app.listen(8888)
    print("WebSocket server started at ws://localhost:8888/websocket")
    word_selector = RandomWordSelector(word_list)
    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda: WebSocketServer.send_message(word_selector.sample()), 1000)
    periodic_callback.start()
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
