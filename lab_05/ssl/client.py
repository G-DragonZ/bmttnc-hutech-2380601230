import socket
import ssl
import threading
server_address = ('localhost', 12345)
def receive_messages(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("Received: {}".format(data.decode('utf-8')))
    except:
        pass
    finally:
        print("Connection closed")
        ssl_socket.close()
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')
ssl_socket.connect(server_address)
receive_thread = threading.Thread(target=receive_messages, args=(ssl_socket,))
receive_thread.start()
try:
    while True:
        message = input("Enter message to send: ")
        if message.lower() == 'exit':
            break
        ssl_socket.sendall(message.encode())
finally:
    ssl_socket.close()