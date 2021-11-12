"""
Ques. Richest Customer Wealth
T.C. = O(m * n)
S.C. = O(1)
Link - https://leetcode.com/problems/richest-customer-wealth/
"""
class Solution:
    def maximumWealth(self, accounts) -> int:
        m = len(accounts)
        n = len(accounts[0])
        
        maxwealth = -1
        wealth = 0 
        
        for i in range(m):
            for j in range(n):
                wealth += accounts[i][j]
            
            if(wealth > maxwealth):
                maxwealth = wealth
                
            wealth = 0
            
        return maxwealth