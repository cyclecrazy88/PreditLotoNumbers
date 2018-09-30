
from dataModules.processInputDataSet import processInputDataSet as process
from dataModules.processNumberGuess import prrocessNumberGuess

from guessNumbers.guessManager import guessManager

from  initialise.loadNumbers import loadNumbers as numbersIn
def initialiseMain():
    numbers = numbersIn();
    groupDataItemSet = []
    nextNumberSet = numbers.getNextNumberSet()
    
    
    while nextNumberSet != None:
        #print("\nProcess Number Set: ",  nextNumberSet)
        dataSetManager = process(nextNumberSet)
        processedDataSet = dataSetManager.getResultData()
        #print(processedDataSet)
        groupDataItemSet.append(processedDataSet)
        
        # Now the data set has been procssed. It's manager is no longer needed.
        del dataSetManager
        
        nextNumberSet = numbers.getNextNumberSet()
        #break
    resultingCalcData = prrocessNumberGuess( groupDataItemSet )
    #print(resultingCalcData)
    
    guessManager(resultingCalcData)
    
if __name__ == "__main__":
	initialiseMain()
