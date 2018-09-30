
import random

from dataModules.processInputDataSet import processInputDataSet as process
from dataModules.processNumberGuess import prrocessNumberGuess

from guessNumbers.compareFactorItem import compareFactorItem

class guessItemNumber:
	inputProcessData = None
	
	# Hold onto the currentItemNumber
	currentItemNumber = None	
	
	def __init__(self ,  inputProcessData = None):
		if inputProcessData != None:
			#print('Input Data: ', inputProcessData)
			self.inputProcessData = inputProcessData
			self.currentItemNumber = 0
		else:
			raise Exception("GuessNumber - inputProcessData not provided")
	# -----------------------------------------------------------------------------------------------------
	# Caller method - Allow the next available guess to occur/be made.
	# -----------------------------------------------------------------------------------------------------
	def makeNextGuess(self , guessCount = None):
		#print("Def - makeNextGuess - Guess Next Item")
		nextGapSizeNumber  = self.getNextItemFromDataSet()
		#print('GapSize:', nextGapSizeNumber)
		initialNumbers = self.generateInitialNumbers(nextGapSizeNumber ,  1, 5)
		# --------------------------------------------
		#  Calculate the next guess for the item and then process these
		#  input values.
		# --------------------------------------------
		def calculateLocalGuess(inputNumbersGuessed):		
			# Create a array. This will have a length of 0 so this can be used to process lots of data items.
			groupDataItemSet = []
			dataSetManager = process(inputNumbersGuessed)
			processedDataSet = dataSetManager.getResultData()
			groupDataItemSet.append(processedDataSet)
			del dataSetManager	
			# Process the numbers for this guess
			resultingCalcData = prrocessNumberGuess( groupDataItemSet )
			#print(resultingCalcData)
			return resultingCalcData
		aboutResultGuess = calculateLocalGuess(initialNumbers)
		#print('About Guess:',aboutResultGuess)
		# -------------------------------------------
		#  Try to be compare the guess with the input data.
		# -------------------------------------------
		comparisionResult = self.compareGuessItem(aboutResultGuess , guessCount)
		#print('InputNumbers: ', initialNumbers)
		#print("Running Comparision Result: ", comparisionResult)
		return (comparisionResult , initialNumbers)
		



		
	# --------------------------------------------------------------------------------------------------
	# Allow the looping around each data item. The objective here is to discover how closely the factors
	# for the guess relate to the previous number items.
	# - Input Data Item contains all of the known combinations which have been found recently.
	# --------------------------------------------------------------------------------------------------
	def compareGuessItem(self, testGuess , numberItemsBack = None):
		# ----------------------------------------------------
		#   Check the dictionary is an expected shape.
		#
		#   - These factors are calculated in the data modules 
		#   - component.
		# ----------------------------------------------------
		if "factorOutputItemSet" not in self.inputProcessData:
			raise Exception("compareGuessItem - Factor Item Data doesn't contain factors.")
		if "factorOutputItemSet" not in testGuess:
			raise Exception("compareGuessItem - Factor Item for guess doesn't contain factors.")
		
		# Create an empty data item for the running totals item.
		runningTotalsItem = [(0,0),(0,0),(0,0),(0,0),(0,0)]

		runningCount = 0

		# -----------------------------------------------------------------
		#	Loop Compare the result.
		#
		# Loop around and fetch the corresponding items from the data set.
		# -----------------------------------------------------------------
		for inputItemData in self.inputProcessData["factorOutputItemSet"]:
			# -----------------------------------------------------------
			# Allow the comparision to be a running change. We don't need
			# everything. Just something recent.
			# If the number of items is well, not provide as a maximum just keep going.
			# -----------------------------------------------------------
			if numberItemsBack != None and \
				runningCount >= numberItemsBack:
				break
			# Increment the counter.
			runningCount += 1
			#print("Current Count: ", runningCount)
			# -----------------------------------------------------------
			# Each item contains the (factor,count). So factor and number 
			# of times it's occured.
			# -----------------------------------------------------------
			#print('Guess Item: ', testGuess["factorOutputItemSet"])
			#print('Compare Item: ', inputItemData)
			
			# Compare item for the guess. Test the guess against the item
			dataComparision = compareFactorItem( testGuess["factorOutputItemSet"] , inputItemData )

			# Check the result data is a list
			assert type(dataComparision)== list, "Returned comparison data should be a list."
			runningTotalsItem = self.processComparsionData(dataComparision , runningTotalsItem)
			#print("Running Total Item: ",runningTotalsItem)
			#break
		# ----------------------------------------
		# Running count item.
		# ----------------------------------------
		return runningTotalsItem
			
	# ---------------------------------------------------------------------------		
	# Handler function to look at the comparision data and recommend adjustments where needed to the guess.
	#
	#	Using the two data sets the input and the guess. Attempt to make a comparision
	#   for the item data.
	# ---------------------------------------------------------------------------
	def processComparsionData(self , inputData , runningTotalsItem):
		for compareData in inputData:
			#print(compareData)
			assert "SearchIndex" in compareData , "Search index number should be available"		
			assert "TimesOccured" in compareData , "Factor difference number should be available"
			assert type(compareData["SearchIndex"]) == int , "Search index should be a number"
			assert type(compareData["TimesOccured"]) == int , "Factor difference should be a number"

			factorCount , runningCount = runningTotalsItem[ compareData["SearchIndex"] -1 ]
			factorCount += compareData["TimesOccured"]
			runningCount += compareData["SearchIndex"]
			
			runningTotalsItem[ compareData["SearchIndex"] -1 ] = (factorCount , runningCount)

		return runningTotalsItem
		
	# -----------------------------------------------------------------------------------------------------
	# For each loop around request the next possible gap size number for the number in
	# the data set.
	#
	# This is the average gap size for the input data items.
	# -----------------------------------------------------------------------------------------------------
	def getNextItemFromDataSet(self):
		if 'gapItemDataSet' in self.inputProcessData:
			gapItemDataSetInput = self.inputProcessData['gapItemDataSet']
			
			# If the number is to big then simply flip this back around to the number 0
			if self.currentItemNumber >= len(gapItemDataSetInput):
				# Set this back to 0
				self.currentItemNumber = 0
			
			if self.currentItemNumber < len(gapItemDataSetInput):
				gapSize = gapItemDataSetInput[self.currentItemNumber]
				#print("GapSize", gapSize)
				# Increment the current item nmber
				self.currentItemNumber += 1
				return gapSize
		raise Exception("Unable to find next gap item")
		
	# -------------------------------------------------------------------------
	#  Try to create some random numbers. These will basically make up the next
	#  guess to be made.
	# -------------------------------------------------------------------------	
	def generateInitialNumbers(self ,  gapSize,  startingNumber ,  itemLength):
		outputNumbers = []
		# Hold onto a reference for the starting number
		sizeAdjustment = random.randint(0, gapSize)
		# Using the starting number. Append a random size number to this
		localCount = (startingNumber + sizeAdjustment)
		for count in range(0,itemLength ):
			
			sizeAdjustment = random.randint(0, gapSize)
			
			# Add the gap size to the starting number to create the next number
			localCount += (gapSize + sizeAdjustment)
			outputNumbers.append(localCount)
			#print(localCount)
		return outputNumbers
