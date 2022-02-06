def decisions(sma,conv,cloud,lag):
	#print("Decision based only on ichimoku conv/base: %.10f"% conv)
	#print("//// UNDER MAINTENANCE //// Decision based only on Ichimoku Cloud: %.10f"% cloud)
	#print("Decision based only on Lagging Index: %.10f"%lag)

	final = (sma)# + (conv*0.15) + (lag*0.25))#) + (cloud*0.3))
	
	if final <= (-0.10):
		print("\nFinal Decision: %.10f"%(final)," SHORT")
	elif final <=0.10 and final > (-0.10):
		print("\nFinal Decision: %.10f"%(final)," HOLD")
	else:
		print("\nFinal Decision: %.10f"%(final)," LONG")

	return final

def balances(BalanceBTC,BalanceUSD,BalanceWallet):
	print("BalanceBTC: ", BalanceBTC)
	print("BalanceUSD: ", BalanceUSD)
	print("BalanceWallet: ", BalanceWallet)
	return 0
