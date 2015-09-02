# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 23:03:34 2015

Say you have an array for which the ith element is the price of a given stock 
on day i.

Design an algorithm to find the maximum profit. You may complete as many 
transactions as you like (ie, buy one and sell one share of the stock multiple 
times). However, you may not engage in multiple transactions at the same time 
(ie, you must sell the stock before you buy again).

Tags Array Greedy
Similar Problems (M) Best Time to Buy and Sell Stock 
(H) Best Time to Buy and Sell Stock III (H) Best Time to Buy and Sell Stock IV

idea:

由于可以进行无限次的交易，那么只要是递增序列，就可以进行利润的累加。
只需要看相邻两个数，后面比前面大就可以加到利润里面。
为什么？比如3,5,8，递增数列中间的5并不影响利润是5.
又比如3,5,1,8不是递增数列，但是最大利润就是greedy得来的。
又比如3,5,6,1,8，也是如此。

4,2,6,7,3,4,1,8
    4 1   1   7


@author: Neo
"""

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        maxP = 0
        for i in xrange(len(prices)-1):
            if prices[i+1] > prices[i]:
                maxP += prices[i+1] - prices[i]
        return maxP
            
sol = Solution()
prices1 = [4,2,6,7,3,4,1,8]
print sol.maxProfit(prices1)