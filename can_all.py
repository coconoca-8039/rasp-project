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
	humi_upper = can_data[6]
	humi_lower = can_data[7]
	press_upper = can_data[8]
	press_lower = can_data[9]
	
	# tempture
	tempture = (temp_upper << 8) | temp_lower
	if tempture >= 0x8000:
	    tempture -= 0x10000
	tempture = tempture / 100.0
	tempture = f"{tempture}℃"
	
	result.append(tempture)
	
	return result 
	
	
