# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 22:27:53 2015

Given a positive integer, return its corresponding column title 
as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 

idea:
使用Python解题时，需要使用ord()函数将字母转化为整数，使用chr()函数将整数转化回字母

@author: Neo
"""

class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        ans = ""
        while n:
            ans = chr(ord('A') + (n - 1) % 26) + ans #  +ans, not ans+
            n = (n - 1 ) / 26 # must be n- 1
        return ans

sol = Solution()    
print sol.convertToTitle(28)













