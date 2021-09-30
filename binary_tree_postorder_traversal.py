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
        
        while len(stack) > 0:
            cur = stack.pop()
            res.append(cur.val)
            if(cur.left != None):
                stack.append(cur.left)
            if(cur.right != None):
                stack.append(cur.right)
            
        return res[::-1]