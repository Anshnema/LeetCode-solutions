"""
Ques. Balanced Binary Tree 
T.C. = O(n)
S.C. = O(n)
"""
class Solution:
    def isBalanced(self, root) -> bool:
        def dfs(root):
            if(root is None):
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]