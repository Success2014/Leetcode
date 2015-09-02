# -*- coding: utf-8 -*-
"""
Created on Sun Aug 02 16:44:04 2015

@author: Neo
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if not s:
            return 0
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1
        if s[0] != "0":
            dp[1] = 1
        else:
            dp[1] = 0
        
        for i in xrange(2,len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if 10<=int(s[i-2:i])<=26:
                dp[i] += dp[i-2]
        
        return dp[len(s)]
        
        
        
        
        
        