# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:15:06 2015

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

以前是[4,5,6,7,0,1,2]
现在可能是可能A[L]=A[M]=A[R],比如以下数组找0.
[1,1,1,0,1], [1,0,1,1,1] 可能在M左边，也可能在M右边.
例子中：
A[M]=A[R], 如果因为A[M]和A[R]都大于0，而排出右边就错了。
或者
A[L]=A[M], 如果因为A[L]和A[M]都大于0，而排除左边就错了。

如果只是一边?以下情况不可能。
[4,5,6,2,1,2,2]
除非没有移动过
[0,1,2,3,3,3,3]
否则第一个数，一定比最后一个数大。
或者就是
[4,5,6,2,2,2,2],这种情况一下就找到了。

所以如果第一下(相对的)M没有找到，必然是A[L]=A[M]=A[R].


Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

Tags: Array Binary Search
Similar Problems: (H) Search in Rotated Sorted Array



@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        L = 0
        R = len(nums) - 1
        while L <= R:
            M = (L + R) / 2
            if nums[M] == target:
                return True
                
            if nums[M] == nums[L] == nums[R]:
                L += 1
                R -= 1
                
            elif nums[M] >= nums[L]:#左边有序，必须有等号，否则a1通不过
                if nums[M] > target and nums[L] <= target:
                    R = M - 1
                else:
                    L = M + 1
            else:
                if nums[M] < target and nums[R] >= target:
                    L = M + 1
                else:
                    R = M - 1
        
        return False
                
                
a1 = [3,1]
a2 = [1,1,1,0,1]
a3 = [1,0,1,1,1]
sol = Solution()
print sol.search(a1,1)
print sol.search(a2,0)
print sol.search(a3,0)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        