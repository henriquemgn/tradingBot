
def BA(volumes):

	if type(volumes) == list:

		percentages = []
		Up = 0
		Down = 0
		Sum = 0

		if volumes != None and volumes[0] != [] :

			for i in range(100):

				Sum += volumes[i]
				i+= 1

		#print("Test")
		volumesAvg = 0.1*(Sum/100)

		print("Buyable Amount: ", volumesAvg)
		return(volumesAvg)