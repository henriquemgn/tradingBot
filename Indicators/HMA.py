import math
from Indicators import LWMA

def HMA(closes,period):
	i = 0
	raw_HMA = []
	for i in range(math.floor(math.sqrt(period))):
		raw_HMA.append((2 * LWMA.calculate_lwma(closes[0+i:],math.floor(period/2))) - LWMA.calculate_lwma(closes[0+i:],period))
	
	HMA = LWMA.calculate_lwma(raw_HMA,math.floor(math.sqrt(period)))
	return HMA
	
def HMAavg(HMAdec,count):
	try:
		if HMAdec[1]!=0:
			avgWin = (HMAdec[0])/(count)
		else:
			avgWin = 0

		if HMAdec[3]!=0:
			avgLoss = (HMAdec[2])/(count)
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

def HMApoints(value, HMA, multiplier):
	if ((((value/HMA)-1)*24)*multiplier) > 1:
		return 1
	elif ((((value/HMA)-1)*24)*multiplier) < -1:
		return (-1)
	else:
		return ((((value/HMA)-1)*24)*multiplier)

def HMAsimply(HMA,prices,currentValue):

	winCounter = 0
	winAmount = 0
	lossCounter = 0
	lossAmount = 0
	counter = 1
	multiplier = 1
	if HMA > currentValue:
		while True:
			if HMA < prices[counter] and multiplier > 0.29:
				winCounter += 1
				winAmount += HMApoints(currentValue,HMA, multiplier)
				break
			elif multiplier <= 0.29:
				winCounter +=1
				winAmount += HMApoints(currentValue, HMA, multiplier)
				break
			elif multiplier >= 0.9:
				counter +=1
				multiplier -= 0.075
			elif multiplier < 0.9:
				counter += 1
				multiplier -= 0.05
	else:
		while True:
			if HMA > prices[counter] and multiplier >0.29:
				lossCounter += 1
				lossAmount += HMApoints(currentValue, HMA, multiplier)
				break
			elif multiplier <= 0.29:
				lossCounter += 1
				lossAmount += HMApoints(currentValue, HMA, multiplier)
				break
			elif multiplier >= 0.9:
				counter +=1
				multiplier -= 0.075
			elif multiplier < 0.9:
				counter += 1
				multiplier -= 0.05

	return winCounter,lossCounter,winAmount,lossAmount

def HMAdec(opens,closes,currentValue):

	totalWin = 0
	totalLoss = 0
	countWin = 0
	countLoss = 0
	HMAS = []
	HMAsimplys = 0
	count = 70
	x = 3
	while x < (count):
		HMAS.append(HMA(closes,x))
		x+=1
	for i in range(len(HMAS)):
		HMAsimplys=list(HMAsimply(HMAS[i],closes,currentValue))
		countWin+=HMAsimplys[0]
		countLoss+=HMAsimplys[1]
		totalWin+=HMAsimplys[2]
		totalLoss+=HMAsimplys[3]

	
	return(totalWin,countWin,totalLoss,countLoss,i)
