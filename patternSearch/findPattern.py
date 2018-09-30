
numberWeeksBack = 3

# -------------------------------------------------
# Try to load the pattern. Check there are enough
# numbers available to do, search through to see
# what the movement lots like
# -------------------------------------------------
def loadPattern(numbers):
	#print("Numers: ",numbers)
	# Check there are enough numbers to process
	assert len(numbers)>2, "Not enough numbers to process:"+numbers

	weekCount = 0

	dataSample = [0,0,0,0,0,0,0,0,0]
	dataSampleAvg = [ [],[],[],[],[],[],[],[],[] ]
	lastWeeksData = None
	# Loop through the week of numbers
	for numberData in numbers:
		if lastWeeksData == None:
			lastWeeksData = numberData
		else:
			#print("Last Week:",lastWeeksData )
			#print("This week:",numberData)
			
			for indexCount in range(0 , len(numberData) ):
				#print("Number Found", numberData[indexCount])
				if numberData[indexCount] > lastWeeksData[indexCount]:
					#print("Increase")
					dataSample[indexCount]+= 1
					dataSampleAvg[indexCount].append( numberData[indexCount] - lastWeeksData[indexCount] )
				elif numberData[indexCount] == lastWeeksData[indexCount]:
					#print("Same")
					pass
				elif numberData[indexCount] < lastWeeksData[indexCount]:
					#print("Decrease")
					dataSample[indexCount]-= 1
					dataSampleAvg[indexCount].append( numberData[indexCount] - lastWeeksData[indexCount] )
			
		# Put last week into this week now
		lastWeeksData = numberData
		# -----------------------------------------------------------------
		# Don't go to far back this is just a check to see what the current
		# trend is looking like right now.
		# -----------------------------------------------------------------
		if weekCount > numberWeeksBack:
			break
		weekCount+= 1
	#print("Movement Result: ", dataSample)
	#print("Data Average: ",dataSampleAvg )
	
	# ----------------------------------------------------------
	#   Return a tuple for the result. The data sample, then it's corresponding
	#	averages.
	# ----------------------------------------------------------
	return (dataSample,dataSampleAvg) 
