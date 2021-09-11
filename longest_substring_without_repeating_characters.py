"""
Ques. Longest substring without repeating characters
T.C. - O(n)
S.C. - O(n)
Link - https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
def lengthOfLongestSubstring(self, s: str) -> int:
    str_map = {}
    start = 0
    end = 0
    length = 0
    max_len = 0
    n = len(s)
    
    while end < n:
        if(s[end] not in str_map):
            str_map[s[end]] = True
            length = end - start + 1 
            max_len = max(max_len, length)
            end += 1 
        else:
            while s[end] in str_map:
                str_map.pop(s[start])
                start += 1 
    
    return max_len
    