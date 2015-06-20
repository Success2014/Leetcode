# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 15:16:58 2015

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have 
security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of
money of each house, determine the maximum amount of money you can
rob tonight without alerting the police.

动态规划（Dynamic Programming）

状态转移方程：
dp[i] = max(dp[i - 1], dp[i - 2] + num[i - 1])
其中，dp[i]表示打劫到第i间房屋时累计取得的金钱最大值。
时间复杂度O(n)，空间复杂度O(n)

@author: Neo
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        size = len(nums)
        dp = [0] * (size + 1)
        if size:
            dp[1] = nums[0]
        for i in xrange(2, size + 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i - 1])
        return dp[size]
    
    """
    观察可知，上述代码的空间复杂度可以进一步化简为O(1)：
    """
    def rob2(self, nums):
        size = len(nums)
        odd = 0
        even = 0
        for i in xrange(size):
            if i % 2:
                odd = max(odd + nums[i], even)
            else:
                even = max(even + nums[i], odd)
        return max(odd,even)
















