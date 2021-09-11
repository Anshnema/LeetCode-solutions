"""
Ques. Two Sum
T.C. = O(n)
S.C  = O(n) 
Link - https://leetcode.com/problems/two-sum/
"""
def twoSum(self, nums, target):
    no_map = {}
    n = len(nums)
    
    for i in range(n):
        res = target - nums[i]
        if(res in no_map):
            return [i, no_map[res]]
        else:
            no_map[nums[i]] = i