from constants import *
import pickle


def sendMsg(conn, data):
    try:
        encoded_data = pickle.dumps(data)
        msg_length = len(encoded_data)
        send_length = pickle.dumps(str(msg_length))
        send_length = pickle.dumps(
            str(msg_length) + str(" "*(HEADERSIZE - len(send_length))))
        conn.send(send_length)
        conn.send(encoded_data)
        return True
    except:
        return False


def recvMsg(conn):
    try:
        msg_length = pickle.loads(conn.recv(HEADERSIZE))
        if(msg_length):
            msg_length = int(msg_length)
            data = pickle.loads(conn.recv(msg_length))
            return data
    except:
        return False
