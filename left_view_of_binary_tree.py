"""
Ques. Left View of binary Tree  
T.C. = O(n)
S.C. = O(n) #max no of nodes in any level
Link - https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1
"""
def LeftView(root):
    if(root is None):
        return 
    
    leftview = [] 
    parent = [root]
    
    while len(parent) != 0:
        leftview.append(parent[0].data)
        children = []
        
        for cur in parent:
            if(cur.left != None):
                children.append(cur.left)
            if(cur.right != None):
                children.append(cur.right)
        
        parent = children 
        
    return leftview 