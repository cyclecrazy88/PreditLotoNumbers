# -------------------------------------------
#  Def bestBits - Try to figure out which numbers as part of the result
#					are good. Like, factors occur lots of times.
#		ResultData - Input Data
#		minimumAverage - Minimal number of averages required.
#		groupGuessResultAverage - Summary data (List item).
# -------------------------------------------
def bestBits(resultData , minimumAverage ,groupGuessResultAverage):
	#print("Result: ", resultData)
	resultNumbers , inputGuessNumbers = resultData
	# Counter for the current index position. The number of positions
	# in the data set
	indexPosition = -1
	# -----------------------------------
	# For each item in the result. Attempt to find the match
	# percentage. Based on this, position and number it should be
	# possible to take a mass of numbers to calculate the guess.
	# -----------------------------------
	for resultNumber in resultNumbers:
		#print("Number: ", resultNumber )
		# Split the data into a tuple.
		factorCount , count = resultNumber
		
		# Increment the array possition for this index.
		indexPosition += 1
		
		if count == 0:
			continue;
		if factorCount == 0:
			continue;
		
		# Get the average number - Average for the result item
		averageNumber = int((factorCount / count)*100)
		if averageNumber > minimumAverage :
			#print("Average Number: ", averageNumber , 'Index: ',indexPosition ,\
			#			"Number: ",inputGuessNumbers[indexPosition])
						
			# Check the result item is the correct length
			assert indexPosition < len(groupGuessResultAverage) , \
						'Average result data set length too short'	
			groupGuessResultAverage[indexPosition][ inputGuessNumbers[indexPosition] ]\
							= averageNumber	
			
	# Return the result item.
	#print('Guess Item: ',groupGuessResultAverage )
	return groupGuessResultAverage
