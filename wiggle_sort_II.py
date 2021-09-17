"""
Ques. Wiggle Sort.
T.C. = O(n log n)
S.C. = O(n)
Link - https://leetcode.com/problems/wiggle-sort-ii/
"""
class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = sorted(nums)
        i, j = 1, len(nums) - 1
        
        while j >= 0:
            if(i > len(nums) - 1):
                i = 0
            nums[i] = ans[j]
            i += 2 
            j -= 1 
