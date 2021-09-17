"""
Ques 1. Minimum Window Substring 
len(t) = m; len(s) = n
T.C. - O(m + n)
S.C. - O(m + n)
Link - https://leetcode.com/problems/minimum-window-substring/
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter 
        if(not s or not t):
            return ""
        
        dict_t = Counter(t)
        formed = 0
        required = len(dict_t)
        window_str = {}
        l, r = 0, 0
        ans = (float("inf"), None, None)
        
        while r < len(s):
            ch = s[r]
            if(ch not in window_str):
                window_str[ch] = 1
            else:
                window_str[ch] += 1 
        
            if(ch in dict_t and window_str[ch] == dict_t[ch]):
                formed += 1 
        
            while l <= r and formed == required:
                ch = s[l]
                if(r - l + 1 < ans[0]):
                    ans = (r - l + 1, l, r)
                    
                window_str[ch] -= 1     
                if(ch in dict_t and window_str[ch] < dict_t[ch]):
                    formed -= 1
                
                l += 1 
            r += 1
            
        if(ans[0] == float("inf")):
            return ""
        return s[ans[1] : ans[2] + 1] 
            