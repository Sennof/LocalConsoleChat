import threading
import datetime

def send_messages(conn):
    while True:
        dataSend = input("").encode()
        conn.send(len(dataSend).to_bytes(4, "big"))
        conn.send(dataSend)

def get_messages(conn):
    while True:
        message_size = int.from_bytes(conn.recv(4), "big")
        dataGot: str = conn.recv(message_size).decode()
        print(f"[{datetime.datetime.now}] {dataGot}")

def start_chat(conn):
    threading.Thread(target=send_messages, args=(conn,), daemon=True).start()
    threading.Thread(target=get_messages, args=(conn,), daemon=True).start()
    while True:
        try:
            conn.send(b'')
        except KeyboardInterrupt:
            exit()
        except:
            print("Connection lost")
            break

