import socket
from Chat import start_chat

PORT = 8800

def main():
    while True:
        host = input("Server IP: ")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((host, PORT))

        start_chat(s)

        s.close()

if __name__ == "__main__":
    main()
