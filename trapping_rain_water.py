"""
Ques. Trapping Rain Water 
T.C. = O(n)
S.C. = O(1)
Link - https://leetcode.com/problems/trapping-rain-water/
"""
class Solution:
    def trap(self, height):
        i = 0
        j = len(height) - 1
        maxleft = 0
        maxright = 0
        water = 0 
        
        while i < j: 
            if(height[i] <= height[j]):  
                maxleft = max(height[i], maxleft)
                water += maxleft - height[i]
                i += 1 
            else: 
                maxright = max(height[j], maxright)
                water += maxright - height[j]
                j -= 1 
                
        return water 