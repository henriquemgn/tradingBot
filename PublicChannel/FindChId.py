import hmac, hashlib, base64, rsa, json, time
from websocket import create_connection
from base64 import b64encode, b64decode


def ChannelId(ws)
	result = ws.recv()
	time.sleep(1)
	if result[result.find("subscribed"):result.find("subscribed")+10] == "subscribed":
		chId = result[result.find("chanId")+8:result.find("chanId")+13]
		print(result)
		print(result[result.find("subscribed"):result.find("subscribed")+10])
		print("foi: ", chId)