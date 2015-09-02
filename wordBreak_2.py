# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:25:24 2015

@author: Neo
"""

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False for i in xrange(n+1)]
        dp[0] = True
        
        for i in xrange(1,n+1):
            for j in xrange(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        
        return dp[n]
        
        
s1 = "a"
wordDict1 = ["a"]
s2 = "hello world you"
wordDict2 = ["hello world you"]
sol = Solution()
print sol.wordBreak(s2, wordDict2)
        
        