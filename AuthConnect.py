import hmac
import hashlib
import base64
import rsa
from base64 import b64encode, b64decode
import json
import time


#authString = 'AUTH'
def ConnectAuth(ws_auth):

	API_KEY = ""
	API_SECRET = ""

	nonce = str(int(time.time() * 10000))
	auth_string = 'AUTH' + nonce
	auth_sig = hmac.new(API_SECRET.encode(), auth_string.encode(),hashlib.sha384).hexdigest()
	payload = {'event': 'auth', 'apiKey': API_KEY, 'authSig': auth_sig,
            'authPayload': auth_string, 'authNonce': nonce, 'dms': 4}
	ws_auth.send(json.dumps(payload))
	time.sleep(1)
	print("Connected")

#print(ws_auth.recv())
