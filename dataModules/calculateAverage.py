
def calculateAverage(inputArray):
    runningTotal = 0
    for number in inputArray:
        runningTotal += number
    
    if runningTotal > 0 and len(inputArray) > 0:
        return int(runningTotal / len(inputArray) )
    else:
        return None
        
        
if __name__ == "__main__":
   print(calculateAverage( [22, 31, 36, 38, 44] ) )
