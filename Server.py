import  socket

PORT = 8800
HOST = "192.168.25.237"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Created")
except:
    print("Failed to create socket")

s.bind((HOST, PORT))
s.listen()

while True:
    conn, addr = s.accept()
    print(f"Got connection from: {addr}")

    dataSend = "hello".encode()
    conn.send(len(dataSend).to_bytes(4, "big"))
    conn.send(dataSend)

    message_size = int.from_bytes(conn.recv(4), "big")
    dataGot: str = conn.recv(message_size).decode()
    print(f"Received: {dataGot}")

    conn.close()
    print("Connection Closed")
