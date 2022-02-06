import json
import time
import datetime
from websocket import create_connection
import sys
import math

def BollingerBands(SMA):
	SimpleMovingAverage = SMA[0]
	ClosedValues = SMA[1][1]
	Sum = 0
	MeanAvg = 0

	for i in range(14):
		Sum += ClosedValues[i]

	MeanAvg = Sum/14
	SumVar = 0

	for j in range(14):
		SumVar += (ClosedValues[j] - MeanAvg)**2

	SD = math.sqrt(SumVar/14)

	LowerBB = SimpleMovingAverage - (SD*2)
	UpperBB = SimpleMovingAverage + (SD*2)

	return(UpperBB,LowerBB)

def BollingerIndex(UpperBB,LowerBB,SMA,currentPrice):
	lengthBBand = UpperBB-LowerBB # 
	rawIndex = currentPrice-LowerBB #Index has to be bigger than 0.75
	Index = rawIndex/lengthBBand

	if Index > 0.75:
		return 1	
