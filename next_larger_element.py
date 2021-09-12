"""
Ques. Next larger element  
T.C. = O(n)
S.C. = O(n)
Link - https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1
"""
def nextLargerElement(self,arr,n):
    stack = list()
    next_larger_element = [0] * n
    
    for idx, val in enumerate(arr):
        if(len(stack) == 0):
            stack.append(idx)
        else:
            cur = val
            while len(stack) != 0 and arr[stack[-1]] < cur:
                x = stack[-1]
                stack.pop()
                next_larger_element[x] = cur 
            stack.append(idx)
            
    
    while len(stack) > 0:
        x = stack[-1]
        stack.pop()
        next_larger_element[x] = -1
    
    return next_larger_element