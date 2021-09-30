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
        
        while len(stack) > 0:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left
            if(cur.left != None):
                stack.append(cur.left)
            if(cur.right != None):
                stack.append(cur.right)
                
        return root 