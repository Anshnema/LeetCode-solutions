"""
Ques. Palindrome Linked List 

Approach. Reversing the Linked list from the mid position and match the elements.
          1. Slow and fast are 2 pointers. 
          2. Fast moves with 2x speed of slow. Hence, slow is at the mid when fast is at the end

T.C. = O(n)
S.C = O(1)
"""
class Solution:
    def isPalindrome(self, head):
        def reverse(head):
            prev = None
            cur = head
            
            while cur != None:
                nxt = cur.next 
                cur.next = prev
                prev = cur 
                cur = nxt 
            
            return prev
        
        slow = fast = head 
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next 
            
        slow = reverse(slow)
        cur = head 
        
        while slow != None:
            if(slow.val != cur.val):
                return False 
            slow = slow.next 
            cur = cur.next 
            
        return True
