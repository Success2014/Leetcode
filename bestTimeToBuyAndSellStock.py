# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:54:30 2015

Say you have an array for which the ith element is the price of a given stock 
on day i.

If you were only permitted to complete at most one transaction (ie, buy one 
and sell one share of the stock), design an algorithm to find the maximum 
profit.

Tags Array Dynamic Programming
Similar Problems (M) Maximum Subarray (M) Best Time to Buy and Sell Stock II 
(H) Best Time to Buy and Sell Stock III (H) Best Time to Buy and Sell Stock IV

idea:
用low来记录最低价格，代表用这个价格买进的。
然后用每天的价格（代表卖出的价格）来减去这个最低价格，计算收益。

@author: Neo
"""

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        
        low = prices[0]
        maxProfit = 0
        for i in xrange(len(prices)):
            if prices[i] < low:
                low = prices[i]
            maxProfit = max(maxProfit, prices[i] - low)
        return maxProfit
        
        
        
        
        
        
        
        