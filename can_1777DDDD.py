def can_get_1777DDDD(can_data, target):
	"""
	can_data -> can_data
	target -> 指定したID
	
	Byte:1~4 longitude 経度 
	Byte:5~8 latitude 緯度 
	
	"""
	
	result = []
	
	longitude_byte1 = int(can_data[4], 16)
	longitude_byte2 = int(can_data[5], 16)
	longitude_byte3 = int(can_data[6], 16)
	longitude_byte4 = int(can_data[7], 16)
	latitude_byte1 = int(can_data[8], 16)
	latitude_byte2 = int(can_data[9], 16)
	latitude_byte3 = int(can_data[10], 16)
	latitude_byte4 = int(can_data[11], 16)
	
	longitude = (longitude_byte1 << 24) | (longitude_byte2 << 16) | (longitude_byte3 << 8) | longitude_byte4
	longitude = longitude / 1000000
	longitude = f"経度：{longitude}"
	
	latitude = (latitude_byte1 << 24) | (latitude_byte2 << 16) | (latitude_byte3 << 8) | latitude_byte4
	latitude = latitude / 1000000
	latitude = f"緯度：{latitude}"
	
	result.append(longitude)
	result.append(latitude)
	
	return result
