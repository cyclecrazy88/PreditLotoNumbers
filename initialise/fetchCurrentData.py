
import json
import urllib.request
import pickle, os

from initialise.parseLotoNumbersHtml import parseData

# ------------------------------------------------
#  Network request and pickle handlers.
# ------------------------------------------------
def makeNetworkRequest( targetURL ):
	initialURL = targetURL
	outputData = urllib.request.urlopen(initialURL).read()
	decodeData = outputData.decode("utf-8")
	return decodeData

def pickleResultSet(inputData):
	fileHandle = open('./currentLotoData.pkl','wb')
	pickle.dump(inputData, fileHandle)
	fileHandle.close()
# ---------------------------------------------------
# Regardless of the location - try to pickup a current
# request data set. This can be parsed/processed later.
# ---------------------------------------------------
def requestDataSet():
	
	if os.path.isfile('./currentLotoData.pkl')==False:	
		print("Go get data")
		resultData = makeNetworkRequest("https://www.national-lottery.co.uk/results/euromillions/draw-history/")
		pickleResultSet(resultData)
		return parseData(resultData)
	else:
		print("Data already available")
		fileHandle = open('./currentLotoData.pkl','rb')
		resultData = pickle.load(fileHandle)
		fileHandle.close()
		return parseData(resultData)

#print(resultData)

