"""
Ques. Group Anagrams 
T.C. = O(nk) => Length of each string in n is counted 
S.C. = O(nk) => Information for each n and k is stored in the dictionary

# n = size of strs; k = max length of a string
Link - https://leetcode.com/problems/group-anagrams/
"""
def groupAnagrams(self, strs):
    soln = dict()
        
    for string in strs:
        count = [0] * 26
        
        for i in string:
            count[ord(i) - ord("a")] += 1
            
        if(tuple(count) not in soln.keys()):
            soln[tuple(count)] = [string]
        else:
            soln[tuple(count)].append(string)
    return soln.values()
