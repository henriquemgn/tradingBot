import json
import time
import datetime
from websocket import create_connection
import sys

#sys.path.insert(1,'C:/Users/henri/PythonBot/PublicChannel')
#import HistoryCandles


def SMA(prices,size):
	#time.sleep(5)
	Candles = prices
	#print(Candles)
	if type(Candles) == list:
	#print(Candles)
		#print(type(Candles))
		lCandles = Candles
		percentages = []
		Up = 0
		Down = 0
		Sum = 0

		#print(lCandles[0])
		if type(lCandles) == list and lCandles != None and lCandles[0] != [] :

			for i in range(size):

				#diff = lCandles[0][i] - lCandles[1][i]


				Sum += prices[0][i]
				i+= 1

		#print("Test")
		AvgU = Up / size
		AvgD = Down / size
		SMA = Sum/ size


		#print("Small Moving Average: ", round(SMA,1))
		return(SMA, lCandles)

def SMAavg(SMAdec, count):
	try:
		if SMAdec[1]!=0:
			avgWin = (SMAdec[0])/count
		else:
			avgWin = 0

		if SMAdec[3]!=0:
			avgLoss = (SMAdec[2])/count
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

def SMApoints(value, SMA, multiplier):
	if ((((value/SMA)-1)*1)*multiplier) > 1:
		return 1
	elif ((((value/SMA)-1)*1)*multiplier) < -1:
		return (-1)
	else:
		return ((((value/SMA)-1)*1)*multiplier)

def SMAsimply(SMA,prices,currentValue):

	winCounter = 0
	winAmount = 0
	lossCounter = 0
	lossAmount = 0
	counter = 1
	multiplier = 1
	if SMA > currentValue:
		while True:
			if SMA < prices[counter] and multiplier > 0.29:
				winCounter += 1
				winAmount += SMApoints(currentValue,SMA, multiplier)
				break
			elif multiplier <= 0.29:
				winCounter +=1
				winAmount += SMApoints(currentValue, SMA, multiplier)
				break
			elif multiplier >= 0.9:
				counter +=1
				multiplier -= 0.075
			elif multiplier < 0.9:
				counter += 1
				multiplier -= 0.05
	else:
		while True:
			if SMA > prices[counter] and multiplier >0.29:
				lossCounter += 1
				lossAmount += SMApoints(currentValue, SMA, multiplier)
				break
			elif multiplier <= 0.29:
				lossCounter += 1
				lossAmount += SMApoints(currentValue, SMA, multiplier)
				break
			elif multiplier >= 0.9:
				counter +=1
				multiplier -= 0.075
			elif multiplier < 0.9:
				counter += 1
				multiplier -= 0.05
	return winCounter,lossCounter,winAmount,lossAmount

def SMAdec(opens,closes,currentValue):

	totalWin = 0
	totalLoss = 0
	countWin = 0
	countLoss = 0
	SMAS = []
	SMAsimplys = 0
	count = 101
	x = 3
	allPrices = [closes,opens]
	while x < (count):
		SMAS.append(SMA(allPrices,x)[0])
		x+=1
	for i in range(len(SMAS)):
		SMAsimplys=list(SMAsimply(SMAS[i],closes,currentValue))
		countWin+=SMAsimplys[0]
		countLoss+=SMAsimplys[1]
		totalWin+=SMAsimplys[2]
		totalLoss+=SMAsimplys[3]

	
	return(totalWin,countWin,totalLoss,countLoss,i)
