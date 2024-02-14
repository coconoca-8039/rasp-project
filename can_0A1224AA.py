# 1234ABCD 1から9までの数字をランダムで入れているだけ
# 0A1234AA 気温湿度温度
# 0CCC4444 XYZセンサ

def can_get_0A1224AA(can_data, target):
	"""
	can_data -> can_data
	target -> 指定したID
	
	Byte:1~2 temp 
	Byte:3~4 humidity 
	Byte:5~6 press
	
	"""
	
	result = []
	
	temp_upper = int(can_data[4], 16)
	temp_lower = int(can_data[5], 16)
	humi_upper = int(can_data[6], 16)
	humi_lower = int(can_data[7], 16)
	press_upper = int(can_data[8], 16)
	press_lower = int(can_data[9], 16)
	
	# tempture
	tempture = (temp_upper << 8) | temp_lower
	if tempture >= 0x8000:
	    tempture -= 0x10000
	tempture = tempture / 100.0
	tempture = f"{tempture} ℃"
	
	# humidity
	humidity = (humi_upper << 8) | humi_lower
	if humidity >= 0x8000:
	    humidity -= 0x10000
	humidity = humidity / 100.0
	humidity = f"{humidity} %"
	
	# pressure
	pressure = (press_upper << 8) | press_lower
	if pressure >= 0x8000:
	    pressure -= 0x10000
	pressure = f"{pressure} hPa"
	
	# 返り値用に格納
	result.append(tempture)
	result.append(humidity)
	result.append(pressure)
	
	return result 
	
	
