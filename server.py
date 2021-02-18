from socket import *

myHost = '0.0.0.0'
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)      # AF_INET - IP protocol, SOCK_STREAM - TCP
sockobj.bind((myHost, myPort))
sockobj.listen(5)

while True:
    connection, address = sockobj.accept()
    print('Server connected by', address)

    while True:
        data = connection.recv(1024)

        if not data : break
        connection.send(b'Echo => ' + data)

    connection.close()
'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0' #this is ip
port = 1204
s.bind((host,port))
s.listen(1)
socketclint , address = s.accept()
print("got conection from :",address)
con = True
while con:
    msg = socketclint.recv(1024)
    msg = msg.decode("utf-8")
    print("clint data :",msg)
    ap = input("enter msg : ")
    socketclint.send(ap.encode("utf-8"))
    if msg == "quit":
        s.close()
        con = False
'''
