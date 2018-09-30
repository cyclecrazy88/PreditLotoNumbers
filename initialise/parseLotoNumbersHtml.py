# ---------------------------------------------
# Split down the data set. Look at the span tags.
# Try to find all the numbers in the span tag,
# this results in an array, which can be processed later.
# ---------------------------------------------
def splitSpanTags(data):
	splitDataSpan = data.lower().split("<span")
	spanTotalLength = len(splitDataSpan)
	#print("Span Length: ", spanTotalLength)
	outputData = []
	for spanItem in splitDataSpan:
		if spanItem.lower().find('</span>')>-1:
			spanItem = spanItem[: spanItem.lower().find('</span>') ].strip()
			
			# If there is a closing tag. Just jump past this into the content
			if spanItem.lower().find('>')>-1:
				spanItem = spanItem[ spanItem.lower().find('>')+1: ].strip()
			
			# Now look at the content. I am looking for some dashes for the numbers.
			itemPart = spanItem.split('-')
			if len(itemPart)>3:
				#print('SpanData Tag: ',spanItem )
				# Push the item onto the array for output
				outputData.append(spanItem)
	return outputData
	
# Parse HTML data into blocks
def parseData(data):
	#print("Parse Result")
	return splitSpanTags(data)
