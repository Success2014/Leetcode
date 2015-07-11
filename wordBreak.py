# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 16:21:17 2015


Given a string s and a dictionary of words dict, determine if s can be 
segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

Tag: Dynamic Programming
Similar Problems: (M)Palindrom Partitioning (H)Work BreakII


idea:
Use Dynamic Programming.
DP[i] tracks the state of string of length i.

@author: Neo
"""

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        dp = [False for i in range(len(s)+1)] # +1 for the code in line 32
        dp[0] = True 
        
        for i in xrange(1,len(s)+1):
            for j in xrange(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[len(s)]


s = "leetcode"
wordDict = ["leet", "code"]
sol = Solution()
print sol.wordBreak(s, wordDict)
        
        
        
        