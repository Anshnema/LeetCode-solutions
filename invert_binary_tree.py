"""
Ques. Invert Binary Tree
T.C. = O(n) 
S.C. = O(n)
Link - https://leetcode.com/problems/invert-binary-tree/
"""
class Solution:
    def invertTree(self, root):
        if(root is None):
            return 
        
        stack = [root]
        cur = root 
        
        while stack:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left
            if(cur.left):
                stack.append(cur.left)
            if(cur.right):
                stack.append(cur.right)
                
        return root 