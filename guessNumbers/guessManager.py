# Functionality to allow a random guess to be made.
from guessNumbers.guessItemNumber import guessItemNumber
from guessNumbers.selectGuessBestBits import bestBits

import pickle

def requestGuessToBeMade(inputData, guessLength = None):
   # Allow a number guess or set of guesses to occur.
    guessNumber = guessItemNumber(inputData)
    #print("Guess Next Number")
    resultData = guessNumber.makeNextGuess(guessLength)
    del guessNumber
    return resultData
    
def groupGuess(inputData, guessLength = None,percentageAllowed = 0):
	# Setup an empty array for the result items.
	groupGuessResultAverage = [ {},{},{},{},{} ]
	
	calculationInputLength = 2000
	print("Calculation Length", calculationInputLength)
	print("Guess Length: ", guessLength)
	for count in range(1,calculationInputLength):
	
		guessResult = requestGuessToBeMade(inputData, guessLength)
		#print("Guess Result:", guessResult)
		groupGuessResultAverage = bestBits(guessResult , percentageAllowed , groupGuessResultAverage)
	print("Guess Average: ",groupGuessResultAverage )
	return groupGuessResultAverage
    
def guessManager(inputData):
	output = {}
	
	print('Low Percentage Everything')
	output["lowPercentageEverythingLengthNone"] = groupGuess(inputData,None, 33)
	print('Low Percentage')
	output["lowPercentageLength10"] = groupGuess(inputData,10,33)
	
	print('Middle Percentage')
	output["middlePercentageLength10"] = groupGuess(inputData,10,50)

	print('High Percentage - Data Set 20')
	output["highPercentageLength20"] = groupGuess(inputData,20,66)
	
	
	print('High Percentage')
	output["highPercentageLength10"] = groupGuess(inputData,10,66)

	# ---------------------------------
	# Push the file handle to the file (output pickle).
	# ---------------------------------
	fileHandle = open('./guessManagerSummary.pkl','wb')
	pickle.dump(output ,fileHandle )
	fileHandle.close()
