"""
Ques. Binary Tree Preorder Traversal 
T.C. = O(n)
S.C. = O(n)
Link - https://leetcode.com/problems/binary-tree-preorder-traversal/
"""
class Solution:
    def preorderTraversal(self, root):
        stack = list()
        res = list()
        cur = root 
        
        while cur or stack:
            while(cur != None):
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            cur = cur.right
            
        return res 
