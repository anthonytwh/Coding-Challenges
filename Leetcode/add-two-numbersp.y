## WORK IN PROGRESS##

# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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