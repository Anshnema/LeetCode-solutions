"""
Ques. Count complete tree nodes 
T.C. = O(log n * log n)
S.C. = O(n)
Link - https://leetcode.com/problems/count-complete-tree-nodes/
"""
class Solution:
    def countNodes(self, root):
        def leftheight(root):
            cnt = 0
            cur = root 
            while cur != None:
                cnt += 1 
                cur = cur.left
            
            return cnt 

        def rightheight(root):
            cnt = 0 
            cur = root
            while cur != None:
                cnt += 1 
                cur = cur.right 
            
            return cnt 

        lh = leftheight(root)
        rh = rightheight(root)

        if(lh == rh):
            return (2 ** lh) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1 