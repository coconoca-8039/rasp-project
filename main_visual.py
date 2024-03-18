import os
import posix_ipc
import sys
import time
from datetime import datetime
import sched
import sqlite3
from can_0A1224AA import can_get_0A1224AA
from can_0CCC2222 import can_get_0CCC2222

def handle_client(mq):

    # この部分はまだ試作これから作り込む
    # can_functions = {
    	# '0A1234AA': can_get_0A1234AA,
    	# '0CCC2222': can_get_0CCC2222
    # }
    
    while True:
        try:
            message, _ = mq.receive()
            can_data = message.decode().split(' ')
            # print(type(can_data))
             
            # print(can_data)  # 受信したデータを全表示
            
            # １時間に1度だけ実行する処理
            current_time = datetime.now()
            if current_time.minute == 0 || current_time.second == 0:           
            	# ここでSqliteにデータを格納する
            	# この処理は別スレッドにしたほうがいいかも
            	# insert_climate_data()
            
            # ここの処理を６時間おきとかで実行したい
            if can_data[2] == '0A1234AA':
                can_0A1234AA = can_get_0A1224AA(can_data, '0A1234AA')
                # print(can_0A1234AA)
                # print("  ")
            
            if can_data[2] == '0CCC2222':
                can_0CCC2222 = can_get_0CCC2222(can_data, '0CCC2222')
                # print(can_0CCC2222)
                # print("  ")
                
            print(can_0A1234AA + can_0CCC2222)
            print("")
            
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
