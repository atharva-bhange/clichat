import socket
import threading

from constants import *
from utils import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))


def clientHandler(conn, addr, clients):
    print("NEW CLIENT :", addr)
    clients[addr] = conn
    connected = True
    while connected:
        data = recvMsg(conn)
        if(data == DISCONNECT):
            connected = False
        for other_clients in clients.values():
            if(other_clients == conn):
                continue
            sendMsg(other_clients, data)

    sendMsg(conn, DISCONNECT)
    conn.close()
    del clients[addr]
    print("CLIENT LEFT :", addr)


def run():
    clients = {}
    server.listen()
    print("SERVER STARTED PORT :", PORT)
    while True:
        try:
            (conn, addr) = server.accept()
            thread = threading.Thread(
                target=clientHandler, args=(conn, addr, clients))
            thread.start()
            print("ONLINE CLIENTS :", threading.activeCount() - 1)

        except KeyboardInterrupt:
            break


run()
