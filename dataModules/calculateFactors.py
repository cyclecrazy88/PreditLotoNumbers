
from dataModules.calculateAverage import calculateAverage 

def listFactorsLoop(numberList = None):
    """Loop around a list of current factor numbers given"""
    outputData = []
    if numberList != None:
        for numberItem in numberList:
            factorGroup = loopAroundFactorsForNumber(number = numberItem)
            
    
            # Using a tuple. Include the average factor here.
            averageTotal = calculateAverage(factorGroup)
            
            dictionaryResult = {'factorGroup':factorGroup ,  'averageTotal':averageTotal}
    
            # Return this is part of the output. (Dictionary item)
            outputData.append(dictionaryResult)
    return outputData
def loopAroundFactorsForNumber(  number = None):
    """For an individual number. Find all of it's factors"""
    outputData = []
    if number != None:
        for count in range(1, number):
            numberStr = int(number % count)
            if numberStr == 0:
                outputData.append(count)
    return outputData
if __name__ == "__main__":
    print(loopAroundFactorsForNumber(number=50))
