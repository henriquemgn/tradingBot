import json
import time
import datetime
from websocket import create_connection

import sys
sys.path.insert(1,'/home/pi/iza')

import Requests

def TradeValue(ws):
    #print("pass")
    #Requests.RequestTrades(ws)
    for repeat in range(4):
        try:
            result = ws.recv()
            time.sleep(1)
            result = json.loads(result)
            time.sleep(1)
        except:
            currentTrade = []

            if len(result) > 2 and len(result) < 10 and type(result) == list:
        	   #time to actual readable time
                time_in_ms = result[2][1]
                amount = result[2][2]
                dt = datetime.datetime.fromtimestamp(time_in_ms / 1000.0, tz=datetime.timezone.utc)

           	#price
                price = result[2][3]
            	#amounts
                if amount >= 0:
                    print (dt, "\nAmount Bought: ", amount, "\nPrice: ", price, "\n")
                    currentTrade.append(amount)
                    currentTrade.append(price)
                else:
                    print (dt, "\nAmount Sold: ", amount, "\nPrice: ", price, "\n")
                    currentTrade.append(amount)
                    currentTrade.append(price)

            #if Requests.GetChId(ws, result) != "pass":
                #print("test")
            #    Requests.Unsub(ws, Requests.GetChId(ws, result))
            #    Requests.RequestCandles(ws)
            #if(type(result) == dict and ("key" in result)):
                        #print(result)
             #   ChanId = result["chanId"]
                        #print(ChanId)
              #  Requests.UnsubTrades(ws, ChanId)
            else:
                if type(result) == list:
                    if type(result[1]) == list:
                        if type(result[1][0]) == float:
                            return ("sad")

                if Requests.GetChId(ws, result) != "pass":
                    print("test")
                    Requests.Unsub(ws, Requests.GetChId(ws, result))
            #print(currentTrade)
            
            #if currentTrade != []:  
            #    if Requests.GetChId(ws, result) != "pass":
                    #print("test")
             #       Requests.Unsub(ws, Requests.GetChId(ws, result))  
                #print(currentTrade)   
          #  return(currentTrade)
