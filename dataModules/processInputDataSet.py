
from dataModules.difference import gapFinder as gapFind

from dataModules.calculateFactors import listFactorsLoop
from dataModules.calculateAverage import calculateAverage 


class processInputDataSet:
    processData = []
    gapFindData = None
    factorsBetween = None
    resultData = None
    def __init__(self ,  numbers):
        """Handler for processing of current number set."""
        self.processData = numbers
        #print("My Numbers:"+str(numbers) )
        self.gapFindData = gapFind(numbers)
        self.factorsBetween = listFactorsLoop(numberList = numbers)
        #print("Factors Between: ", self.factorsBetween )
        #print("Gap Find Data: ",  self.gapFindData.getNumberRangeFound() )
        
        averageGap = calculateAverage( self.gapFindData.getNumberRangeFound() )
        #print("Average Gap: ",  averageGap)
        
        # Cluster the resulting items together in a dictionary. A calculation can occur later as a group.
        resultData = {'inputNumbers':numbers}
        resultData['factorsBetween'] = self.factorsBetween 
        resultData['numberRangeFound'] = self.gapFindData.getNumberRangeFound() 
        resultData['averageGap'] = averageGap
        self.resultData = resultData
    def getResultData(self):
        return self.resultData
        
