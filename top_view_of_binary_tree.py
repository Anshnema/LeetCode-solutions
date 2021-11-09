"""
Ques. Top View of Binary Tree 
T.C. = O(n)
S.C. = O(n)
Link - https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1
"""
class Solution:
    def topView(self,root):
        if(root is None):
            return 
        
        parent = [(root, 0)]
        d = {0: root.data}
        
        while len(parent) != 0:
            children = []
            for cur, axis in parent:
                if(cur.left != None):
                    if((axis - 1) not in d):
                        d[axis - 1] = cur.left.data
                    children.append((cur.left, axis - 1))
                
                if(cur.right != None):
                    if((axis + 1) not in d):
                        d[axis + 1] = cur.right.data
                    children.append((cur.right, axis + 1))
                
            parent = children 
        
        res = [] 
        for i in range(min(d.keys()), max(d.keys()) + 1):
            res.append(d[i])
            
        return res 
