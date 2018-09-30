
class gapFinder:
    numbersInput = []
    numberRangeProcessed = []
    
    def __init__(self ,  inputNumbers):
        """Look at the gaps for the given number sets inputs and to be processed."""
        self.numbersInput = inputNumbers
        self.numberRangeProcessed  = self.loopAroundNumbers()
         
    def loopAroundNumbers(self):
        """Loop around and find the gap for each set of numbers"""
        lastNumberFound = None
        resultData = []
        
        for number in self.numbersInput:
            #print("Number: "+str(number) )
            # Check to see if I have previously found a number of
            # interest. If not, treat it as the first one.
            if lastNumberFound == None:
                lastNumberFound = number
            else:
                # Calculate the gap in the number set. How big is the difference?
                numberDifference = (number - lastNumberFound);
                # Add the data onto the end of the array. Remember it for later.
                resultData.append(numberDifference)
                # Initialise the number for the next time around
                lastNumberFound = number
        #print("Resulting Difference Data Set: "+ str( resultData) )
        return resultData;
        
    def getNumberRangeFound(self):
        return self.numberRangeProcessed;
        
        
        
        
        
