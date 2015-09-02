# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:15:59 2015

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

Tags Backtracking Math
Similar Problems (M) Next Permutation (M) Permutations


idea:
http://www.cnblogs.com/zuoyuan/p/3785530.html

比如
"123"
"132"
"213"
"231"
"312"
"321"
k = 4(!!!注意是第4位,写的时候k要减去1,k=3.因为nums=[1,2,3,4,5,6,7,8,9]没有0.)
第一位应该是(k-1)/(n-1)!,因为抛开第一位数后面还有(n-1)位数，(n-1)!就是确定第一位后
可能有的数,即1XX. 比如d=(k-1)/(n-1)!, d = floor((k-1)/(n-1)!), d*(n-1)!<=k，
意思就是k之前能容纳下d个(n-1)!个数，k的第一位应该是d+1.
计算得到第一个数之后，再利用剩下的余数计算第二位数,让k=k%(n-1)!,第二位数应该是
k/(n-2)!，因为第二位数后面只有(n-2)个数了。
记得把用过的数从candidate中删掉。



@author: Neo
"""
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        res = ''
        k -= 1
        nums = [i for i in xrange(1,n+1)]#at most 9 numbers
        fac = 1
        for i in xrange(1,n):#(n-1)!
            fac *= i
        
        for i in xrange(n-1,-1,-1):#here n-1 is for (n-2)! later
            cur = nums[k / fac]
            res += str(cur)
            nums.remove(cur)
            
            
            if i != 0:#otherwise fac/i will error
                k = k % fac
                fac /= i #(n-2)!,(n-3)!...
        return res
        

sol = Solution()
print sol.getPermutation(3,3)
