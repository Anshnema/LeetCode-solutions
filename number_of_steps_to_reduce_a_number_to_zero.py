"""
Ques. Number of steps to reduce a number to zero 
==> no // 2 = (no - 1)/2 ====> // opeator subtracts  no by 1 and divides it by 2 at the same time (in 1 step)
T.C. = O(log(n))
S.C. = O(1)
Link - https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
"""
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0 
        
        while num >= 1:
            if(num % 2 == 0 or num == 1):
                num /= 2
                steps += 1 
            else:
                num //= 2
                steps += 2 
        
        return steps 
