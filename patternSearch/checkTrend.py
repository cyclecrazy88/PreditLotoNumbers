# -----------------------------------------------------
#	Check - checkTrend
#		Check to see if the item is currently
# -----------------------------------------------------
def checkTrend(patternResult , trend , indexNumber ):
	(dataSample,dataSampleAvg)  = patternResult
	lowerLimit = 0
	upperLimit = 0
	if dataSample[indexNumber] > 0:
		lowerLimit -= dataSample[indexNumber]
		upperLimit += dataSample[indexNumber]
	else:
		lowerLimit += dataSample[indexNumber]
		upperLimit -= dataSample[indexNumber]


	
	#print("\n\nInput Sample: ",dataSample)
	#print("Data Sample - Lower Limit: ",lowerLimit , "Upper Limit:" ,upperLimit )
	
	currentTrend = trend[indexNumber]
	#print("Current Trend: ", currentTrend)
	
	if currentTrend > lowerLimit and currentTrend < upperLimit:
		print("Within Trend: ",indexNumber )
		return True
	else:
		print("Currently not within trend",indexNumber )
		return False
