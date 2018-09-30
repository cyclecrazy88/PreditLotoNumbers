
# ---------------------------------------------------------------
#	Search for a given set of factor data. - 
#	This is an internal function used to get factor data so a 
#	comparision can be made.
# ---------------------------------------------------------------
def getInputItem(passInDataItem , searchIndex):
	#print("Input Data Length: ", len(passInDataItem) , passInDataItem )

	# ---------------------------------------------------------
	# Format the input item data for searching
	# This should be a tupple with factors and input numbers
	# ---------------------------------------------------------
	factorData, inputNumbers = passInDataItem

	#print("\nSearch Index: ",searchIndex , "Input Length: " , len(factorData) )

	# Check the inputs - An assertion is here as it's getting complex around here.
	assert len(factorData)+1 > searchIndex , "Guess index to search is greater than input numbers"
	assert type(searchIndex) is int , "Seach index is not an integer"

	# Try to find the requested data set for the factor items.
	count = 0
	for inputArray in factorData:
		count += 1
		if count == searchIndex:
			#print("Input Numbers Data: ", inputArray)
			return inputArray
	return None

# ---------------------------------------------------------------
# Internal function. Request the number of times a factor has been repeated, None if not present.
# ---------------------------------------------------------------
def itemSetRepeatCountForFactor(itemSetInput, searchFactor):
	'''Lookup number of times this factor has appeared'''
	for item in itemSetInput:
		factorNumber, factorCount = item
		# If the item has been found. Return true to indicate it's occured.
		if searchFactor == factorNumber:
			return True
		
	
	return False

# ---------------------------------------------------------------
# compareFactorItem - Allow a comparision to occur for the numbers guessed and the input numbers
# provided.
# The objective here is to weight up how the factors are looking.
# 
# How similar are the factors in the data set? Are they the same or different?
# ---------------------------------------------------------------
def compareFactorItem(guessNumbers = None , inputNumbersData = None):
	#print("Data Passed In: ",inputNumbersData)
	
	#return
	# ---------------------------------------------------------------
	# Hold onto the guess data. Loop around the items for the guess.
	# ---------------------------------------------------------------
	for guessArray in guessNumbers:
		# This should be a tupple with factors and input numbers
		guessData, inputNumbers = guessArray
		#print("Input Numbers: ",type(inputNumbers) )

		# -----------------------------------------------
		# Check the numbers passed it is a list item.
		# -----------------------------------------------
		assert type(inputNumbers) == list, "Input numbers passed in is not a list item."
		assert type(guessData) == list, "GuessData passed in is not a list item."

		count = 0
		
		# --------------------------------------------------------------
		# Loop around the list for this guess item.
		# --------------------------------------------------------------
		resultItemArray = []
		for guessItem in guessData:
			count+=1
			#print("Guess Item: ",guessItem , "Number Position: ", count)
			resultIndexItemsFound = getInputItem(inputNumbersData , count)

			# Check an expected item has been returned.
			assert resultIndexItemsFound != None , "getInputItem - Should return an item" 
			assert resultIndexItemsFound != list , 'resultIndexItemsFound - Should be a list'
			
			#print("Items Found: ", resultIndexItemsFound)
			itemFoundCount = 0	

			# ---------------------------------------------------
			# Loop around all the factors found
			# Search to find how many matches can be found for the 
			# factor in the data set.
			# ---------------------------------------------------
			for guessFactor in guessItem:
				factorNumber, factorCount = guessFactor
				#print("FactorNumber: ", factorNumber)
				assert type(factorNumber)==int , "Check if comparision factor number is an int"

				# Have a look to see if this item has been found. Is this a factor of the input
				# data?
				itemFound = itemSetRepeatCountForFactor(resultIndexItemsFound , factorNumber)
				#print("Item Found: ",itemFound)
				assert type(itemFound)==bool , "Check if the item is a factor should be a boolean"

				# If as a factor this number has been found. Log this, add this to the
				# counter.
				if itemFound:
					itemFoundCount += 1
	
			# -------------------------------------------------------------------------
			# Hold onto the number of times occured. Using the count and the factor
			# count. A reasonable guess can be made as to the accuracy of the numbers.
			# -------------------------------------------------------------------------
			resultItemArray.append( {"TimesOccured":itemFoundCount , \
						#"FactorsFound":itemFoundCount, \
						#"FactorsInputLengh":len(guessItem) , \
						"SearchIndex":count} )
			#break
		#print("Result Count Set",resultItemArray)
		return resultItemArray
	# No guess numbers found.
	return None
		

