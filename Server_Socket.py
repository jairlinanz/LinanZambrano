import os
import socket
from socketserver import BaseRequestHandler, TCPServer
import threading
import socketserver

SERVER_HOST = 'localhost'
SERVER_PORT = 0 # tells the kernel to pick up a port dynamically
BUF_SIZE = 1024
def client(ip, port, message):
    """ A client to test threading mixin server""" 
 # Connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(BUF_SIZE)
        print("Client received: %s") %response
    finally:
        sock.close()

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """ An example of threaded TCP request handler """
    def handle(self):
        data = self.request.recv(1024)
        current_thread = threading.current_thread()
        response = "%s: %s" %(current_thread.name, data)
        self.request.sendall(response)
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.
TCPServer):
    """Nothing to add here, inherited everything necessary from 
    parents"""
    pass
if __name__ == "__main__":
 # Run server
    server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT), 
    ThreadedTCPRequestHandler)
    ip, port = server.server_address # retrieve ip address
    # Start a thread with the server -- one thread per request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread exits
    server_thread.daemon = True
    server_thread.start()
    print ("Server loop running on thread: %s") %server_thread.name
    # Run clients
    client(ip, port, "Hello from client 1")
    client(ip, port, "Hello from client 2")
    client(ip, port, "Hello from client 3")
    # Server cleanup
    server.shutdown()