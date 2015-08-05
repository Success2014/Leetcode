# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 17:01:39 2015

Given an integer array of size n, find all elements that appear more than
 ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

Hint:

How many majority elements could it possibly have?
Tags: Array
Similar Problems (E) Majority Element

idea:
https://leetcode.com/discuss/43248/boyer-moore-majority-vote-algorithm-and-my-elaboration
The essential concepts of Boyer-Moore Majority Vote algorithm 
is you keep a counter for the majority number X. 
If you find a number Y that is not X, the current counter should deduce 1. 
The reason is that if there is 5 X and 4 Y, there would be one (5-4) more X 
than Y. This could be explained as "4 X being paired out by 4 Y".

And since the requirement is finding the majority for more than ceiling of 
[n/3], the answer would be less than or equal to two numbers. So we can 
modify the algorithm to maintain two counters for two majorities.


其实就是把前一题的思路扩展。
因为现在找n/3的众数，最多有2个，不可能有3个。
比如n=5,[n/3]=1,超过1就是2。如果有3个出现2次的数，那至少就有6个数了。
Theoretically, [n/3]最好情况是等于(n-2)/3.大于这个数就是n/3+1/3.
3*(n/3+1/3)=(n+1).所以最多2个。


@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    
    def majorityElement(self, nums):
        n1 = n2 = None
        c1 = c2 = 0
        for num in nums:
            if n1 == num:
                c1 += 1
            elif n2 == num:
                c2 += 1
            elif c1 == 0:
                n1, c1 = num, 1
            elif c2 == 0:
                n2, c2 = num, 1
            else:
                c1, c2 = c1-1, c2-1
        
        length = len(nums)
        return [n for n in (n1,n2) if nums.count(n) > length/3]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        