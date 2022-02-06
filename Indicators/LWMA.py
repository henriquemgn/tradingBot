
def calculate_lwma(closes,period):
	sum_multipliers = 0
	sum_weights = 0
	for i in range(period):
		sum_multipliers += closes[0+i] * (period-i)
		sum_weights += (period-i)
		
	LWMA = sum_multipliers/sum_weights
	
	return LWMA
