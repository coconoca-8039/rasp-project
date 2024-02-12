import os
import posix_ipc
import sys
from can_all import can_get_0A1224AA

def handle_client(mq):
    while True:
        try:
            message, _ = mq.receive()
            # print(type(message))  # bytes of class
            can_data = message.decode().split(' ')
            # print(type(can_data))
             
            # print(can_data)  # 受信したデータを全表示

            if can_data[2] == '0A1234AA':
                tmp = can_get_0A1224AA(can_data, '0A1234AA')
                print(tmp)
                print("  ")
                
            #tmp = can_get_0A1224AA(can_data, '0A1234AA')
            #print(tmp)
            
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
