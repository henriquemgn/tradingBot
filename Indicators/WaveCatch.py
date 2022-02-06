def Catch(close, openp):

	SumPercent = 0
	i = 0

	while i < 100:
		i+=1
		if openp[i]>close[i]:
			SumPercent += abs(openp[i] / close[i])
		else:
			SumPercent += abs( close[i]/ openp[i])

	Average = SumPercent/100
	Result = (((((Average-1)*100)*10)/7)/100)+1
	return Result