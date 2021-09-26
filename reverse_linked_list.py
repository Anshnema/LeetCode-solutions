"""
Ques 1. Reverse Linked list 
T.C. = O(n)
S.C. = O(1)
Link - https://leetcode.com/problems/reverse-linked-list/
"""
class Solution:
    def reverseList(self, head):
        if(head is None):
            return None
        
        cur = head 
        prev = None 
        
        while cur != None:
            nxt = cur.next
            cur.next = prev 
            prev = cur 
            cur = nxt 
                
        return prev 
