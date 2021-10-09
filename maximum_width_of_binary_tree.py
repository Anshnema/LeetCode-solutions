"""
Ques. Maximum width of binary tree
T.C. = O(n)
S.C. = O(n)
Link - https://leetcode.com/problems/maximum-width-of-binary-tree/
"""
class Solution:
    def widthOfBinaryTree(self, root) -> int:
        root.val = 0
        max_width = 0
        parent = [root]
        
        while len(parent) > 0:
            children = []
            max_width = max(max_width, parent[-1].val - parent[0].val + 1)
            
            for cur in parent:
                if(cur.left != None):
                    cur.left.val = cur.val * 2 
                    children.append(cur.left)
                
                if(cur.right != None):
                    cur.right.val = (cur.val * 2) + 1
                    children.append(cur.right)
            
            parent = children 
        
        return max_width 
