def can_get_0CCC2222(can_data, target):
	"""
	can_data -> can_data
	target -> 指定したID
	
	"""
	
	result = []
	
	xaxis_upper = int(can_data[4], 16)
	xaxis_lower = int(can_data[5], 16)
	yaxis_upper = int(can_data[6], 16)
	yaxis_lower = int(can_data[7], 16)
	zaxis_upper = int(can_data[8], 16)
	zaxis_lower = int(can_data[9], 16)
	
	# X
	xaxis = (xaxis_upper << 8) | xaxis_lower
	xaxis = f"X方向 {xaxis}"
	
	# Y
	yaxis = (yaxis_upper << 8) | yaxis_lower
	yaxis = f"Y方向 {yaxis}"
	
	# Z
	zaxis = (zaxis_upper << 8) | zaxis_lower
	zaxis = f"Z方向 {zaxis}"
	
	# 返り値用に格納
	result.append(xaxis)
	result.append(yaxis)
	result.append(zaxis)

	return result 
