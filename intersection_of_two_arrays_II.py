"""
Ques. Intersection of Two arrays II
T.C. = O(max(m, n)) # m and n represents the length of the arrays nums1 and nums2
S.C. = O(m)
Link - https://leetcode.com/problems/intersection-of-two-arrays-ii/
""" 
class Solution:
    def intersect(self, nums1, nums2):
        dict1 = dict()
        
        for i in nums1:
            if(i in dict1):
                dict1[i] += 1 
            else:
                dict1[i] = 1 
        
        res = []
        for j in nums2:
            if(j in dict1 and dict1[j] != 0):
                res.append(j)
                dict1[j] -= 1 
                
        return res
