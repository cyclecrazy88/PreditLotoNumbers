from dataModules.processFactorGroup import processFactorGroup


# ------------------------------------------------------------------------------------------------
# Gap Variation - Look at the general trend with regards to any gaps.
# ------------------------------------------------------------------------------------------------
# Look for the variation. Gaps higher/lower/equal in the data set.
def inspectGapVariation(gapNumbers):
    previousNumber = None
    
    dataSetPatten = []
    
    for gapItem in gapNumbers:
        if previousNumber == None:
            previousNumber = gapItem
            continue
        #print("Next Item: ",gapItem ,  ' Previous',  previousNumber  )

        # Append an index. Higher, lower or non depending on the 
        #movement of the gap
        if gapItem < previousNumber:
            # Indicate the gap been getting smaller.
            dataSetPatten.append(False)
        elif gapItem > previousNumber:
            # Indicate the gap has been getting bigger
            dataSetPatten.append(True)
        else:
            # No change in the gap size
            dataSetPatten.append(None)
        #print(dataSetPatten)
        previousNumber = gapItem
    return dataSetPatten
# ------------------------------------------------------------------------------------------------
# Gap Trend - Look at the pattern for the gaps. See what the pattern looks like.
# Loop around the recent items. Find a likely recent pattern
# ------------------------------------------------------------------------------------------------
def getMovementLikelyWithinGroup(dataSetItems ,  distanceBack):
    count = 0
    
    countTrue = 0
    countFalse = 0
    
    for itemMovement in dataSetItems:
        if itemMovement == True:
                countTrue += 1
        elif itemMovement == False:
                countFalse += 1
        
        #print(itemMovement)
        count += 1
        if count > distanceBack:
            break
    #print("True",  countTrue ,  'False',  countFalse)
    
    # Return true/false/None whether there has been a positive trend
    # recently
    if countTrue > countFalse:
        return True
    elif countTrue < countFalse:
        return False
    else:
        return None
    
    
    
    
# ------------------------------------------------------------------------------------------------
# Main Entry Handler. For the given input items look at different
# combinations and variables in the data set.
# ------------------------------------------------------------------------------------------------
def prrocessNumberGuess(inputDataSet):
    # Array for the gap numbers
    gapItemDataSet = []
    # Array for the factor numbers
    itemFactorDataSet = []
    inputNumberData = []
    
    for dataSetItem in inputDataSet:
        #print(dataSetItem)
        
        if 'averageGap' in dataSetItem:
            #print('Gap:', dataSetItem['averageGap']  )
            gapItemDataSet.append(dataSetItem['averageGap'])
        if 'inputNumbers' in dataSetItem:
            inputNumberData.append( dataSetItem['inputNumbers'] )
            #print('Input Numbers: ', dataSetItem['inputNumbers'] )
        if 'factorsBetween' in dataSetItem:
            pass
            #print('Factors Between:', dataSetItem['factorsBetween'] )
            # Add a factor to the data set.
            inputNumbers = None
            if 'inputNumbers' in dataSetItem:
                inputNumbers = dataSetItem['inputNumbers']
                
            # Append in factors and the input numbers to the data set.
            itemFactorDataSet.append( (dataSetItem['factorsBetween'] , inputNumbers  ) )
        if 'numberRangeFound' in dataSetItem:
            pass
            #print('Number Range: ', dataSetItem['numberRangeFound'] )
    
    # For the gap look at the general trend in the data set.
    if len(gapItemDataSet) > 0:
        # For the give data set. Look for a higher/lower pattern
        gapVariationStats = inspectGapVariation(gapItemDataSet)
    
        # Look at the general trend - True = Bigger. False = Smaller
        generalTrend = getMovementLikelyWithinGroup(gapVariationStats, 6)
        # False
        #print("Gap Analysis Trend: ",generalTrend )
        #print(gapVariationStats)
    outputFactorGroupingData = []
    # Only jump into here if some data has been found.
    if len(itemFactorDataSet)>0:
        # Loop around all the resulting items in the data set. Create/calc the factors
        # for each and every line numbe.
        for factorLoopAround in itemFactorDataSet:
            factorDataItem ,  inputNumbers = factorLoopAround
            # Take the factor numbers from the Tuple and pass into the item.
            resultItem = processFactorGroup( factorDataItem )
            # Format the item neatly into a Tuple.
            outputItem = (resultItem , inputNumbers )
            # Add the resulting item to the data set for the factor numbes
            outputFactorGroupingData.append(outputItem)
            #print(resultItem ,  "Numbers",outputItem  )
        
    # Format the resulting data items nicely into a dictionary. This allows a seperate
    # module to process the data items later.
    completeResult = {"inputNumbers":inputNumberData,"gapItemDataSet" : gapItemDataSet ,  \
    "factorOutputItemSet":outputFactorGroupingData ,  "generalTrend":generalTrend }
    
    return completeResult
