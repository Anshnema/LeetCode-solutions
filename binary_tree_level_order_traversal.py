"""
Ques. Binary Tree Level Order Traversal
T.C. = O(n)
S.C. = O(n)
Link - https://leetcode.com/problems/binary-tree-level-order-traversal/
"""
class Solution:
    def levelOrder(self, root):
        if(root is None):
            return 
        
        parent = [root]
        output = list()
        
        while len(parent) > 0:
            values = []            
            children = []
            
            for cur in parent:
                values.append(cur.val)
                
                if(cur.left != None):
                    children.append(cur.left)
                
                if(cur.right != None):
                    children.append(cur.right)
            
            parent = children                
            output.append(values)

        return output                         