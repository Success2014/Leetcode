# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:44:40 2015

Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character 
while preserving the order of characters. No two characters may map to 
the same character but a character may map to itself.

For example,
Given "egg", "add", return true.
Given "foo", "bar", return false.
Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

idea:
创建两个字典来反映两个字符串中的映射关系,当映射关系不等时则返回False.
否则"ab","aa"要出错。
不一定要2个字典，如方法3，通过逻辑判断，s[i]不在dict的key中，t[i]也应该不在dict的value中

@author: Neo
"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic2(self, s, t): # much faster
        map_from_s = {} # a:b means a in s is b in t
        map_to_t = {}   # b:a means b in t is a in s
        for i in xrange(len(s)):
            letter_s = s[i]
            letter_t = t[i]
            tmp1 = map_from_s.get(letter_s, None)
            tmp2 = map_to_t.get(letter_t, None)
            if tmp1 is None:
                map_from_s[letter_s] = t[i]
            else:
                if tmp1 != t[i]:
                    return False
            
            if tmp2 is None:
                map_to_t[letter_t] = s[i]
            else:
                if tmp2 != s[i]:
                    return False            
            
        return True
        
    def isIsomorphic(self, s, t):
        dict_s = {} # a:b means a in s is b in t
        dict_t = {} # a:b means a in t is b in s
        
        for i in xrange(len(s)):
            if s[i] in dict_s.keys() and dict_s[s[i]] != t[i]: #slow
                return False
            if t[i] in dict_t.keys() and dict_t[t[i]] != s[i]:
                return False
            dict_s[s[i]] = t[i]
            dict_t[t[i]] = s[i]
            
        return True
    
    def isIsomorphic3(self, s, t):
        if s == t:
            return True
        dic = {}
        
        for i in xrange(len(s)):
            k = s[i]
            if not dic.has_key(k):
                if t[i] not in dic.values():
                    dic[k] = t[i]
                else:
                    return False
            elif t[i] != dic[k]:
                return False
        return True
        
sol = Solution()
s = "paper"
t = "title"

print sol.isIsomorphic3(s,t)        
        
        
        
        
        
        
        
        
        