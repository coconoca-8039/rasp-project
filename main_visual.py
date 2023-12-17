# import socket
# import threading
# import pickle
import os
import posix_ipc
import sys

def handle_client(mq):
    while True:
        try:
            message, _ = mq.receive()
            can_data = message.decode().split(' ')
            print(can_data)  # 受信したデータを表示
        except posix_ipc.BusyError:
            print("Message queue is full, skipping this message.")
        except Exception as e:
            print(f"An error occurred: {e}")

def main_visual_server():
    mq_name = "/can_data_mq"
    mq = posix_ipc.MessageQueue(mq_name, posix_ipc.O_CREAT)

    handle_client(mq)

    mq.close()
    mq.unlink()

if __name__ == "__main__":
    main_visual_server()
