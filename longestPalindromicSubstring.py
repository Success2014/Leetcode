# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 15:13:18 2015

Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, and there exists one
unique longest palindromic substring.

Tags: String
Similar Problems (H) Shortest Palindrome



@author: Neo
"""

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        """O(n2) runtime, O(1) space – Simpler solution:
        In fact, we could solve it in O(n2) time using only constant space.
        We observe that a palindrome mirrors around its center. Therefore, 
        a palindrome can be expanded from its center, and there are only 2n – 1
        such centers. You might be asking why there are 2n – 1 but not n centers?
        The reason is the center of a palindrome can be in between two letters.
        Such palindromes have even number of letters (such as “abba”) and its 
        center are between the two ‘b’s. Since expanding a palindrome around its 
        center could take O(n) time, the overall complexity is O(n2)."""
        start = 0 #最后返回的起始
        end = 0 #最后返回的末尾
        for i in xrange(len(s)):
            len1 = self.expandhere(s, i, i)
            len2 = self.expandhere(s, i, i + 1)
            lenM = max(len1, len2)
            if lenM > (end - start):
                start = i - (lenM - 1)/2
                end = i + lenM / 2
        return s[start:end+1]#必须+1
        
    def expandhere(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left + 1 - 2 #必须-2，因为退出while后left,right都加了 1
        

sol = Solution()
print sol.longestPalindrome("aa")        