import json
import time
import datetime
from websocket import create_connection
import sys

def VarianceStop(closePrices, previousStop, counterSL):
	#if Variance > 150:
	#	Variance = SumVariance/20
	if counterSL==1:
		Stop = closePrices[0] + (closePrices[1] * 4/100)
	if counterSL==2:
		Stop = closePrices[0] + (closePrices[1] * 3.5/100)
	if counterSL==3:
		Stop = closePrices[0] + (closePrices[1] * 3.25/100)
	if counterSL==4:
		Stop = closePrices[0] + (closePrices[1] * 3/100)
	if counterSL==5:
		Stop = closePrices[0] + (closePrices[1] * 2.75/100)
	if counterSL==6:
		Stop = closePrices[0] + (closePrices[1] * 2.5/100)
	if counterSL==7:
		Stop = closePrices[0] + (closePrices[1] * 2/100)
	if counterSL==8:
		Stop = closePrices[0] + (closePrices[1] * 1.75/100)
	if counterSL==9:
		Stop = closePrices[0] + (closePrices[1] * 1.5/100)
	if counterSL==10:
		Stop = closePrices[0] + (closePrices[1] * 1.25/100)
	if counterSL==11:
		Stop = closePrices[0] + (closePrices[1] * 1/100)
	if counterSL==12:
		Stop = closePrices[0] + (closePrices[1] * 0.75/100)
	if counterSL==13:
		Stop = closePrices[0] + (closePrices[1] * 0.5/100)
	if counterSL>=14:
		Stop = closePrices[0] + (closePrices[1] * 0.3/100)

	if counterSL <=0:
		Stop = closePrices[0] + (closePrices[1] * 4/100)

	if previousStop < Stop and previousStop != 0:
		return(previousStop,counterSL)

	elif Stop <= previousStop:
		return Stop,counterSL

	elif previousStop == 0:
		previousStop = Stop
		return Stop,counterSL	
