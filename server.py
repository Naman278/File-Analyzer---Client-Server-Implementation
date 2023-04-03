import socket
import threading
import os


def handle_client(conn, addr):
    print("New Connection")

    while True:
        msg = conn.recv(2048).decode()
        if not msg:
            print('Bye')
            break
        words,char,lines = counter(msg)
        msg = (words,char,lines)
        res = int.from_bytes(msg, byteorder ='big')
        conn.send(str(res).encode())
    conn.close()
    
def counter(fname):
    num_words = 0
    num_lines = 0
    num_charc = 0
    with open(fname, 'r') as f:
    	for line in f:
            line = line.strip(os.linesep)
            wordslist = line.split()
            num_lines = num_lines + 1
            num_words = num_words + len(wordslist)
            num_charc = num_charc + sum(1 for c in line if c not in (os.linesep, ' '))
    return num_words,num_charc,num_lines

def main():
    port = 51000
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("",port))
    server.listen(1)
    print(f"[LISTENING] Server is listening...")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, ("",port)))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    main()
