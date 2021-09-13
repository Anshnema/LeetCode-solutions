"""
Ques. Min stack
T.C. = O(1)
S.C. = O(n)
Link - https://leetcode.com/problems/min-stack/
"""
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.NormalStack = list()
        self.MinStack = list()
        
    def push(self, val: int) -> None:
        self.NormalStack.append(val)
        
        if(len(self.MinStack) == 0):
            self.MinStack.append(val)
        else:
            self.MinStack.append(min(val, self.MinStack[-1]))

    def pop(self) -> None:
        self.MinStack.pop()
        self.NormalStack.pop()
        
    def top(self) -> int:
        return self.NormalStack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]
        
