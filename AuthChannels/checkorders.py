import json
import requests
import time
def active_orders(ws_auth):

	cid = int(round(time.time() * 1000))

	headers = ws_auth

	order = (
	  {
	  	"cid":	cid,
	    "symbol": 'tBTCUSD',
		"trading":"tBTCUSD"
	  }
	)

	#orderPayload = [0,'on',None,order]
	r = ws_auth.send(json.dumps(order))
	time.sleep(1)
	print(r)
	return (r)
