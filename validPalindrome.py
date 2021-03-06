# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:20:57 2015

Given a string, determine if it is a palindrome, considering only alphanumeric 
characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to 
ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.

Tags: Two Pointers String
Similar Problems (E) Palindrome Linked List


idea: two pointers, one left, one right. remember to convert to lower case

@author: Neo
"""

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        if not s:
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
            else:
                if not s[left].isalnum():
                    left += 1
                if not s[right].isalnum():
                    right -= 1
        return True
        

sol = Solution()        
print sol.isPalindrome("Abcba")