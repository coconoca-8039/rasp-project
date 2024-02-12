import os
import posix_ipc
import sys

def handle_client(mq):
    while True:
        try:
            message, _ = mq.receive()
            # print(type(message))  # bytes of class
            can_data = message.decode().split(' ')
            print(type(can_data))
            # print(can_data[0])
            
            # dropped_can_data = []
            # exclude_elements = [0, 1, 3]
            # for elem in can_data:
            	# if elem not in exclude_elements:
            		# dropped_can_data[elem]
            # print(dropped_can_data)
            
            # can_data = list(can_data)
            #exclude_elements = [0, 1, 3]
            #filtered_list = list(filter(lambda x: x not in exclude_elements, can_data))
            #print(filtered_list)
             
            # print(can_data)  # 受信したデータを表示

            if can_data[2] == '1234ABCD':
                can_1234ABCD = can_data[2]
                print(can_1234ABCD)

            
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
