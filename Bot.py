import json, time, hmac, base64, rsa, AuthConnect, Requests, timeit, talib

from soldatdb import soldatdb
from Indicators import SMA, RS, Variance, BB, BuyAmount, WaveCatch, Ichimoku,output,EMA,HMA
from AuthChannels import Balance,checkorders
from base64 import b64encode, b64decode
from websocket import create_connection
from datetime import datetime
from Strats import Strategy1, Strat

import pandas as pd
import math
import sys
sys.path.insert(1,'/home/pi/iza/PublicChannel')
import Candles, HistoryCandles, Trades

PaperBalance = 500

ws = create_connection("wss://api-pub.bitfinex.com/ws/2")
time.sleep(1)
ws_auth = create_connection("wss://api.bitfinex.com/ws/2")
time.sleep(1)
VarianceTest = 0

milliseconds = (int(round(time.time() * 1000))/1000)

AuthConnect.ConnectAuth(ws_auth)
time.sleep(1)
Requests.RequestBalance(ws_auth)
time.sleep(1)
timeComparator = [0,0]

Requests.RequestCandles(ws)
time.sleep(1)
prices = list(HistoryCandles.History(ws))
time.sleep(1)
BalanceValues=[]

AboveOne = 0
Wave=0
WaveCut=0
Strategy = 0

counterSL = 0
previousStop = [0,0]
pricesUpdatable = 0

CheckPosition = 0

timeStop = -1
points = 0

decisionSMA = 0

IchimokuC = [0,0]
conversionLine = 0
baseLine = 1
pastConv = 0
convList = 0
pastBase = 0
baseList = 0

DataPast = prices
DataOpen = 0
DataClose = 0

BalanceBTC = 0.0
BalanceUSD = 0.0
BalanceWallet = 0.0

while True:
	while True:
		for count in range(300):
			if count == 299 or count == 100 or count == 200:
				try:
					fullRequest = Requests.connect300()
					ws = fullRequest[0]
					ws_auth =fullRequest[1]

					AuthConnect.ConnectAuth(ws_auth)
					time.sleep(1)
					Requests.RequestBalance(ws_auth)
					time.sleep(1)
					Requests.RequestCandles(ws)
					time.sleep(1)
					prices = list(HistoryCandles.History(ws))
					time.sleep(1)

					DataPast = prices
					DataOpen = 0
					DataClose = 0
				except:
					break
			start_time = time.time() ####TIME TO RUN
			print("\n---------- Bitcoin/USD ----------\n")
##############################################################
			#BALANCE
			if BalanceUSD == 0 or BalanceBTC == 0:
				print("Updating Balance...\n")
				BalanceValues=[]
				Balances = Balance.balanceCheck(BalanceUSD,BalanceBTC,CheckPosition,BalanceValues,BalanceWallet,ws_auth)
				BalanceUSD = Balances[0]
				BalanceBTC = Balances[1]
				CheckPosition = Balances[2]
				BalanceValues = Balances[3]
				BalanceWallet = Balances[4]

			print(checkorders.active_orders(ws_auth))
##############################################################
			#Indicators

			SMAv = SMA.SMA(prices,14)
			SMA20 = SMA.SMA(prices,20)[0]
			
			UpperBB = BB.BollingerBands(SMAv)[0]
			LowerBB = BB.BollingerBands(SMAv)[1]
			#BBindex = BollingerIndex(UpperBB,LowerBB,SMAv,closePrices[0])

			RSI = list(RS.RSI(prices))
			print("RSI: ", RSI[len(RSI)-3])

			VolumeAvg = BuyAmount.BA(DataPast[2])
##############################################################
			time.sleep(1)


			if CheckPosition == 1:
				print("\nPosition: SOLD\n")
			else:
				print("\nPosition Bought\n")
##############################################################
			#Ping
			if (datetime.now().minute % 10 == 1) and datetime.now().second == 00:
				Requests.pinging(ws)

