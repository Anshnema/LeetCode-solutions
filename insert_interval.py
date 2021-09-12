"""
Ques. Insert Interval
T.C. = O(n)
S.C. = O(n)
Link - https://leetcode.com/problems/insert-interval/
"""
def insert(self, intervals, newInterval):
        ans = []
        for i in range(len(intervals)):
            if(intervals[i][1] < newInterval[0]):
                ans.append(intervals[i])
            elif(intervals[i][0] > newInterval[1]):
                ans.append(newInterval)
                return ans + intervals[i:] 
            else:
                if(intervals[i][1] >= newInterval[0] or intervals[i][0] <= newInterval[1]):
                    newInterval[0] = min(intervals[i][0], newInterval[0])
                    newInterval[1] = max(intervals[i][1], newInterval[1])
        
        ans.append(newInterval)
        return ans 