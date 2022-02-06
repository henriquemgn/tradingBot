import json
import time
import datetime
from websocket import create_connection


def CandleValue(ws):
	try:
		result = ws.recv()
		time.sleep(1)
		result = json.loads(result)
		time.sleep(1)
		currentCandle = []
		Requests.RequestTrades(ws)
		time.sleep(1)
		if len(result) <= 3 and type(result) == list and type(result[1][0]) != list and type(result[1]) != str:

			time_in_ms = result[1][0]
			print((datetime.datetime.now().timestamp())*1000)
			print(time_in_ms)
			dt = datetime.datetime.fromtimestamp(time_in_ms / 1000.0, tz=datetime.timezone.utc)
			openPrice = result[1][1]
			closePrice = result[1][2]

			highPrice = result[1][3]
			lowPrice = result[1][4]

			volume = result[1][5]

			currentCandle.append(result[1][1])
			currentCandle.append(result[1][2])
			currentCandle.append(result[1][3])
			currentCandle.append(result[1][4])
			currentCandle.append(result[1][5])

			print(currentCandle)
			print (dt, "\nOpen: ", openPrice, "\nClose: ", closePrice, "\nHigh: ", highPrice, "\nLow: ", lowPrice, "\nVolume: ", volume, "\n")
			return currentCandle
	except:
		return 0