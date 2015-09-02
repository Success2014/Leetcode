# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 15:36:12 2015

Write a function that takes an unsigned integer and returns the number of 
’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 
00000000000000000000000000001011, so the function should return 3.

Tags: Bit Manipulation
Similar Problems (E) Reverse Bits (E) Power of Two


Brute force solution:
Iterate 32 times, each time determining if the ith bit is a ‘1’ or not. 
This is probably the easiest solution, and the interviewer would probably 
not be too happy about it. This solution is also machine dependent 
(You need to be sure that an unsigned integer is 32-bit). 
In addition, this solution is not very efficient too, as you need to 
iterate 32 times no matter what.

Best solution:
Hint: Remember my last post about making use x & (x-1) to determine if an 
integer is a power of two? Well, there are even better uses for that! 
Remember every time you perform the operation x & (x-1), a 
single 1 bit is erased?


@author: Neo
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count
    def hammingWeightBF(self, n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
        
sol = Solution()
print sol.hammingWeightBF(11)