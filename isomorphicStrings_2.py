# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 15:44:25 2015

使用两个哈希表sourceMap和targetMap维护两个字符串中字符的映射关系。

sourceMap[ t[x] ] = s[x]

targetMap[ s[x] ] = t[x]

当出现映射不一致的情形时，返回False

否则返回True

@author: Neo
"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        sMap = {}
        tMap = {}
        for i in xrange(len(s)):
            sm = sMap.get(s[i])
            tm = tMap.get(t[i])
            if sm is None and tm is None:
                sMap[s[i]] = t[i]
                tMap[t[i]] = s[i]
            elif sm != t[i] or tm != s[i]:
                return False
        return True
    
    def isIsomorphic2(self, s, t):
        """s[i]不在dict的key中，t[i]也应该不在dict的value中"""
        dic = {}
        for i in xrange(len(s)):
            if not dic.has_key(s[i]):
                if t[i] not in dic.values():
                    dic[s[i]] = t[i]
                else:
                    return False
            if t[i] != dic[s[i]]:
                return False
        return True