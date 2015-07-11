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
DP[i] tracks the state of string of s[:i].

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
                if dp[j] and s[j:i] in wordDict:#很关键,必须是j,不是i-1
                    dp[i] = True
        return dp[len(s)]


s = "leetcode"
wordDict = ["leet", "code"]
s1 = "catsanddog"
wordDict1 = ["cat", "cats", "and", "sand", "dog"]
sol = Solution()
print sol.wordBreak(s, wordDict)
print sol.wordBreak(s1, wordDict1)
        
        
        
        