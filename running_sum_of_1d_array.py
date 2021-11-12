"""
Ques. Running sum of 1d array  
T.C. = O(n)
S.C. = O(1)
Link - https://leetcode.com/problems/running-sum-of-1d-array/
"""
class Solution:
    def runningSum(self, nums):
        n = len(nums)
        for i in range(1, n):
            nums[i] = nums[i] + nums[i - 1]
            
        return nums 