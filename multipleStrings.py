# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 10:07:38 2015

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.


直接乘会溢出，所以每次都要两个single digit相乘，最大81，不会溢出。
比如385 * 97, 就是个位=5 * 7，十位=8 * 7 + 5 * 9 ，百位=3 * 7 + 8 * 9 …
可以每一位用一个Int表示，存在一个int[]里面。
这个数组最大长度是num1.len + num2.len，比如99 * 99，最大不会超过10000，所以4位就够了。
如果个位在后面的，最后相加时不好做，所以干脆先把string reverse了代码就清晰好多。
最后结果前面的0要清掉。

@author: Neo
"""

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        """这个能AC"""
        num1 = int(num1)
        num2 = int(num2)
        
        return str(num1*num2)
    
    def multiply2(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        arr = [0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i+j] += int(num1[i]) * int(num2[j])
        res = []
        for i in xrange(len(arr)):
            digit = arr[i] % 10
            carry = arr[i] / 10
            if i < len(arr) - 1:
                arr[i + 1] += carry
            res.insert(0, str(digit))
        while res[0] == "0" and len(res)>1:
            del res[0]
        return ''.join(res)


sol = Solution()        
print sol.multiply("125","80")
print sol.multiply2("125","80")
print sol.multiply2("0","0")
print sol.multiply2("9133", "0")
