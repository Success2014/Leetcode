# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:24:47 2015

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
Tags Dynamic Programming Backtracking Greedy String
Similar Problems (H) Regular Expression Matching

idea:
http://yucoding.blogspot.com/2013/02/leetcode-question-123-wildcard-matching.html
*可以是0个或者任意多个，任意的字符。
分别用两个指针分别逐个扫描两个string.
如果相等或者问号，则下一个。
如果遇到*，保存两个指针当前位置和*的位置。
如果还不是，则检查上一个*的位置。从上一个*位置的下一个位置开始匹配。
如果都不是，那就返回错误。
比如：
xyabcabd
xy*abd

遇到*后，先把*当做空白看待，看后面的abd,发现不对就返回把*看做a,还是不对就把*看做ab,
还是不对就把*看做abc,这下就对了。

最后可能末尾还剩几个*，都是合法的。

@author: Neo
"""

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        scur = 0#current position in s
        pcur = 0#current position in p
        star = -1#most recent position of *
        match = 0#before this postion, s,p are matched
        while scur < len(s):
            if pcur < len(p) and (s[scur] == p[pcur] or p[pcur] == "?"):
                scur += 1
                pcur += 1                
            elif pcur < len(p) and p[pcur] == "*":
                match = scur
                star = pcur
                pcur += 1
            elif star != -1:
                pcur = star + 1
                match += 1
                scur = match                 
            else:
                return False
        
        while pcur < len(p) and p[pcur] == "*":
            pcur += 1
        
        return pcur == len(p)
                

s1 = "aa"
p1 = "*"
s2 = "hi"
p2 = "*?"
s3 = "aabcde"
p3 = "a*bcd*"

sol = Solution()
print sol.isMatch(s3,p3)