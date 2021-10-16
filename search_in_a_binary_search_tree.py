"""
Ques. Search in a Binary search Tree 
T.C. = O(n) 
S.C. = O(1)
Link - https://leetcode.com/problems/search-in-a-binary-search-tree/
"""
class Solution:
    def searchBST(self, root, val):
        while root != None:
            if(root.val == val):
                return root 
            elif(root.val > val):
                root = root.left 
            else:
                root = root.right 
        
        return 
