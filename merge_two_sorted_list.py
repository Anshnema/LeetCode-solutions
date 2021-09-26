"""
Ques. Merge two sorted lists
T.C. = O(n)
S.C. = O(n)
Link - https://leetcode.com/problems/merge-two-sorted-lists/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        if(l1 is None):
            return l2
        
        if(l2 is None):
            return l1
        
        head = ListNode(0)
        cur = head
        
        while l1 != None and l2 != None:
            if(l1.val < l2.val):
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next 
            else:
                cur.next = ListNode(l2.val)
                cur = cur.next 
                l2 = l2.next
        
        while l1 != None:
            cur.next = ListNode(l1.val)
            cur = cur.next 
            l1 = l1.next
        
        while l2 != None:
            cur.next = ListNode(l2.val)
            cur = cur.next 
            l2 = l2.next 
            
        return head.next 
