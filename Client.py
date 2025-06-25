import socket

HOST = "192.168.25.237"
PORT = 8800

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))

    msg = "Hello, Server!".encode()
    s.send(len(msg).to_bytes(4, "big"))
    s.send(msg)

    msg_size = int.from_bytes(s.recv(4), "big")
    msg = s.recv(msg_size)

if __name__ == "__main__":
    main()
