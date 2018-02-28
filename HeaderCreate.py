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
# 
	inList = data
	outList = []
	for element in inList:
		for index, item in enumerate(element):
			if not any(item == header for header in outList):
				outList.insert(index, item)
	return outList



def headers_traverse(data):
	"""
		Traverse through JSON dataset to extract headers in all levels (including headers of lists/dicts).

		Method:
			- Recursively loop through JSON data from higher level and if a nested element is found, loop through nested element for headers and add all found headers sequentially into new list.

		Useage:
			inList = ['some data']
			outList = []
			headers_traverse(inList)
			print (outList)

	"""

	if isinstance(data, list):
		# print ("list")
		return [headers_traverse(v) for i, v in enumerate(data)]

	elif isinstance(data, dict):
		# print ("dict")
		# print (list(data.keys()))
		# Emptylist.append(list(data.keys()))

		for key in data.keys():
			if not any(key == header for header in Emptylist):
				# print('append: ' + key)
				Emptylist.append(key)

			for k, v in data.items():
				if ((key == k) and ((type(v) == list) or (type(v) == dict))):
					# print (key, k, v, type(v))
					headers_traverse(v)

				# if ((key == k) and ((type(v) == list) or (type(v) == dict))):
				# 	print (key, k, v, type(v))
					# if type(v) == dict:
					# 	print('append: ' + k)
					# 	Emptylist.append(k)

				# if (type(v) == list or dict and key == k and not(type(v) == str or int)):
					

		# for k, v in data.items():
		# 	print (k, type(v), list(data).index(k))
		# 	if type(v) == list or dict:
		# 		Emptylist.insert(list(data).index(k), k) # --> NEED TO MATCH THISD WITH ITS HEADER VALUE!! Because the indexes are correct (0, 1, 2, 3, 0, 1, 2, 3...), if needs to be sub of index 2, add 2 to index.
		# 	# else:
			# 	Emptylist.insert(list(data).index(k), list(data.keys())[list(data).index(k)])
		# for k, v in data.items():
		# 	return {k: headers_traverse(v)}
		return {k: headers_traverse(v) for k, v in data.items()}

	else:
		return
		
headers_traverse(Examplelist)

# -- END -- #

print("--")
print("")
print(Emptylist)
print (headers_basic(Examplelist))