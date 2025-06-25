import  socket
from Chat import start_chat

PORT = 8800
HOST = "192.168.25.237"


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        print(f"Got connection from: {addr}")

        start_chat(conn)

        conn.close()
        print("Connection Closed")

if __name__ == "__main__":
    main()