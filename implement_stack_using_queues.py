"""
Ques. Implement Stack Using queues
T.C. = Push - O(n); Pop - O(1); Top - O(1); empty - O(1)
S.C. = O(n) 
1 Queue is used here.
Link - https://leetcode.com/problems/implement-stack-using-queues/
"""
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = list()
  
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)
        n = len(self.queue1)
        while n > 1:
            self.queue1.append(self.queue1.pop(0))
            n -= 1 
 
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue1.pop(0)
    
    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[0]
        
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0