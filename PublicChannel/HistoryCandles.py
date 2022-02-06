import json as json
import time
import datetime
from websocket import create_connection

import sys

sys.path.insert(1,'/home/pi/iza')
import Requests

def History(ws):

#this is cause the first few messages recieved aren't usable
	for j in range(4): 
		try:
			result = ws.recv()
			time.sleep(1)
			result = json.loads(result)
			time.sleep(1)
	#this will calculate the past 100 open and closes candles
			if type(result) == list and type(result[1]) != str and type(result[1][0]) == list:  
				#print(result)
				i=0
				pastClosedPrices = []
				pastOpenPrices = []
				pastHighPrices = []
				pastLowPrices = []
				volumes = []
				while i < len(result[1]):

					if type(result[1][i]) == list and len(result[1][i]) >= 6:

						time_in_ms = result[1][i][0]
						dt = datetime.datetime.fromtimestamp(time_in_ms / 1000.0, tz=datetime.timezone.utc)

						openPrice = result[1][i][1]
						closePrice = result[1][i][2]
						pastClosedPrices.append(closePrice)
						pastOpenPrices.append(openPrice)

						highPrice = result[1][i][3]
						lowPrice = result[1][i][4]
						pastHighPrices.append(highPrice)
						pastLowPrices.append(lowPrice)

						volumes.append(result[1][i][5])

						i+=1
						j+=1
							
					else:
						i+=1
						j+=1

				if pastOpenPrices != []:
					print("")
					return(pastClosedPrices,pastOpenPrices,volumes,pastHighPrices,pastLowPrices)

				j+=1
		except:
			return 0

def updateHistory(ws, prices, timeComparator, DataOpen, DataClose):
	try:
		result = ws.recv()
		result = json.loads(result)
		time.sleep(1)
		if type(prices) == list :
			if type(result) == list:

				if  type(prices) == list and type(prices[0]) == list and type(result[1]) == list:
					nowUtc = datetime.datetime.now(tz = datetime.timezone.utc)
					time_in_ms = result[1][0]

					dt = datetime.datetime.fromtimestamp(time_in_ms / 1000.0, tz=datetime.timezone.utc)

					if dt.hour == nowUtc.hour:
					
						timeComparator.insert(0, time_in_ms)

						if len(timeComparator) > 2:
							timeComparator.pop()

						if (timeComparator[0] != timeComparator[1] or timeComparator[1] != timeComparator[0]) and timeComparator[1] != 0:
						#OPEN PRICES UPDATE

							prices[0][0] = result[1][1]

							prices[2].pop()
							prices[1].pop()
							prices[0].pop()

							prices[1].insert(0, result[1][1])

							#CLOSE PRICES UPDATE
							prices[0].insert(0, result[1][2])

							prices[2].insert(0, result[1][5])

							DataOpen = prices[1][1]
							DataClose =prices[0][1]

							with open('Data.txt', 'a') as f:
								f.write("\n")
								f.write("%d" % DataOpen)
								f.write("\n")
								f.write("%d" % DataClose)
								f.write("\n")

							return prices

						else:
						#OPEN PRICES UPDATE
							
							prices[1][0] = result[1][1]

						#CLOSEPRICESUPDATE
							prices[0][0] = result[1][2]

							return prices
					else:
						return prices
				else:
					return prices
			else:
				return prices
		else:
			return prices
	except:
		return prices
