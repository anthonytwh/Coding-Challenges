"""

List Logic (Python3)
	- Remove Duplicate Methods


February 13, 2018
@anthonytwh


"""

ExampleList = [1,4,7,8,6,89,7,4,5,1,2,3,6,5,9,7,4,5,2,1,3,65,45,78,4,2,1,5,4,874,61,21,5,7,8,9654,2,7,87,23,56,4,8,7,5,98,45,4,12,54,98,87,54,62,35,8,4,5,8,7,1,2,35,8,8,1,6,8,7,5,8,4,2,4,9,35,45,54,87,1,5,7,52,2,566,99]


def RemoveDuplicates_invasive(data):
	"""
		Remove all non-unique items in a list.

		Method:
			- Match each element with every other element in the list and remove if duplicate exists.
			
	"""

	inList = data
	for element in inList:
		for item in inList:
			if item == element: 
				del inList[inList.index(item)]
	return inList


def RemoveDuplicates_invasiveP(data):
	"""
		Remove duplicates in a list.

		Method:
			- Count item occurences and remove items when duplicates are counted. 
		
	"""

	inList = data
	for element in inList:
		count = 0
		for index, item in enumerate(inList):
			if element == item:
				count = count + 1

			if count >= 2:
				inList.pop(index)
				count = count - 1
	return inList


def RemoveDuplicates_single(data):
	"""
		Create unordered header of items in a list while preserving original data.

		Method:
			- If any element in input list is not found in output list, it is added to the end of output list. 

	"""

	inList = data
	outList = []
	for element in inList:
		if not any(element == item for item in outList):
			outList.append(element)
	return outList


def RemoveDuplicates_multiple(data):
	"""
		Create ordered header of items in a list (equivalent to removing duplicates in a list) while preserving original data

		Method:
			- If any element in input list is not found in output list, it is added to output list based on the index of the element. 
			
	"""

	inList = data
	outList = []
	for element in inList:
		if not any(element == item for item in outList):
			outList.insert(inList.index(element),element)
	return outList


# -- END -- #