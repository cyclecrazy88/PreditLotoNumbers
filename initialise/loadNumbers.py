from initialise.fetchCurrentData import requestDataSet

# Input Class - Request the numbers/items.
class loadNumbers:
	inputDataSet = None
	def __init__(self):
		"""Initalising loading the numbers array"""
		# Fetch from file.
		##self.initialiseFileData()
		self.inputDataSet = []
		
		webRequestData = requestDataSet()
		#print("Data length: ", webRequestData)
		self.readDataFromArray(webRequestData)
		#print('Input Data Found: ',self.inputDataSet)
		
		
		
	def getNextNumberSet(self):
		"""Return the next numbers for the sequence."""
		if len(self.inputDataSet)>0:
			nextItemSetFound = self.inputDataSet.pop(0)
			#print("Item Set Found: "+ str(nextItemSetFound))
			return nextItemSetFound
		else:
			return None
			
	def readDataFromArray(self,inputDataSet):
		# Loop around the input array and assemble the data items.
		for inputData in inputDataSet:
			# Check if the line looks like it's formatted correctly.
			if inputData.find(' - ') > -1:
				stringDataItems = inputData.strip().split(' - ');
				lineDataSet = []
				for itemData in stringDataItems:
					if itemData.isnumeric():
						lineDataSet.append( int(itemData) )
					
				# Ensure there are enough numbers in the set. To ensure this is actually a loto number
				if len(lineDataSet)>4:
				# Add the line data which results to the inputDataSet stored as part of this class.
					self.inputDataSet.append(lineDataSet)		
		
	def initialiseFileData(self):
		"""Read the input numbers from a text file"""
		fileData = open("./inputData/inputData2.txt",  "r")
		# Loop around each data item. For each number, parse it as a number
		# then append it to an array.
		for dataLine in fileData:
			# Check if the line looks like it's formatted correctly.
			if dataLine.find(' - ') > -1:
				stringDataItems = dataLine.strip().split(' - ');
				lineDataSet = []
				for itemData in stringDataItems:
					if itemData.isnumeric():
						lineDataSet.append( int(itemData) )
				# Ensure there are enough numbers in the set. To ensure this is actually a loto number
				if len(lineDataSet)>4:		
					# Add the line data which results to the inputDataSet stored as part of this class.
					self.inputDataSet.append(lineDataSet)
