import threading
import datetime

def send_messages(conn):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        dataSend = input("").encode()
        conn.send(len(dataSend).to_bytes(4, "big"))
        conn.send(dataSend)

def get_messages(conn):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        message_size = int.from_bytes(conn.recv(4), "big")
        dataGot: str = conn.recv(message_size).decode()
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{current_time}] {dataGot}")

def start_chat(conn):
    t1 = threading.Thread(target=send_messages, args=(conn,), daemon=True)
    t1.start()
    t2 = threading.Thread(target=get_messages, args=(conn,), daemon=True)
    t2.start()

    while True:
        try:
            conn.send(b'')
        except KeyboardInterrupt:
            exit()
        except:
            print("Connection lost")
            t1.do_run = False
            t2.do_run = False
            break
