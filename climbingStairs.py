# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 12:20:13 2015

爬楼梯问题。经典的动态规划问题。每次上一个台阶或者两个台阶，
问一共有多少种方法到楼顶。这个实际上就是斐波那契数列的求解。
可以逆向来分析问题，如果有n个台阶，那么走完n个台阶的方式有f(n)种。
而走完n个台阶有两种方法，先走完n-2个台阶，然后跨2个台阶；先走完n-1个台阶，
然后跨1个台阶。所以f(n) = f(n-1) + f(n-2)。
f(1)=1, f(2)=2.为了方便定义f(0)=1.

@author: Neo
"""

def climbStairs(n):
    """定义一个数组来存储所有的数, O(n) space complexity"""
    dp = [1 for i in range(n + 1)]
    for i in xrange(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def climbStairs2(n):
    """bottom up, O(1) space complexity"""
    p = 1 
    q = 1
    for i in xrange(2, n + 1):
        tmp = q
        q = p + tmp
        p = tmp
    return q


class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs3(self, n):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            res = 0
            for i in xrange(n/2+1):
                res += self.nChoosek(n-i,i)
            return res

    def fact(self, n):
        """return factorial of a non-negative number"""
        res = 1
        for i in xrange(1, n+1):
            res *= i
        return res
    
    def nChoosek(self, n, k):
        if n == 0:
            return 0
        elif k == 0:
            return 1
        else:
            return self.fact(n)/self.fact(k)/self.fact(n-k)



#print climbStairs(0)
#print climbStairs(5)
#print climbStairs2(0)
#print climbStairs2(5)
sol = Solution()
#print sol.fact(0), sol.fact(4)
#print sol.nChoosek(4,2), sol.nChoosek(5,1)
print sol.climbStairs3(6)