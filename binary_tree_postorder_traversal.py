"""
Ques. Binary tree postorder traversal 
T.C. = O(n)
S.C. = O(n)
Link - https://leetcode.com/problems/binary-tree-postorder-traversal/
"""
class Solution:
    def postorderTraversal(self, root):
        if(root == None):
            return 
        
        stack = [root]
        res = list()
        cur = root 
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if(cur.left):
                stack.append(cur.left)
            if(cur.right):
                stack.append(cur.right)
            
        return res[::-1]