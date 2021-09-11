"""
Ques. Valid Parenthesis.
T.C. = O(n)
S.C. = O(n) 
Link - https://leetcode.com/problems/valid-parentheses/
"""
def isValid(self, s: str) -> bool:
    dictionary = {"(": ")","{":"}", "[":"]"}
    
    stack = []
    
    for bracket in s:
        if(bracket in dictionary):
            stack.append(bracket)
        
        else:
            if(len(stack) == 0):
                return False
            else:
                if(dictionary[stack[-1]] != bracket):
                    return False
                stack.pop()
        
    if(len(stack) == 0):
        return True
    return False