"""
Ques. Binary Tree Inorder Traversal
T.C. = O(n)
S.C. = O(n)
Link - https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
class Solution:
    def inorderTraversal(self, root):
        res = []
        stack = list()
        cur = root 
        
        while cur or stack:
            while(cur != None):
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right 
            
        return res 