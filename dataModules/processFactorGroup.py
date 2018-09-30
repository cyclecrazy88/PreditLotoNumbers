
def factorItemSet(factorSet):
    output = []
    # For a data set. Factor numbers are likely to repeat. Ensuring a current
    # pobable pattern is important. So look around to see how many factors 
    # are unique which might provide a possible clue to numbers which 'relate' that 
    # appear in a recent sequence.
    def repeatItemsInSet(itemCode ,  dataSetInput):
        countTotal = 0
        # Loop around the data set. How many times have the items appeared
        # with this factor.
        for dataSetItem in dataSetInput:
            # If this is a multiple count it
            # ignore any own numbers, which are itself.
            if dataSetItem != itemCode and (dataSetItem % itemCode) == 0:
                countTotal += 1
        return countTotal
    # Loop around the recent factors found within the group.
    if 'factorGroup' in factorSet:
        groupSet = factorSet['factorGroup']
        #print("Group Set", groupSet)
        
        # Loop around the items in the set
        for item in groupSet:
            factorRpeatCount = repeatItemsInSet( item ,  groupSet )
            # Include anything with repeat factor codes.
            if item > 1:
                #print(item ,  "Repeat Count",  factorRpeatCount)
                output.append( (item , factorRpeatCount) )
    return output
                

def processFactorGroup(groupItemData):
    #print("Factor Group: ", groupItemData )
    output = []
    for groupItem in groupItemData:
        
        output.append( factorItemSet(groupItem) ) 
        
    #print(output)
    return output
        
        
