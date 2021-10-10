"""
Ques. Path Sum 
T.C. = O(n) 
S.C. = O(n)
Link - https://leetcode.com/problems/path-sum/
"""
class Solution:
    def hasPathSum(self, root, targetSum):
        if(root is None):
            return None 
        
        stack = [(root, root.val)]
        
        while len(stack) > 0:
            cur, total = stack.pop()
            
            if(cur.left is None and cur.right is None):
                if(total == targetSum):
                    return True 
                
            if(cur.left != None):
                stack.append((cur.left, total + cur.left.val))
                
            if(cur.right != None):
                stack.append((cur.right, total + cur.right.val))
        
        return False   