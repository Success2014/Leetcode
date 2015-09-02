# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 00:59:37 2015
Say you have an array for which the ith element is the price of a given stock 
on day i.

Design an algorithm to find the maximum profit. You may complete at most k 
transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must 
sell the stock before you buy again).

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

Tags Dynamic Programming
Similar Problems (M) Best Time to Buy and Sell Stock 
(M) Best Time to Buy and Sell Stock II (H) Best Time to Buy and Sell Stock III



http://www.cnblogs.com/maples7/p/4350047.html
贪心是不对的。
考虑这样一个样例：
Input: 　　2, [1,2,4,2,5,7,2,4,9,0]
如果用上面那段代码得出的结果会是：12，显然是取了 3~5 和 6~8 这两个区段(list下标号).
但实际上，因为 k 限制在 2，所以可以有更优的解：0~5 和 6~8: 6+7=13。
这样，我们就找了一个反例证明贪心的不正确性（其实也不难直观的去想到）。
实际上，由于 k 的限制，使得决策之间产生了联系，决定了贪心的错误性。
很自然的，做决策求最值，会想到用 DP （动态规划）来完成这道题。

再来思考问题的本质，可以发现这样的特点：
买入和卖出操作是交替执行的，而且卖出之前一定得先买入。
转化为这样的一个数学问题：
给定一个序列，从该序列中找出一个元素保持在原序列中顺序并且元素个数是偶数的子序列，
使得其偶数项之和与奇数项之和的差最大。

而对于每一天来说，只有两种选择，即选择 操作 或者 不操作。
而具体的操作是买入还是卖出得由当前已经执行的操作数是奇偶性来决定。
所以我们可以从天数递增来地推上去直到第n天。

如果用 dp[j] 表示 完成第j次交易时 （由 j-1 转移到 j 必需伴随着一次操作）的最大收益，
则状态转移方程可以写为：

dp[j] = max{dp[j], dp[j-1] + prices[i] * (j%2)?-1:1}

外循环 天数 i 从 0 递推到 size (第 j 次交易不一定发生在哪一天)，内循环 j 从 1 递推
到当前允许的最大操作数：min{2*k, i+1} （i 是 prices 中的 第 i+1 个元素）。

初始条件：dp[0] = 0，dp中的其他值为无穷小（None比任何数值都小）。

另外，有一个优化，当 2*k >= szie 时，k 的限制已经形同虚设了，操作数限制已经可以覆盖
到每一天都允许操作，这种情况下还用上述DP效率太低，可以改为没有k限制的贪心版本（把所
有上升区段跨度求和即为解）。

由于有了上述优化，所以用DP的情况一定是 2*k < size的情况，这种情况下 用完 2*k 次操作
数限制所得的结果一定等于最优解（虽然不一定实际上进行2*k次操作，因为此时实际上放宽了
题目限制条件，在同一个 i 值，dp[j]可能把这个 i 买入使得当前更优（因为初始值为无穷
小），而到了dp[j+1]就把这个 i 卖出使得当前更优，实际上就相当于不操作，但记录的操作
数 j 还是增加了2，所以实际上此时dp[j]表示的准确的实际含义是 最多完成j次交易时（实
际可能不在j次时是最优），放大到全局即为 2*k 处最优。而又因为 i 是递推上去到 n 的，
所以总会有找到 正确的最后一次交易使得在第 i 天dp[2*k]最大，而 i 再增加，操作数已经
不能增加了（已经到了最大的限制）），所以最后的结果为 dp[2*k]。


E.g.:
dp[j] = max{dp[j], dp[j-1] + prices[i] * (j%2)?-1:1}


k=3
i=   0, 1, 2, 3, 4, 5, 6, 7, 8
p=  [4, 2, 6, 3, 4, 1, 8, 2, 6]


dp_j 0, 1, 2, 3, 4, 5, 6
i=0  0,-4
i=1  0,-2, 0
i=2  0,-2, 4,-2
i=3  0,-2, 4, 1, 4
i=4  0,-2, 4, 1, 5, 1
i=5  0,-1, 4, 3, 5, 4, 5
i=6  0,-1, 7, 3,11, 4,12
i=7  0,-1, 7, 5,11, 9,12
i=8  0,-1, 7, 5,11, 9,15

自己心得：
具体的操作是买入还是卖出得由当前已经执行的操作数是奇偶性来决定。
当i<=2k时，就是所有递增数列的和；
当i>2k时，有可能后面出现的递增数列会大于前面的递增数列，所以需要比较。
i>2k后的奇数项就是在寻找可能更低的成本，偶数项就是寻找更高的收益。


每天都可以买进或者卖出。可以当天买进，然后卖出，收益为0.
计算奇数项，是为了计算偶数项。
虽然奇数项，偶数项都是当前操作次数的最大收益，但是感觉奇数项像最低成本，
偶数项像最大收益。


Another example:

k=2
i=  0  1  2   3  4  5
p= [4, 7, 2, 10, 6, 3]

dp_j 0, 1, 2, 3, 4
i=0  0,-4
i=1  0,-4, 3
i=2  0,-2, 3, 1
i=3  0,-2, 8, 1, 11
i=4  0,-2, 8, 2, 11
i=5  0,-2, 8, 5, 11

Another example:

k=2
i=  0  1  2  3  4  5  6  7
p= [5, 3, 1, 8, 9, 7, 1, 9]

dp_j 0, 1, 2, 3, 4
i=0  0,-5, \0,-5, 0
i=1  0,-3, 0,\-3, 0
i=2  0,-1, 0,-1, \0
i=3  0,-1, 7,-1, 7
i=4  0,-1, 8,-1, 8
i=5  0,-1, 8, 1, 8
i=6  0,-1, 8, 7, 8
i=7  0,-1, 8, 7,16
第i天时，只需要算到min(2k,i+1)交易.只要小于2k,多算了的话，也没关系，结果还是正确的。
为什么只需要算到i+1次交易？比如i=0,这是第一天，i+1代表第一次交易，再多的交易也都是
重复。两次交易最大收益必然为0，三次交易最大收益必然还是一次交易的值......


@author: Neo
"""

class Solution:
    # @return an integer as the maximum profit 
    def maxProfit(self, k, prices):
        size = len(prices)
        if k > size / 2:
            return self.quickSolve(size, prices)
        dp = [None] * (2 * k + 1)
        dp[0] = 0
        for i in range(size):
            for j in range(1, min(2 * k, i + 1) + 1):
                dp[j] = max(dp[j], dp[j - 1] + prices[i] * [1, -1][j % 2])
        return dp[2 * k]

    def quickSolve(self, size, prices):
        sum = 0
        for x in range(size - 1):
            if prices[x + 1] > prices[x]:
                sum += prices[x + 1] - prices[x]
        return sum

sol = Solution()        
k1 = 3
k2 = 2
k3 = 2
prices1 = [4,2,6,3,4,1,8,2,6]
prices2 = [4, 7, 2, 10, 6, 3]
prices3= [5, 3, 1, 8, 9, 7, 1, 9]
print sol.maxProfit(k3,prices3)