"""
Ques. Merge Two binary Trees 
T.C. = O(n) # n represents the min no of nodes from the 2 given trees 
S.C. = O(n) #Stack can be filled upto O(n) in case of a skewed tree
Link - https://leetcode.com/problems/merge-two-binary-trees/
"""
class Solution:
    def mergeTrees(self, root1, root2):
        if(root1 is None):
            return root2
        
        if(root2 is None):
            return root1
        
        stack = [(root1, root2)]
        
        while len(stack) != 0:
            node1, node2 = stack.pop()
            
            if(node1 == None or node2 == None):
                continue 
            
            node1.val += node2.val 
            
            if(node1.left == None):
                node1.left = node2.left
            else:
                stack.append((node1.left, node2.left))
                
            if(node1.right == None):
                node1.right = node2.right
            else:
                stack.append((node1.right, node2.right))
  
        return root1
