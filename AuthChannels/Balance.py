import hmac, hashlib, base64, rsa, time, sys
import json as json
sys.path.insert(1,'/home/pi/iza')
import Requests
from base64 import b64encode, b64decode

def Balance(ws_auth, BalanceValues):
	try:
		time.sleep(1)
		result = ws_auth.recv()
		time.sleep(1)
		result = json.loads(result)
	except:
		return BalanceValues

	time.sleep(1)
	i = 0
	BalanceValues = []
	if type(result) == list and (result[1] == 'wu' or result[1] == 'bu'):
			
		if ( (result[1] == 'wu') and ((type(result[2])) == list)) and result[2][1] == "BTC":
			#print("Currency: ", result[2][1], "\nBalance: ", result[2][2], "\nBalance Available", result[2][4], "\n")
			BalanceValues.append(1)
			BalanceValues.append(result[2][2])
			return BalanceValues

		elif ( (result[1] == 'wu') and ((type(result[2])) == list)) and result[2][1] == "USD":
			#print("Currency: ", result[2][1], "\nBalance: ", result[2][2], "\nBalance Available", result[2][4], "\n")
			BalanceValues.append(2)
			BalanceValues.append(result[2][2])
			return BalanceValues
		elif( result[1] == 'bu' and type(result[2]) == list ):
			#print("Balance Update: ", result[2][0])
			BalanceValues.append(3)
			BalanceValues.append(result[2][0])
			return BalanceValues

		else:
			BalanceValues.append(4)
			BalanceValues.append(4)
			return BalanceValues

def balanceCheck(BalanceUSD, BalanceBTC, CheckPosition,BalanceValues,BalanceWallet,ws_auth):

	if BalanceUSD != 0 or BalanceBTC != 0:

		if (BalanceBTC != 0 and BalanceUSD <100):
			CheckPosition = 0

		elif BalanceUSD > 100:
			CheckPosition = 1

	if BalanceBTC == 0 or BalanceUSD == 0:
		BalanceTest = Balance(ws_auth, BalanceValues)

		if type(BalanceTest) == list:

			if type(BalanceTest[0]) != None:

				if BalanceTest[0] == 1:
					BalanceBTC = float(BalanceTest[1])

				elif BalanceTest[0] == 2:
					BalanceUSD = float(BalanceTest[1])

				elif BalanceTest[0] == 3:
					BalanceWallet = float(BalanceTest[1])

	return(BalanceUSD,BalanceBTC,CheckPosition,BalanceValues,BalanceWallet)
