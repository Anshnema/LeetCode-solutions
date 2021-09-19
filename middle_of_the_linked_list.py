"""
Ques. Middle of the linked list
T.C. = O(n)
S.C. = O(1)
Link - https://leetcode.com/problems/middle-of-the-linked-list/
"""
class Solution:
    def middleNode(self, head):
        def lengthLinkedList(head):
            cur = head
            cnt = 0
            while cur != None:
                cur = cur.next 
                cnt += 1 
            
            return cnt 
        
        size = lengthLinkedList(head)
        
        if(size % 2 == 1):
            mid = (size + 1) // 2 
        else:
            mid = (size // 2) + 1 
            
        cnt = 1
        cur = head 
        while cnt != mid:
            cur = cur.next 
            cnt += 1 
        
        return cur 
