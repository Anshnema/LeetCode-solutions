"""
Ques. Increasing Order Search Tree 
T.C. = O(n)
S.C. = O(n)
Link - https://leetcode.com/problems/increasing-order-search-tree/
"""    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        firstNode = True 
        
        while len(stack) != 0 or root != None:
            while root != None:
                stack.append(root)
                root = root.left 
            
            root = stack.pop()
            
            if(firstNode is True):
                new_root = TreeNode(root.val)
                next_node = new_root
                firstNode = False 
            else:
                next_node.right = TreeNode(root.val)
                next_node = next_node.right
                                       
            root = root.right 
            
        return new_root
