# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:26:39 2015

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following 
requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Tags Greedy


先从前到后扫描一遍数组，如果序列递增，就+1；然后从后到前扫描一遍数组，序列递增，+1。
注意[4,2,3,4,1]这种情况。
第一遍[1,1,2,3,1],第二遍如果要判断candynum[j] > candynum[j+1],如果成立，代表j已经
比j+1多了，就没必要再给j多加了。



@author: Neo
"""

class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        n = len(ratings)
        if n == 1:
            return 1
        candynum = [1 for i in xrange(n)]
        for i in xrange(1,n):
            if ratings[i] > ratings[i-1]:
                candynum[i] = candynum[i-1] + 1
        for j in xrange(n-2, -1, -1):
            if ratings[j] > ratings[j+1] and candynum[j] <= candynum[j+1]:
                candynum[j] = candynum[j+1] + 1
        
        return sum(candynum)
        
        
        
sol = Solution()        
rating1 = [5,3,1]
print sol.candy(rating1)