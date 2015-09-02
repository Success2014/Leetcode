# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:12:10 2015

Similar to Question [6. Reverse Words in a String], but with the following 
constraints:
“The input string does not contain leading or trailing spaces and the words 
are always separated by a single space.”
Could you do it in-place without allocating extra space?

idea: 先把每个单词翻转，再把整个句子翻转。或者先把整个句子翻转，再把每个单词翻转。
"the sky is blue"
"eht yks si eulb"
'blue is sky the'
or
"eulb si yks eht"
"blue is sky the"

可以用"word"[::-1]来翻转单词，挑战：不用这个


好像不行
s = "hello"
s[0] = 'a'
TypeError: 'str' object does not support item assignment



@author: Neo
"""

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        self.rev(s, 0, len(s)-1)
        i = 0
        for j in xrange(len(s)):
            if s[j].isspace() or j == len(s) -1:
                self.rev(s,i,j)
                i = j + 1
        return s
        
    def rev(self, s, begin, end):
        for i in xrange(0, (end-begin)/2):
            tmp = s[begin + i]
            s[begin + i] = s[end - i]
            s[end - i] = tmp
        

s = "the sky is blue"           
sol = Solution()        
print sol.reverseWords(s)
