
def summariseGroupAverage(inputData , indexNumber):
	totalCountPositive = 0 
	positiveCount = 0
	for patternItem in inputData:
		#print("PatternItem: ", patternItem)
		(dataSample,dataSampleAvg)  = patternItem
		# Check the item is available.
		assert indexNumber < len(dataSampleAvg), 'Item not in data set'
		
		# Pass down the item to average it's numbers.
		averageDataSampleSet = dataSampleAvg[indexNumber]
		#print("Totals: ",averageDataSampleSet )
		
		
		for inputNumber in averageDataSampleSet:
			if inputNumber > 0:
				totalCountPositive += inputNumber
				positiveCount += 1
				
	# For this dataset feed in the average.
	positiveAverage = 0
	if positiveCount > 0 and totalCountPositive > 0:
		positiveAverage = int( totalCountPositive / positiveCount )
		print("AverageNumber:", positiveAverage , 'Index Number:' ,indexNumber )
			
		#break
