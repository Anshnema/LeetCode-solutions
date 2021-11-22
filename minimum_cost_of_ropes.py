"""
Ques. Minimum Cost of ropes 
T.C. = O(n log n)
S.C. = O(n)
Link - https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1
"""
import heapq
class Solution:
    def minCost(self,arr,n) :
        heap = []
 
        for x in arr:
            heapq.heappush(heap, x)
       
        cost = 0    
        while len(heap) != 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            cost += (x + y)
            heapq.heappush(heap, x + y)
 
        return cost