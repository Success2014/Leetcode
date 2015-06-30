# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:32:55 2015

Given a string, find the length of the longest substring without repeating 
characters. For example, the longest substring without repeating letters 
for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest 
substring is "b", with the length of 1.

@author: Neo
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        """两个指针i,j。注意碰到重复时,指针i后，新的i前都需要在dict里清掉,清的时候把该清的
        清掉，该留的留下"""
        if not s:
            return 0
        i = 0
        j = 0
        ad = {}
        maxlen = 0
        while j < len(s):
            if ad.has_key(s[j]):                
                maxlen = max(maxlen, j - i) 
                tmp = i
                i = ad[s[j]] + 1                                                               
                for t in range(tmp, ad[s[j]]):
                    ad.pop(s[t], None)                
                ad[s[j]] = j
                
            else:
                ad[s[j]] = j
                maxlen = max(maxlen, j - i + 1)
                
            j += 1        
        return maxlen
    def lengthOfLongestSubstring2(self, s):
        """每次都跟cur当前比。
        cur是当前最长长度，没有重复就直接加1.如果遇到重复，要么就是两个重复的字母的
        距离，要么这个距离太长，就是当前距离加1"""
        d = {}
        res = 0
        cur = 0 # current max length
        for i, c in enumerate(s):
            if c not in d:
                cur += 1
            else:
                cur = min(cur + 1, i - d[c])
            d[c] = i
            res = max(res, cur)
        return res



sol = Solution()
print sol.lengthOfLongestSubstring2("abcefcgcilmno")  
print sol.lengthOfLongestSubstring2("eee")      
print sol.lengthOfLongestSubstring2("au")
print sol.lengthOfLongestSubstring2("tmmzuxt")
print sol.lengthOfLongestSubstring2("aaca")
print sol.lengthOfLongestSubstring2("ejtdfngsdnnkgpkvtigsq")