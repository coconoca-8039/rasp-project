def can_get_1888DDDD(can_data, target):
	"""
	can_data -> can_data
	target -> 指定したID
	
	Byte:1 衛星の捕捉数 
	Byte:3~4 標高 
	
	"""
	
	result = []
	
	satellites = int(can_data[4], 16)
	altitude_byte1 = int(can_data[6], 16)
	altitude_byte2 = int(can_data[7], 16)
	
	satellites = f"衛星数：{satellites}"
	
	altitude = (altitude_byte1 << 8) | altitude_byte2
	altitude = altitude / 100
	altitude = f"標高：{altitude}"
	
	result.append(satellites)
	result.append(altitude)
	
	return result
