"""

Accellion Coding Question 2
Anthony Tam
anthonytam2018@gmail.com

"""

class ReadWriteExecute:

	# r = 4, w = 2, x = 1, - = 0
	# Return in blocks of 3 characters: rwx (7), r-x (5), -w- (2)
		# = 752
    # param perm_string String, UNIX permission string
    # Returns integer, numerical representation of given permissions
    
    def symbolic_to_octal(str_input):
    	lst = {"r": 4, "w": 2, "x": 1, "-": 0}
    	blk = ""
    	val = 0
    	ret = ""

    	for i in str_input:
    		for k, v in lst.items():
    			if i == k:
    				val += v
    				blk = blk + i

    			if len(blk) == 3:
    				ret = ret + str(val)
    				val = 0
    				blk = ""
    	return ret


print(ReadWriteExecute.symbolic_to_octal('rwxrg-x-w-'))