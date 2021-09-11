"""
Ques. Intersection of 2 array
T.C. = O(n)
S.C. = O(n)
Link - https://leetcode.com/problems/intersection-of-two-arrays/
"""

def intersection(self, nums1, nums2):
        dict1 = {}
        dict2 = {}
        
        for i in nums1:
            if(i not in dict1):
                dict1[i] = 1 
        
        for j in nums2:
            if(j not in dict2):
                dict2[j] = 1
        
        arr = []
        
        for i in dict1:
            if(i in dict2):
                arr.append(i)
                
        return arr
