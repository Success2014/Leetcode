# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:56:43 2015

@author: Neo
"""

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        res = []
        self.dfs(s, wordDict, res, '')
        return res
        
    def dfs(self, s, wordDict, res, string):
        if len(s) == 0:
            res.append(string[1:])
            return 
        if self.isValid(s, wordDict):
            for i in xrange(1,len(s)+1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], wordDict, res, string + " " + s[:i])
        else:
            return 
        
    def isValid(self, s, wordDict):
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
sol = Solution()        
print sol.wordBreak(s1,wordDict1)