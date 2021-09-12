"""
Ques. Pascal's triangle
T.C. = O(n ^ 2)
S.C. = O(n ^ 2)
Link - https://leetcode.com/problems/pascals-triangle/
"""
def generate(self, numRows):
    tri = []
    row = []

    for i in range(numRows):
        row = (i + 1) * [1]
        if(len(row) <= 2):
            tri.append(row)             
        else:
            for j in range(len(row)):
                if(0 < j < len(row) -1):
                    row[j] = tri[-1][j] + tri[-1][j - 1]
            tri.append(row)
    return tri 
