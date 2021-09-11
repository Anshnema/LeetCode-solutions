"""
Ques. Merge-intervals
T.C. = O(n log n)
S.C. = O(n) 
Link - https://leetcode.com/problems/merge-intervals/
"""
def merge(self, intervals):
    intervals.sort()
    ans = []
    start = intervals[0][0]
    end = intervals[0][1]
    
    for i in intervals:
        if(i[0] > end):
            ans.append([start, end])
            start, end = i[0], i[1]
        else:
            end = max(end, i[1])
        
    ans.append([start, end])
    return ans 
    