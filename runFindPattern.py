# Request the numbers for the input.
from  initialise.loadNumbers import loadNumbers as numbersIn

# Pattern summarise.
from patternSearch.summarisePattern import parseRecentPattern, summarizePattern
from patternSearch.summariseGroupAverages import summariseGroupAverage
from patternSearch.checkTrend import checkTrend

from run import initialiseMain as initialiseMainRun

import os,pickle

def initialiseMain():
	numbers = numbersIn();
	numberData = []
	nextNumberSet = numbers.getNextNumberSet()
	while nextNumberSet != None:
		nextNumberSet = numbers.getNextNumberSet()
		numberData.append(nextNumberSet)

	print("First Number :",numberData[0])
	print("Second Number:",numberData[1])

	outputTrend = []
	patternResult = parseRecentPattern(numberData)
	for resultItem in range(0,7):
		outputTrend.append( summarizePattern(patternResult,resultItem) )
		summariseGroupAverage(patternResult, resultItem)
	#print("OutputTrend: ",outputTrend )
	firstItem = patternResult[0]
	#print("First Item: ",firstItem )
	for resultItem in range(0,7):
		checkTrend(firstItem , outputTrend , resultItem)
	readFactorData()
def readFactorData():
	inputData = None
	if os.path.isfile('./guessManagerSummary.pkl'):
		fileHandle = open('./guessManagerSummary.pkl','rb')
		inputData = pickle.load(fileHandle)
		fileHandle.close()
	else:
		initialiseMainRun()
		fileHandle = open('./guessManagerSummary.pkl','rb')
		inputData = pickle.load(fileHandle)
		fileHandle.close()
		
	print('lowPercentageLength10:',inputData["lowPercentageLength10"] )
	
	print('lowPercentageEverythingLengthNone:',inputData["lowPercentageEverythingLengthNone"] )
	
if __name__ == "__main__":
	initialiseMain()
