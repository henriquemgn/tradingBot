from datetime import datetime

def IchimokuCloud(high,low,IchimokuCloudA,IchimokuCloudB):
	IchimokuCloudA = []
	IchimokuCloudB = []
	conversion = []
	base = []
	zeto = 26
	while zeto >= 0:
		period9High = 0
		period9Low = 0
			
		period26High = 0
		period26Low = 0
			
		period52High = 0
		period52Low = 0

		for i in range(9):
			if high[i+zeto] > period9High:
				period9High = high[i+zeto]
			if low[i+zeto] < period9Low or period9Low == 0:
				period9Low = low[i+zeto]

		for x in range (26):
			if high[x+zeto] > period26High:
				period26High = high[x+zeto]
			if low[x+zeto] < period26Low or period26Low == 0:
				period26Low = low[x+zeto]

		for y in range (52):
			if high[y+zeto] > period52High:
				period52High = high[y+zeto]
			if low[y+zeto] < period52Low or period52Low == 0:
				period52Low = low[y+zeto]
		
		conversionLine = (period9High + period9Low) / 2
		baseLine = (period26High + period26Low) / 2
		
		leadingSpanA = (conversionLine + baseLine) / 2
		leadingSpanB = (period52High + period52Low) / 2


		IchimokuCloudA.append(leadingSpanA)
		IchimokuCloudB.append(leadingSpanB)

		if IchimokuCloudA[0] == 0:
			IchimokuCloudA.remove(0)
		if IchimokuCloudB[0] == 0:
			IchimokuCloudB.remove(0)
		zeto -= 1
	return IchimokuCloudA, IchimokuCloudB,conversionLine,baseLine


def convBase(conversionLine, baseLine, currentValue):

	if conversionLine > currentValue :
		cv =0 #win15*30

	else:
		cv = 0 #loss


	if conversionLine < baseLine:
		cb = ((conversionLine/baseLine))-1	 #win

	else:
		cb = ((conversionLine/baseLine)-1) #loss


	final = (cb + cv) *50

	if final > 1:
		final = 1
	if final < (-1):
		final = (-1)


	return final

def cloudIndex(currentValue,IchimokuCloudA, IchimokuCloudB):
    wins = 0.001
    lenofwins = 0
    losses = 0.001
    lenoflosses = 0

    for i in range(10):

        if IchimokuCloudA[i] > IchimokuCloudB[i] and currentValue > IchimokuCloudA[i]:
            losses += ((IchimokuCloudA[i]/IchimokuCloudB[i])-1)
            lenoflosses+=1
            
        elif IchimokuCloudB[i] > IchimokuCloudA[i] and currentValue > IchimokuCloudB[i]:
        	losses += (((IchimokuCloudB[i]/IchimokuCloudA[i])-1)/2)
        	lenoflosses+=1
        elif IchimokuCloudA[i] > IchimokuCloudB[i] and currentValue < IchimokuCloudB[i]:
            wins += ((((IchimokuCloudA[i]/IchimokuCloudB[i])-1) / 2) * (-1))
        else:
            wins += ((IchimokuCloudA[i]/IchimokuCloudB[i])-1)
            lenofwins+=1
    
    if lenoflosses == 0:
        final = (wins/11)*64
    elif lenofwins ==0:
        final = (losses/11) * 64
    else:
        final = ((losses/11) + (wins/11) / 2) * 64

        
    #if IchimokuCloudA[i] >= IchimokuCloudB[i] and currentValue > IchimokuCloudA[i]:
    #    final += (((currentValue/IchimokuCloudA[0])-1)*(-1)) * 4
            
    #elif IchimokuCloudB[i] > IchimokuCloudA[i] and currentValue > IchimokuCloudB[i]:
    #    final += (((currentValue/IchimokuCloudB[0])-1)*(-1)) * 8

    #elif IchimokuCloudA[i] >= IchimokuCloudB[i] and currentValue < IchimokuCloudB[i]:
    #    final += (((IchimokuCloudB[0]/currentValue)-1) * 8)
    #else:
    #    final += (((IchimokuCloudA[0]/currentValue)-1) * 4)
          
    if final > 1:
        final = 1
    if final < (-1):
        final = (-1)

    return final

def laggingIndex(closePrices):

    avgLag = (closePrices[26]+closePrices[27]+ closePrices[28]) / 3

    if closePrices[0] > avgLag:
        if closePrices[1] < closePrices[27] or closePrices[2] < closePrices[28] or closePrices[3] < closePrices[29]:
            laggingIndex = (closePrices[0]/avgLag - 1) *(28)#* (2**4)
        elif closePrices[4] < closePrices[30] or closePrices[5] < closePrices[31]:
            laggingIndex = (closePrices[0]/avgLag - 1) *(20)
        else:
            laggingIndex = (closePrices[0]/avgLag - 1) *10
    else:
        if closePrices[1] > closePrices[27] or closePrices[2] > closePrices[28]:
            laggingIndex = (closePrices[0]/avgLag - 1) *(50)#* (2**4)
        elif closePrices[3] > closePrices[29] or closePrices[4] > closePrices[30] or closePrices[5] > closePrices[31]:
            laggingIndex = (closePrices[0]/avgLag - 1) *(32)
        else:
            laggingIndex = (closePrices[0]/avgLag - 1) *16

    if laggingIndex > 0:
        laggingIndex = laggingIndex

    if laggingIndex < 0:
        laggingIndex = laggingIndex


    if laggingIndex > 1:
        laggingIndex = 1
    elif laggingIndex < (-1):
        laggingIndex= (-1)

    return laggingIndex
