from Indicators import SMA

def calculate_ema(opening_prices ,closing_prices, period):

    previous_EMA = SMA.SMA(opening_prices, closing_prices , period)[0]
    constant = (2 / (period + 1))
    current_EMA = (closing_prices[0] * (2 / (1 + period))) + (previous_EMA * (1 - (2 / (1 + period))))
    return (current_EMA)
    
def EMAavg(EMAdec,count):
	try:
		if EMAdec[1]!=0:
			avgWin = (EMAdec[0])/(count)
		else:
			avgWin = 0

		if EMAdec[3]!=0:
			avgLoss = (EMAdec[2])/(count)
		else:
			avgLoss = 0

		    
		result =((avgLoss+avgWin))

		if result <= (-1):
			result = (-1)
		if result >= 1:
			result = 1

		return ((result) )
	except:
		return 0

def EMApoints(value, EMA, multiplier):
	if ((((value/EMA)-1)*24)*multiplier) > 1:
		return 1
	elif ((((value/EMA)-1)*24)*multiplier) < -1:
		return (-1)
	else:
		return ((((value/EMA)-1)*24)*multiplier)

def EMAsimply(EMA,prices,currentValue):

	winCounter = 0
	winAmount = 0
	lossCounter = 0
	lossAmount = 0
	counter = 1
	multiplier = 1
	if EMA > currentValue:
		while True:
			if EMA < prices[counter] and multiplier > 0.29:
				winCounter += 1
				winAmount += EMApoints(currentValue,EMA, multiplier)
				break
			elif multiplier <= 0.29:
				winCounter +=1
				winAmount += EMApoints(currentValue, EMA, multiplier)
				break
			elif multiplier >= 0.9:
				counter +=1
				multiplier -= 0.05
			elif multiplier < 0.9:
				counter += 1
				multiplier -= 0.025
	else:
		while True:
			if EMA > prices[counter] and multiplier >0.29:
				lossCounter += 1
				lossAmount += EMApoints(currentValue, EMA, multiplier)
				break
			elif multiplier <= 0.29:
				lossCounter += 1
				lossAmount += EMApoints(currentValue, EMA, multiplier)
				break
			elif multiplier >= 0.9:
				counter +=1
				multiplier -= 0.05
			elif multiplier < 0.9:
				counter += 1
				multiplier -= 0.025

	return winCounter,lossCounter,winAmount,lossAmount

def EMAdec(opens,closes,currentValue):

	totalWin = 0
	totalLoss = 0
	countWin = 0
	countLoss = 0
	EMAS = []
	EMAsimplys = 0
	count = 101
	x = 3
	while x < (count):
		EMAS.append(calculate_ema(opens,closes,x))
		x+=1
	for i in range(len(EMAS)):
		EMAsimplys=list(EMAsimply(EMAS[i],closes,currentValue))
		countWin+=EMAsimplys[0]
		countLoss+=EMAsimplys[1]
		totalWin+=EMAsimplys[2]
		totalLoss+=EMAsimplys[3]

	
	return(totalWin,countWin,totalLoss,countLoss,i)
