# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:18:58 2015

A message containing letters from A-Z is being encoded to numbers using the 
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

Tags: Dynamic Programming String


idea:
比如1121.
1 has 1 way.
11 has 2 ways: 1,1 and 11.

对于112,
先看2能不能独立存在，如果能，就表示前一位之前的都可以。
因为 1<=2<=9,所以能独立存在，所以：
1,1, 2
11, 2
都是对的。独立存在，添加在末尾。
再看12能不能独立存在，如果能，就表示前两位的都可以。
因为10<=12<=26,所以能独立存在，所以：
1, 12
是对的。
不用看112能否独立，因为肯定不能，只有1-26的映射。
所以112共有3种。

再看1121.
1能不能独立？能。所以112的3种都是对的。
1,1,2,1
11,2,1
1,12,1
21能不能独立？能。所以11的2种都是对的。
1,1,12
11,12
所以1121一共有5种。


总结一起，一位数看是否在[1,9],两位数看是否在[10,26],再的话就加上。
利用DP的思想。



@author: Neo
"""


class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if not s:
            return 0
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1 # initialize
        if s[0] == "0":
            dp[1] = 0
        else:
            dp[1] = 1
        
        for i in xrange(2, len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if 10<=int(s[i-2:i])<=26:
                dp[i] += dp[i-2]
        
        return dp[len(s)]
        


sol = Solution()        
print sol.numDecodings("1121")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
