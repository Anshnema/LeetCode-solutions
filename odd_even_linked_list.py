"""
Ques. Odd Even Linked List 
T.C. = O(n)
S.C. = O(1)
Link - https://leetcode.com/problems/odd-even-linked-list/ 
"""
class Solution:
    def oddEvenList(self, head):
        if(head is None):
            return 
        
        odd = head 
        tail= head.next
        even = tail
        
        while even != None and even.next != None:
            odd.next = odd.next.next 
            even.next = even.next.next
            
            odd = odd.next 
            even = even.next 
        
        odd.next = tail 
            
        return head 