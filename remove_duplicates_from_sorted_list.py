"""
Ques. Remove duplicates from sorted list
T.C. = O(n)
S.C. = O(1) 
Link - https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""
class Solution:
    def deleteDuplicates(self, head):
        if(head is None):
            return
        
        cur = head.next 
        prev = head
        
        while cur != None:
            if(cur.val == prev.val):
                cur = cur.next
                prev.next = cur 
            else:
                prev = cur
                cur = cur.next 
        
        return head
