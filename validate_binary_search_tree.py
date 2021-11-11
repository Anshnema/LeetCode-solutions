"""
Ques. Validate Binary Search Tree
T.C. = O(n)
S.C. = O(n)
Link - https://leetcode.com/problems/validate-binary-search-tree/
"""
class Solution:
    def isValidBST(self, root) -> bool:
        prev = float("-inf")
        stack = []
        
        while len(stack) != 0 or root != None:
            while root != None:
                stack.append(root)
                root = root.left 

            root = stack.pop()
            if(root.val <= prev):
                return False

            prev = root.val 
            root = root.right 
            
        return True 