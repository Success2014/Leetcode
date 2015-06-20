# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 16:27:25 2015

Reverse bits of a given 32 bits unsigned integer.
For example, given input 43261596 
(represented in binary as 00000010100101000001111010011100), 
return 964176192 (represented in binary as 00111001011110000010100101000000).
Read from the back to the front.


Follow up:
If this function is called many times, how would you optimize it?


Fast idea:

The key idea of the optimization is to look up a 4 bit chuck and find out
what the reverse is. For example, reverse of 0001 is 1000 (in decimal reverse 
of 1 is 8). Another example, reverse of 1010 is 0101, meaning reverse of 10 is 5.

Based on this idea we could create a look up table:
value -> reverse
0 ------> 0
1 ------> 8
... ------> ...
15 ------> 15

This can be further optimized by using bytes lookup table of size 256 for 8 bits.
This is a trade-off between time complexity and space complexity.
But I am too lazy to generate the table. Note, place the table 
initialization outside the reverseBits() routine is necessary for performance.
In theory, using look up table may improve the performance as we are dealing 
with 4 bits each time. Comparing to the method that iteratively swaps two bits 
each time, the method below should be faster. Given the 600 test cases, the 
performance difference is not dramatic though.

During each iteration, shift the output 4 bits to the left, and discard the 
lowest 4 bits from the input. Make sure the reverse of current lowest 4 bits 
is saved to the current highest 4 bits in the output.


@author: Neo
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in xrange(32):
            ans <<= 1
            ans |= n & 1 # last bit of n
            n >>= 1
            
        return ans
        
    def reverseBitsFast(self, n):
        map_table = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
        ans = 0
        curt = 0
        for i in xrange(8):
            ans <<= 4
            curt = n & 15
            ans |= map_table[curt]
            n >>= 4
        return ans


sol = Solution()
print sol.reverseBits(43261596)













