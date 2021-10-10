"""
Ques. Peak index in mountain array 
T.C. = O(log n) 
S.C. = O(1)
Link - https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""
def peakIndexInMountainArray(self, arr):
        left = 0
        right = len(arr) - 1
        ans = - 1 
        
        while left <= right:
            mid = (left + right) // 2 
            if(arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]):
                return mid 
            elif(arr[mid] < arr[mid + 1]):
                left = mid + 1 
            else:
                right = mid - 1