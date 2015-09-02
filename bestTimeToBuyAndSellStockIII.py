# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 23:29:34 2015

Say you have an array for which the ith element is the price of a given stock 
on day i.

Design an algorithm to find the maximum profit. You may complete at most two 
transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must 
sell the stock before you buy again).

Hide Tags Array Dynamic Programming
Hide Similar Problems (M) Best Time to Buy and Sell Stock 
(M) Best Time to Buy and Sell Stock II (H) Best Time to Buy and Sell Stock IV


idea:
题目规定两次transactions.所以肯定是要找某一天，在这之前完成了一次买卖交易，在这之后
也完成了一次买卖交易。可以这样做：
第一次正向扫描，记录到第i天时的最高收益；当前值减去最小股票值，再与最大值比较。代表
到这一天前的最大收益。
第二次反向扫描，记录到第i天时的最高收益。最大股票值减去当前值，再与最大值比较。代表
从这一天开始交易，最大的收益。
4,2,6,3,4,1,8


@author: Neo
"""
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        
        forward = [0 for i in xrange(len(prices))]
        backward = [0 for i in xrange(len(prices))]
        
        minStock = prices[0]
        maxForward = 0
        for i in xrange(len(prices)):
            if prices[i] < minStock:
                minStock = prices[i]
            maxForward = max(maxForward, prices[i] - minStock)
            forward[i] = maxForward
        
        maxStock = prices[len(prices) - 1]
        maxBackward = 0
        for j in xrange(len(prices)-1, -1, -1):
            if prices[j] > maxStock:
                maxStock = prices[j]
            maxBackward = max(maxBackward, maxStock - prices[j])
            backward[j] = maxBackward
            
        
        res = 0
        for i in xrange(len(prices)):
            if forward[i] + backward[i] > res:
                res = forward[i] + backward[i]
        
        return res
        
     
        
sol = Solution()
prices1 = [2,1,2,0,1]
prices2 = [1,2]
print sol.maxProfit(prices1)
        
        
