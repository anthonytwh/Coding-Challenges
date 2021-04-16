## Leet Code Practice ##


'''
Palindrome Number - Easy
Apr 2021
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        for i in range(0, len(x)):
            if x[i] != x[len(x)-1-i]:
                return False
        return True


'''
Longest Palindromic Substring - Medium
Apr 2021
'''

class Solution:
	def longestPalindrome(self, s: str) -> str:
		out = ""
		for i in range(0,len(s)):
			for j in range (len(s), i, -1):
				# print (s[i], s[j], s[i:j])
				if j - i <= len(out):
					break
				if s[i:j] == s[i:j][::-1]:
					out = s[i:j]
		return out


'''
Reverse Integer - Easy
Apr 2021
'''

class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x == 0:
            ''' Return 0 if 0
            '''
            return 0
        if x < 0:
            ''' If negative make positive and neg true
            '''
            x = x*-1
            neg = True 
        x = int(str(x)[::-1]) # Convert str, flip, convert int
        if neg:
            ''' Re-apply negative 
            '''
            x = x*-1
        
        if not (-2**31 < x < 2**31):
            ''' x must be within condition.
            '''
            return 0
        
        return x

'''
Add Two Numbers
Old
'''

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        carry = 0
        
        while l1 and l2:
            l3 = l1.val + l2.val + carry
            
            carry = 0
            rem = l3%10
            if l3//10 != 0:
                carry = int(l3/10)
                l3 = rem
            
            l1 = l1.next
            l2 = l2.next
            result.append(l3)

        if carry != 0:
            l3 = carry
            result.append(l3)
            
        return result


# Merge two sorted Lists
# Dec 7, 2019
class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		head = ListNode("")
		l3 = head
		while l1 or l2:
			if l2 and not l1:
				l3.val = l2.val
				l2 = l2.next
			if l1 and not l2:
				l3.val = l1.val
				l1 = l1.next
			if l1 and l2:
				if l1.val <= l2.val:
					l3.val = l1.val
					l1 = l1.next
				else:
					l3.val = l2.val
					l2 = l2.next
			if l1 or l2:
				l3.next = ListNode(0)
				l3 = l3.next
		return head


# Water Container
# Dec 7, 2019
class Solution:
	def maxArea(self, height: List[int]) -> int:
		'''Solution'''
		max_area = 0
		start = 0
		end = len(height)-1
		
		while end > start:
			area = min(height[end], height[start]) * (end - start)      
			if area > max_area:
				max_area = area
			if height[end] > height[start]:
				start += 1
			else:
				end -= 1
		return max_area      
		
		
	def maxArea(self, height: List[int]) -> int:
		'''Time limit exceeded'''
		max_area = 0
		for i in range (len(height)):
			for j in range(len(height)):
				if i == j:
					pass
				area = min(height[i], height[j]) * abs(i - j)
				if area > max_area:
					max_area = area
		return max_area


# Remove Element
# Nov 23, 2019
class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		c = 0
		for i in range(len(nums)):
			if nums[i] != val:
				nums[c] = nums[i]
				c += 1
		print (nums[:c])
		return (len(nums[:c]))
				
		

# Remove Duplicates from Sorted Array
# Nov 23, 2019
class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		c = 1
		for i in range(len(nums)-1):
			if nums[i] != nums[i+1]:
				# print (nums[i], nums[i+1])
				nums[c] = nums[i+1]
				c+=1
		# print (nums[:c])
		return len(nums[:c])

# Valid Parenthesis
# Nov 23, 2019
class Solution:
	def isValid(self, s: str) -> bool:
		ref = {'(':')', '[':']', '{':'}'}
		store = []
		for each in s:
			if each in ref:
				store.append(each)
			if not (each in ref):
				if not store:
					return False
				if not (each == ref[store.pop()]):
					return False
		if not store:
			return True

# Lognest Common Prefix
# Nov 17, 2019
class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		if (not(strs) or len(strs) < 1):
			return ""
		
		if len(strs) == 1:
			return strs[0]
		
		if len(strs) > 1:
			short = strs[0]
			for s in strs:
				if len(s) < len(short):
					short = s
			strs.remove(short)
			out = ""
			for i in range(1, len(short)+1):
				count = 0
				for each in strs:
					if short[:i] == each[:i]:                        
						count += 1
					if count == len(strs):
						out = short[:i]
			return out                     


"""
Two Sum
44ms ~~ 100%

"""
class Solution:
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		
		lookup = {}
		for i, num in enumerate(nums):
			if target - num in lookup:
				return [lookup[target - num], i]
			lookup[num] = i
		
		# for i in range(len(nums)):
		#     for j in range(i, len(nums)):
		#         if (nums[i] + nums[j] == target) and not(i==j):
		#             return [i, j]




"""
Reverse Integer
60ms ~~ 100%

"""
class Solution:
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""           
		xstr = str(abs(x))
		ostr = ""
		for i in range(len(xstr)):
			ostr = ostr + xstr[len(xstr)-1-i]
			
		if (int(ostr) < ((2**31) - 1)):
			if not(x == abs(x)):
				return int("-" + ostr)
			else:
				return int(ostr)
		else:
			print (ostr)
			return 0


"""
Merge Two Sorted Lists
68ms ~~ 92.55%

"""
class Solution:
	def __init__(self):
		self.l3= []
	
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		print (self.l3)
		
		if (l1 == None) and (l2 == None):
			return self.l3
		
		if (l1 == None) and not(l2 == None):
			return self.mergel2(l2)
		
		if (l2 == None) and not(l1 == None):
			return self.mergel1(l1)

		if l1.val < l2.val:
			self.l3.append(l1.val)
			l1 = l1.next
			return self.mergeTwoLists(l1, l2)

		if l2.val < l1.val:
			self.l3.append(l2.val)
			l2 = l2.next
			return self.mergeTwoLists(l1, l2)

		if l1.val == l2.val:
			self.l3.append (l1.val)
			l1 = l1.next
			self.l3.append (l2.val)
			l2 = l2.next
			return self.mergeTwoLists(l1, l2)
		
		
	def mergel1(self, l1):
		self.l3.append(l1.val)
		l1 = l1.next
		return self.mergeTwoLists(l1, None)
		
	
	def mergel2(self, l2):
		self.l3.append(l2.val)
		l2 = l2.next
		return self.mergeTwoLists(None, l2)

