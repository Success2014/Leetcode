# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:16:27 2015
Question:
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits 
and the . character.
The . character does not represent a decimal point and is used to separate 
number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", 
it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:
0.1 < 1.1 < 1.2 < 13.37

Note:

how to compare "0.1" and "0.0.1"


@author: Neo
"""

class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        if len(v1) > len(v2):
            return -1 * self.compareVersion(version2, version1)
        
        for i in xrange(len(v1)):
            if int(v1[i]) > int(v2[i]):
                return 1
            if int(v1[i]) < int(v2[i]):
                return -1
            if int(v1[i]) == int(v2[i]):
                if i == len(v1) - 1 and len(v1) == len(v2):
                    return 0
        
#        if int(v2[-1]) == 0: # Leetcode doesn't consider input 1.1, 1.1.1.0, so he accept this
#            return 0
#        return -1 # have iterated over all of v1
        for j in xrange(i+1, len(v2)):
            if int(v2[j]) != 0:
                return -1
        return 0


sol = Solution()
print sol.compareVersion("1.1","1.1.0.0")
















