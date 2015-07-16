# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 10:01:52 2015

Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.

Tags: Hash Table String

anagram的意思是：abc，bac，acb就是anagram。即同一段字符串的字母的不同排序。
将这些都找出来。这里使用了哈希表，即Python中的dict。针对前面的例子来讲，
映射为{abc：abc，bac，acb}。

idea:
Use hash table, where the key is the sorted word.


@author: Neo
"""

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        d = {}
        res = []
        for word in strs:
            word_st = ''.join(sorted(word))
            if word_st in d:
                d[word_st].append(word)
            else:
                d[word_st] = [word]
        
        for key, val in d.items():
            if len(val) > 1:
                res += d[key]
        return res


strs = ['abc','cde','xyz','bca','yzx']
sol = Solution()
print sol.anagrams(strs)