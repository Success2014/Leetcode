# -*- coding: utf-8 -*-
"""
Created on Sat Aug 01 17:08:22 2015

@author: Neo
"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        """use sort. O(nlogn)"""
        return sorted(s) == sorted(t)
    def isAnagram2(self, s, t):
        """O(n) time complexity, O(n) space.
        Use a dictionary to count the appearance of each letter
        in these two strings.
        Every letter you see in s, increase the counter by 1;
        Every letter you see in t, decrease the counter by 1.
        Finally, if any of the counter is not 0, return False."""
        d = {}
        m = len(s)
        n = len(t)
        if m != n:
            return False
        for i in xrange(m):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
            if t[i] in d:
                d[t[i]] -= 1
            else:
                d[t[i]] = -1
        
        for key, val in d.items():
            if val != 0:
                return False
        
        return True

sol = Solution()        
s = "anagram"
t = "nagaram"
print sol.isAnagram2(s,t)