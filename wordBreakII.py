# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 16:46:02 2015

Given a string s and a dictionary of words dict, add spaces in s to construct 
a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

Tags: Dynamic Programming Backtracking
Similar Problems: (M)Work Break


idea:
First judge if a string is valid.
If yes, then find the result use DFS.

@author: Neo
"""

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        Solution.res = [] #final result
        self.dfs(s, wordDict, '')
        return Solution.res
        
        
        
    def dfs(self, s, wordDict, string):
        #print self.isValid(s, wordDict)
        if self.isValid(s, wordDict):
            if len(s) == 0:
                Solution.res.append(string[1:])#get rid of first space
                #string = '' #no need to empty it, since for loop below do not change string
            for i in xrange(1,len(s)+1):#开始结束点很关键
                if s[:i] in wordDict:
                    self.dfs(s[i:], wordDict, string + " " + s[:i])
            
        else:
            return 
        
        
    def isValid(self, s, wordDict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        
        for i in xrange(1, len(s)+1):
            for j in xrange(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[len(s)]
        
                
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
   
sol = Solution()
print sol.wordBreak(s,wordDict)
        
        