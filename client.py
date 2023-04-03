from socket import *

serverName = gethostname()
serverPort = 51000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while True:
    sentence = input("Filename : ")
    if sentence == "over":
        break
    else:
        clientSocket.send(sentence.encode())
        msg  = clientSocket.recv(2048).decode()
        intmsg = int(msg)
        res = tuple(intmsg.to_bytes(4, byteorder ='big'))
        garb_value,words,char,lines = res
        print(f"Characters : {char}")
        print(f"Words      : {words}")
        print(f"Line       : {lines}")
clientSocket.close()
