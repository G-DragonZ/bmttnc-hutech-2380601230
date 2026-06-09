import socket
import ssl
import threading
import signal
import sys

server_address = ('localhost', 12345)
clients = []
clients_lock = threading.Lock()

def handle_client(client_socket):
    peer = None
    try:
        peer = client_socket.getpeername()
    except Exception:
        peer = ('unknown', 0)

    with clients_lock:
        clients.append(client_socket)
    print("Client connected: {}".format(peer))

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            text = data.decode(errors='replace')
            print("Received from {}: {}".format(peer, text))
            # broadcast to other clients
            with clients_lock:
                for c in list(clients):
                    if c is not client_socket:
                        try:
                            c.sendall(data)
                        except Exception:
                            # ignore send errors; the other thread will clean up
                            pass
    except Exception as e:
        print(f"Error handling client {peer}: {e}")
    finally:
        print("Client disconnected: {}".format(peer))
        with clients_lock:
            if client_socket in clients:
                clients.remove(client_socket)
        try:
            client_socket.shutdown(socket.SHUT_RDWR)
        except Exception:
            pass
        client_socket.close()


def create_ssl_context(certfile='certificates/cert.pem', keyfile='certificates/key.pem'):
    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
    ctx.load_cert_chain(certfile=certfile, keyfile=keyfile)
    return ctx


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print("Server is listening on {}:{}".format(*server_address))

    # create SSL context once
    try:
        context = create_ssl_context()
    except Exception as e:
        print(f"Failed to create SSL context (missing/invalid certs?): {e}")
        server_socket.close()
        return

    def shutdown(signum, frame):
        print("Shutting down server...")
        try:
            server_socket.close()
        except Exception:
            pass
        # close all clients
        with clients_lock:
            for c in list(clients):
                try:
                    c.shutdown(socket.SHUT_RDWR)
                except Exception:
                    pass
                c.close()
            clients.clear()
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    while True:
        try:
            client_socket, client_address = server_socket.accept()
        except OSError:
            # socket closed
            break

        try:
            ssl_socket = context.wrap_socket(client_socket, server_side=True)
        except Exception as e:
            print(f"SSL handshake failed from {client_address}: {e}")
            client_socket.close()
            continue

        client_thread = threading.Thread(target=handle_client, args=(ssl_socket,))
        client_thread.daemon = True
        client_thread.start()


if __name__ == '__main__':
    main()
