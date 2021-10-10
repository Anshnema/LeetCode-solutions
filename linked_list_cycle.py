"""
Ques. Linked list cycle 
T.C. = O(n)
S.C. = O(1)
Link - https://leetcode.com/problems/linked-list-cycle/
"""
class Solution:
    def hasCycle(self, head):
        if(head is None):
            return False 
        
        slow = head
        fast = head.next
        
        while slow != None and fast != None and fast.next != None:
            if(slow == fast):
                return True 
        
            fast = fast.next.next
            slow = slow.next 
        return False 