##############################################################

			#UPDATE
			try:
				HistoryCandles.updateHistory(ws,prices,timeComparator, DataOpen,DataClose)
				time.sleep(1)
			except:
				continue

			closePrices = prices[0]
			openPrices = prices[1]
			volumes = prices[2]
			highPrices = prices[3]
			lowPrices = prices[4]
			ta_serie = pd.DataFrame({
				'high':highPrices,
				'open':openPrices,
				'close':closePrices,
				'low':lowPrices
					})
			real = talib.SAR(ta_serie.high.values, ta_serie.low.values, acceleration=0.0002, maximum=0.2)
			HMA36 = HMA.HMA(closePrices,60)
			IchimokuCloudA = []
			IchimokuCloudB = []
			Ichimoku.IchimokuCloud(highPrices,lowPrices, IchimokuCloudA, IchimokuCloudB)
			
			leadingA = Ichimoku.IchimokuCloud(highPrices,lowPrices, IchimokuCloudA, IchimokuCloudB)[0]
			leadingB = Ichimoku.IchimokuCloud(highPrices,lowPrices, IchimokuCloudA, IchimokuCloudB)[1]

			conversionLine = Ichimoku.IchimokuCloud(highPrices,lowPrices, IchimokuCloudA, IchimokuCloudB)[2]

			baseLine = Ichimoku.IchimokuCloud(highPrices,lowPrices, IchimokuCloudA, IchimokuCloudB)[3]
			decisionIchi = (Ichimoku.convBase(conversionLine,baseLine,closePrices[0]))
			decisionCloud = Ichimoku.cloudIndex(closePrices[0],leadingA, leadingB)
			HMAdec = HMA.HMAdec(openPrices,closePrices,closePrices[0])
			SMAdec = SMA.SMAdec(openPrices,closePrices,closePrices[0])
			decisionHMA = HMA.HMAavg(list(HMAdec),HMAdec[4])
			
			SMA100 = SMA.SMA(prices,100)[0]

			decisionSMA = SMA.SMAavg(list(SMAdec),SMAdec[4])
			laggingIndex = Ichimoku.laggingIndex(closePrices)

			finalDecision = output.decisions(decisionHMA , (decisionIchi) , decisionCloud , laggingIndex)

			output.balances(BalanceBTC,BalanceUSD,BalanceWallet)

			print("\\\\\\")
			print("Final Decision ( has to be smaller than -0,15 ): ", finalDecision)
			print("Is Final Decision smaller than -0,15: ", finalDecision<(-0.15))
			print("Is SMA100 Bigger than CurrentPrice: ", SMA100>closePrices[0])
			print("Is Past RSI > 50: ", RSI[len(RSI)-3]>50)
			print("\\\\\\")
			
		###
		#algo was here
		###

			time.sleep(1)
			
			if soldatdb.checkEmpty() == 1:
				print("Empty")
			else:
				SoldAt = soldatdb.formatSold(soldatdb.getSold())

			if BalanceUSD > 100:
			    CheckPosition = 1

			
		###########################################
		# STRATEGY = 0     BREAK  ---- No Change in current Position
		# STRATEGY = 1	   COMMAND TO SELL IF NOT SOLD - - COMMAND TO CHECK STOP LOSS IF ALREADY SOLD
		###########################################
			if Strategy == 1 or CheckPosition == 1:

					#also part of the strategy

				VarianceTest +=1

				if (BalanceBTC != 0 and BalanceUSD <10)  and CheckPosition == 0 :
					CheckPosition = 1

					if VolumeAvg < BalanceBTC:
						Requests.newOrder(ws_auth, VolumeAvg*(-1), (closePrices[0]-50)) 
						time.sleep(3)
						
					else:
						Requests.newOrder(ws_auth, BalanceBTC*(-1), (closePrices[0]-50))
						time.sleep(3)

					soldatdb.insertSold(closePrices[0])
					SoldAt = soldatdb.formatSold(soldatdb.getSold())

					PastBalanceBTC = BalanceBTC
					PastBalanceUSD = BalanceUSD
					
					BalanceUSD = math.floor(BalanceBTC*(closePrices[0]))
					BalanceBTC = 0.0000000001

				elif SoldAt != 0 and CheckPosition == 1: #another part of strategy was here

					counterSL=0

					Requests.newOrder(ws_auth, (BalanceUSD/(closePrices[0]+50)), (closePrices[0]+50))
					
					time.sleep(1)
					
					previousStop = [0,0]
					VarianceTest = 0
					PastBalanceBTC = BalanceBTC
					PastBalanceUSD = BalanceUSD

					BalanceBTC = (BalanceUSD/closePrices[0])
					BalanceUSD = 0.000001

					Strategy = 0
					CheckPosition = 0

					soldatdb.removeSold()
					SoldAt = 9999999

				else:
					print("real: ", real[1])
		########################################

			print ("\nMy program took", time.time() - start_time, "to run")
			print("\n-------------------------------\n")
	try:
		ws = create_connection("wss://api-pub.bitfinex.com/ws/2")
		ws_auth = create_connection("wss://api.bitfinex.com/ws/2")	
		ws.close()
		ws_auth.close()
		ws = create_connection("wss://api-pub.bitfinex.com/ws/2")
		ws_auth = create_connection("wss://api.bitfinex.com/ws/2")
		
		AuthConnect.ConnectAuth(ws_auth)
		Requests.RequestBalance(ws_auth)
		Requests.RequestCandles(ws) 
	except:
		continue
