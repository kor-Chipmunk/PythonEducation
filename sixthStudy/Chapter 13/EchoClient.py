import socket
import sys

if __name__ == '__main__':

    # if len(sys.argv) < 4:
    #     print("{0} <Bind IP> <Server IP> <Message>".format(sys.argv[0]))
    #     sys.exit()

    bindIP = "127.0.0.1"
    serverIP = "127.0.0.1"
    message = "Hello, World!"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((bindIP, 0))

    try:
        sock.connect((serverIP, 5425))

        # 메아리 송신
        sbuff = bytes(message, encoding="utf-8")
        sock.send(sbuff)
        print("송신 : {0}".format(message))

        # 메아리 수신
        rbuff = sock.recv(1024)
        received = str(rbuff, encoding="utf-8")
        print("수신 : {0}".format(received))
    finally:
        sock.close()