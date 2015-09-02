# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 17:20:41 2015

@author: Neo
"""

class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        ps = path.split('/')
        res = []
        for letter in ps:
            if letter == "" or letter == ".":
                pass
            elif letter == "..":
                if res:
                    res.pop()
            else:
                res.append(letter)
        return '/' + '/'.join(res)


sol = Solution()
path = "/..."
print sol.simplifyPath(path)