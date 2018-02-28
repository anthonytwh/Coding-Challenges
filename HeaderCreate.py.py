"""

HeaderCreate (Python3)
	- Create Headers of Lists/Dictionaries (for JSON)


February 28, 2018
@anthonytwh


"""

Examplelist =	[
					{
						'name': 'Anthony', 
						'age': 23, 
						'contacts':	{
										'one': 'Jiwon', 
										'two': 'John', 
										'three': 'Glen'
									}, 
						'gender': 'male', 
						'count':	[
										{ 
											'a': 1, 
											'b': 2, 
											'c':3
										}
									]
					}
				]


Emptylist = []

def headers_basic(data):
	"""
		Create ordered header of items in a list (equivalent to removing duplicates in a list).

		Method:
			- If any element in input list is not found in output list, it is added to output list based on the index of the element. 
			
	"""

	inList = data
	outList = []
	for element in inList:
		for index, item in enumerate(element):
			if not any(item == header for header in outList):
				outList.insert(index, item)
	return outList



def headers_traverse(data):
	"""
		Traverse through JSON dataset to extract headers in all levels (including headers of lists/dicts). In this example, all nested JSON elements are type:dict.

		Method:
			- Recursively loop through JSON data from higher level and if a nested element is found, loop through nested element for headers and add all found headers sequentially into new list.

		Useage:
			inList = ['some data']
			outList = []
			headers_traverse(inList)
			print (outList)

	"""

	if isinstance(data, list):
		return [headers_traverse(v) for i, v in enumerate(data)]

	elif isinstance(data, dict):
		for key in data.keys():
			if not any(key == header for header in Emptylist):
				Emptylist.append(key)
			for k, v in data.items():
				if ((key == k) and ((type(v) == list) or (type(v) == dict))):
					headers_traverse(v)
		return {k: headers_traverse(v) for k, v in data.items()}

	else:
		return
		
headers_traverse(Examplelist)

# -- END -- #