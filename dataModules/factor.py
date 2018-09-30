

# Class Find Factors- For a given number find a given factor for a number.
class findFactors:
    inputNumber = 0;
    
    
    def __init__(self ,  factorNumber):
        """Initialise Find Factors - Prrovide an input number"""
        self.inputNumber = factorNumber
    
    def calculateFactors(self):
        """Calculate Factors - Find all the factors of a number."""
        itemArray = []
        for count in range(1, self.inputNumber-1):
            if ( (self.inputNumber % count) ==0 ):
                itemArray.append(count)
        print("Output:\t"+str(itemArray) )  
        return itemArray
        
factorsInit = findFactors(10)
factorsInit.calculateFactors()
