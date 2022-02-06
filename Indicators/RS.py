import json as json
import time
import datetime
import numpy
from websocket import create_connection
import sys
import Requests
sys.path.insert(1,'/home/pi/iza')
import talib

def RSI(prices):
	#time.sleep(5)
	#print(Candles)
	
	if type(prices) == list:

		RSI = 0
		Sum = 0
		x = 199

		#print(prices)

		if type(prices) == list and prices != None and prices[0] != [] :

			Sum = numpy.arange(200, dtype = 'float64')

			for i in range(200):

				Sum[i] = prices[0][x]
				x-=1
					#Up+=(0)

		#RSI = 100 * AvgUp / (AvgUp+AvgDown)
		RSI = talib.RSI(Sum,14)
		#print("RSI", round(RSI[len(RSI)-1]),2)
		return(RSI)
