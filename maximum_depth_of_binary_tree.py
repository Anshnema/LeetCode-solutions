"""
Ques 1. Maximum Depth of Binary Tree
T.C. = O(n)
S.C. = O(n)
Link - https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
class Solution:
    def maxDepth(self, root):
        if(root == None):
            return 0
        
        depth = 0 
        parent = [root]
        
        while len(parent) > 0:
            children = []
            depth += 1 
            
            for cur in parent:
                if(cur.left != None):
                    children.append(cur.left)
                
                if(cur.right != None):
                    children.append(cur.right)

            parent = children 
            
        return depth 