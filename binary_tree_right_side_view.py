"""
Ques. Binary Tree right side view 
T.C. = O(n)
S.C. = O(n)
Link - https://leetcode.com/problems/binary-tree-right-side-view/
"""
class Solution:
    def rightSideView(self, root):
        if(root is None):
            return  
        
        parent = [root]
        res = []
        while len(parent) > 0:
            res.append(parent[-1].val)
            child = []
            
            for cur in parent:
                if(cur.left != None):
                    child.append(cur.left)
                if(cur.right != None):
                    child.append(cur.right)
            
            parent = child
            
        return res 