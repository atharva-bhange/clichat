
import socket
import threading

from constants import *
from utils import *

msgs = []


def retriveMsg(conn):
    global msgs
    while True:
        new_msg = recvMsg(conn)
        if(new_msg):
            msgs.append(new_msg)
        else:
            break


def run():
    global msgs

    name = input("Username :")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    thread = threading.Thread(
        target=retriveMsg, args=(client,))
    thread.start()

    print("1) Send Message")
    print("2) Recieve Message")
    print("3) Disconnect")
    while True:
        option = input("? ")
        if(option == "1"):
            msg = input("> ")
            sendMsg(client, {"name": name, "msg": msg})
        elif(option == "2"):
            for msg in msgs:
                print(msg["name"], ":", msg["msg"])
            msgs = []
        elif(option == "3"):
            sendMsg(client, DISCONNECT)
            break
        else:
            print("Invalid Option")


run()
