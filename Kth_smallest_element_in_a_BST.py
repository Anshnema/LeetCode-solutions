"""
Ques. Kth smallest element in a BST
T.C. = O(n + k) => k is added as pop operation happens k times.  
S.C. = O(n) 
Link - https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        stack = list()
        cur = root
        cnt = 0 
        
        while cur != None or len(stack) > 0:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cnt += 1
            
            if(cnt == k):
                return cur.val
            
            cur = cur.right 
