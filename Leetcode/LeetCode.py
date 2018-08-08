## Leet Code Practice ##



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