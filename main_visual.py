import os
import posix_ipc
import sys
import time
from datetime import datetime, timedelta
import sched
import sqlite3
from can_0A1224AA import can_get_0A1224AA
from can_0CCC2222 import can_get_0CCC2222
from can_1777DDDD import can_get_1777DDDD
from can_1888DDDD import can_get_1888DDDD
from ClimateData import insert_climate_data

tempture_avg = []
humidity_avg = []
pressure_avg = []
latitude_avg = []
longitude_avg =[]
elevation_avg = []
satellite_count_avg = []
x_direction_avg = []
y_direction_avg =[]
z_direction_avg =[]

def handle_client(mq):

    # この部分はまだ試作これから作り込む
    # can_functions = {
    	# '0A1234AA': can_get_0A1234AA,
    	# '0CCC2222': can_get_0CCC2222
    # }
    
    function_executed = False
    target_time = datetime.now() + timedelta(seconds=30)
    start_time = time.time()
    
    while True:
        try:
            message, _ = mq.receive()
            can_data = message.decode().split(' ')
            # print(type(can_data))
            # print(can_data)  # 受信したデータを全表示
            
            elapsed_time = time.time() - start_time
            elapsed_time = round(elapsed_time, 2)
            print(f"経過時間：{elapsed_time}秒")
            
            if can_data[2] == '0A1234AA':
                can_0A1234AA = can_get_0A1224AA(can_data, '0A1234AA')
                
                tempture = can_0A1234AA[0]
                tempture = float(tempture.replace(" ℃", ""))
                tempture_avg.append(tempture)
                
                humidity = can_0A1234AA[1]
                humidity = float(humidity.replace(" %", ""))
                humidity_avg.append(humidity)
                
                pressure = can_0A1234AA[2]
                pressure = float(pressure.replace(" hPa", ""))
                pressure_avg.append(pressure)
            	
                # print(can_0A1234AA)
                # print("  ")
            
            if can_data[2] == '0CCC2222':
                can_0CCC2222 = can_get_0CCC2222(can_data, '0CCC2222')
                
                xaxis = can_0CCC2222[0]
                xaxis = float(xaxis.replace("X方向 ", ""))
                x_direction_avg.append(xaxis)
                
                yaxis = can_0CCC2222[1]
                yaxis = float(yaxis.replace("Y方向 ", ""))
                y_direction_avg.append(yaxis)
                
                zaxis = can_0CCC2222[2]
                zaxis = float(zaxis.replace("Z方向 ", ""))
                z_direction_avg.append(zaxis)
            	
                # print(can_0CCC2222)
                # print("  ")
                
            if can_data[2] == '1888DDDD':
                can_1888DDDD = can_get_1888DDDD(can_data, '1888DDDD')
                
                satellites = can_1888DDDD[0]
                satellites = int(satellites.replace("衛星数：", ""))
                satellite_count_avg.append(satellites)
                
                altitude = can_1888DDDD[1]
                altitude = float(altitude.replace("標高：", ""))
                elevation_avg.append(altitude)
            	
                # print(can_1888DDDD)
                # print("  ")
             
            if can_data[2] == '1777DDDD':
                can_1777DDDD = can_get_1777DDDD(can_data, '1777DDDD')
                
                longitude = can_1777DDDD[0]
                longitude = float(longitude.replace("経度：", ""))
                longitude_avg.append(longitude)
                
                latitude = can_1777DDDD[1]
                latitude = float(latitude.replace("緯度：", ""))
                latitude_avg.append(latitude)
            	
                # print(can_1777DDDD)
                # print("  ")
                
            # コンソールへの表示
            print(can_0A1234AA + can_0CCC2222)
            print(can_1888DDDD + can_1777DDDD)
            print("")
            
            # リストのデータ数を10件に保つ処理
            mean_tempture = round(sum(tempture_avg) / len(tempture_avg), 2)
            print(f"温度の平均：{mean_tempture}")
            if len(tempture_avg) > 10:
            	tempture_avg.pop(0)
            	
            mean_humidity = round(sum(humidity_avg) / len(humidity_avg), 2)
            print(f"湿度の平均：{mean_humidity}")
            if len(humidity_avg) > 10:
            	humidity_avg.pop(0)
            	
            mean_pressure = round(sum(pressure_avg) / len(pressure_avg), 2)
            print(f"気圧の平均：{mean_pressure}")
            if len(pressure_avg) > 10:
            	pressure_avg.pop(0)
            	
            mean_latitude = round(sum(latitude_avg) / len(latitude_avg), 2)
            print(f"緯度の平均：{mean_latitude}")
            if len(latitude_avg) > 10:
            	latitude_avg.pop(0)
            	
            mean_longitude = round(sum(longitude_avg) / len(longitude_avg), 2)
            print(f"経度の平均：{mean_longitude}")
            if len(longitude_avg) > 10:
            	longitude_avg.pop(0)
            	
            mean_elevation = round(sum(elevation_avg) / len(elevation_avg), 2)
            print(f"標高の平均：{mean_elevation}")
            if len(elevation_avg) > 10:
            	elevation_avg.pop(0)
            	
            mean_satellite_count = round(sum(satellite_count_avg) / len(satellite_count_avg), 2)
            print(f"衛星捕捉の平均：{mean_satellite_count}")
            if len(satellite_count_avg) > 10:
            	satellite_count_avg.pop(0)
            	
            mean_x_direction = round(sum(x_direction_avg) / len(x_direction_avg), 2)
            print(f"X方向の平均：{mean_x_direction}")
            if len(x_direction_avg) > 10:
            	x_direction_avg.pop(0)
            	
            mean_y_direction = round(sum(y_direction_avg) / len(y_direction_avg), 2)
            print(f"Y方向の平均：{mean_y_direction}")
            if len(y_direction_avg) > 10:
            	y_direction_avg.pop(0)
            	
            mean_z_direction = round(sum(z_direction_avg) / len(z_direction_avg), 2)
            print(f"Z方向の平均：{mean_z_direction}")
            if len(z_direction_avg) > 10:
            	z_direction_avg.pop(0)
            
            
            # insert_climate_data(mean_tempture, mean_humidity, mean_pressure, mean_latitude, mean_longitude,
            # mean_elevation, mean_satellite_count, mean_x_direction, mean_y_direction, mean_z_direction)
            
            if datetime.now() >= target_time and not function_executed:
            	insert_climate_data(mean_tempture, mean_humidity, mean_pressure, mean_latitude, mean_longitude,
            	mean_elevation, mean_satellite_count, mean_x_direction, mean_y_direction, mean_z_direction)
            	print("")
            	print("**********処理実行**********")
            	print("")
            	function_executed = True
            		
            current_time = datetime.now()		
            if current_time.minute == 0 and current_time.second == 0:
            	insert_climate_data(mean_tempture, mean_humidity, mean_pressure, mean_latitude, mean_longitude,
            	mean_elevation, mean_satellite_count, mean_x_direction, mean_y_direction, mean_z_direction)
            
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
