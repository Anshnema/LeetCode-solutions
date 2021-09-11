"""
Ques. First Unique character in a string 
T.C. = O(n)
S.C. = O(1) => The dictionary stores at max 26 elements (26 letters in alphabet)
Link - https://leetcode.com/problems/first-unique-character-in-a-string/
"""
def firstUniqChar(self, s: str) -> int:
   n = len(s)
   ch_map = dict()

   for i in range(n):
      if(s[i] not in ch_map):
            ch_map[s[i]] = 1
      else:
            ch_map[s[i]] += 1 

   for i in range(n):
      if(ch_map[s[i]] == 1):
            return i 
      
   return - 1
