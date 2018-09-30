from patternSearch.findPattern import loadPattern
# ----------------------------------------------
#	Def - parseRecentPattern
#		Using a decrementing overlay (removing one element)
#		at a time. Try to see if there is a pattern for the 
#		data set over a couple of draws (Is there a 'current'
#		repeat.
# ----------------------------------------------
def parseRecentPattern(numbersIn):
	# Cache the result of the recent pattern.
	lineDataResult = []
	# Loop around the result - Use the range to create
	# an overlay for the pattern. (Looking for reliability
	# in the movement of the results.
	for repeatCount in range(1,len(numbersIn)-5 ):
		# Add the pattern to the result data.
		lineDataResult.append(loadPattern(numbersIn))
		# Decrement the result for the next loop around.
		numbersIn.pop(0)
	# Return a summary of the result.
	return lineDataResult
# -------------------------------------------------
#	Def - summarizePattern
#		For the pattern try to deduce if there is an
#		average 'repeat' time. Well, the average is the
#		middle time for which the movement will probably
#		be increased/decreased in this area.
# -------------------------------------------------
def summarizePattern(patternData, indexNumber):
	lastNumber = None
	currentCount = 0
	sampleLengthArray = []
	for pattern in patternData:
		(dataSample,dataSampleAvg)  = pattern
		positionSample = dataSample[indexNumber]
		#print('Sample Position: ', positionSample)
		if lastNumber == None:
			# Start the count at 1
			currentCount = 1
		else:
			if lastNumber == positionSample:
				currentCount += 1
			else:
				sampleLengthArray.append(currentCount)
				currentCount = 1
		# Set the last number in the sample for the next loop
		# around
		lastNumber = positionSample
		
	# Pick up any samples left at the end.
	if currentCount > 1:
		sampleLengthArray.append(currentCount)
	#print("Data Result: ", sampleLengthArray)
	
	# Now this is an array of numbers. Just find an average to
	# to go with
	quickAverage = 0
	totalCount = 0
	for sampleNumber in sampleLengthArray:
		totalCount += sampleNumber
	if len(sampleLengthArray) > 0 and totalCount > 0:
		quickAverage = int( totalCount / len(sampleLengthArray) )
		#print("Average: ",quickAverage , 'Index: ', indexNumber )
	return quickAverage
