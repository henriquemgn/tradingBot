import hmac, hashlib, base64, rsa, json, time
from websocket import create_connection
from base64 import b64encode, b64decode

cid = int(round(time.time() * 1000))

def GetChId(ws, result):
	if(type(result) == dict and ("key" in result)):
		#print(result)
		ChanId = result["chanId"]
		return ChanId
	else:
		return "pass"

def RequestCandles(ws):
	ws.send(json.dumps({
    	"event":"subscribe",
    	"channel":"candles",
    	"key":"trade:1h:tBTCUSD"
	}))
	time.sleep(1)
	#print("Candles Subscribed")

def RequestTrades(ws):
	ws.send(json.dumps({
    	"event":"subscribe",
    	"channel":"trades",
    	"symbol":"tBTCUSD"
	}))
	time.sleep(1)
	print("Trades Subscribed")

def RequestBalance(ws_auth):
	ws_auth.send(json.dumps({
    	"event":"auth",
    	"symbol":"tBTCUSD",
    	"type":"exchange"
    	}))
	time.sleep(1)
	#print("Balance Subscribed")

def Unsub(ws, channelId):

	#print(chId)
	ws.send(json.dumps({
		"event":"unsubscribe",
		"chanId":channelId
		}))
	time.sleep(1)

def Ping(ws):

	result = ws.recv()
	result = json.loads(result)
	time.sleep(1)
	print("Pinging...")
	ws.send(json.dumps(
		{
   		"event":"ping",
   		"cid": 1234
		}))
	time.sleep(1)
	print("Connected")
	#print("Unsubscribed to History")

def newOrder(ws_auth, amount, price):
	time.sleep(1)
	order = (
	  {
	  	"cid":	cid,
	    "type": 'EXCHANGE LIMIT',
	    "symbol": 'tBTCUSD',
	    "amount": str(amount),
	    "price": str(price)
	  }
	)

	orderPayload = [0,'on',None,order]
	ws_auth.send(json.dumps(orderPayload))
	time.sleep(1)

def connect300():
	ws = create_connection("wss://api-pub.bitfinex.com/ws/2")
	time.sleep(1)
	ws_auth = create_connection("wss://api.bitfinex.com/ws/2")
	time.sleep(1)
	ws.close()
	time.sleep(1)
	ws_auth.close()
	time.sleep(1)
	ws = create_connection("wss://api-pub.bitfinex.com/ws/2")
	time.sleep(1)
	ws_auth = create_connection("wss://api.bitfinex.com/ws/2")
	time.sleep(1)

	return ws,ws_auth

def pinging(ws):
	print("\nPinging\n")
	Ping(ws)
	time.sleep(1)
	print("OK\n")
