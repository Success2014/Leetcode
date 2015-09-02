# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 17:27:23 2015

Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different 
ways to solve this problem.
Do not return anything, modify nums in-place instead.

Hint:
Could you do it in-place with O(1) extra space?
Related problem: Reverse Words in a String II

Tags: Array
Hide Similar Problems (M) Rotate List (M) Reverse Words in a String II



@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate1(self, nums, k): # O(k*n) in time, extra space O(1)
        if not nums:
            return None
        k = k % len(nums)
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1
        return nums
    
    def rotate2(self, nums, k): # O(n) in time, extra space O(n)
        if not nums:
            return None
        k = k % len(nums)        
#        nums = nums[-k:] + nums[0:-k] # will fail since new nums created
        nums[:] = nums[-k:] + nums[0:-k]
        return nums
        
    
    
    def rotate3(self, nums, k):
        """利用了Python list就是stack的特性，和方法1一样"""
        k = k % len(nums)
        for i in xrange(k):
            tmp = nums.pop()
            nums.insert(0, tmp)
        
        return nums
    
    def rotate4(self, nums, k):
        """时间复杂度O(n)，空间复杂度O(1)。
        依次平移,注意如果长度n能够被k整除的话，是会cycle的。
        可以用一个变量来记录什么时候cycle,cycle的时候就往前进一步。"""
        n = len(nums)
        k %= n
        idx = 0
        cur = nums[0]
        c = 0 # used to track if cycled
        for i in xrange(len(nums)):
            idx_nxt = (idx + k) % n
            #不能直接交换nums[i],nums[j]. nums[j]要往后放
            #所以先存着，下一次再放
            cur, nums[idx_nxt] = nums[idx_nxt], cur
            
            c = c + k
            if c % n == 0:
                idx = (idx_nxt + 1) % n 
                cur = nums[idx]
            else:
                idx = idx_nxt
        
        return nums    
        
        
    def rotate5(self, nums, k):
        """以n - k为界，分别对数组的左右两边执行一次逆置；
        然后对整个数组执行逆置。"""        
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - k)
        self.reverse(nums, n - k, n)
        self.reverse(nums, 0, n)

    def reverse(self, nums, start, end):
        for x in range(start, (start + end) / 2):
            nums[x] ^= nums[start + end - x - 1]
            nums[start + end - x - 1] ^= nums[x]
            nums[x] ^= nums[start + end - x - 1]
            #上面3行就是互换2个数，也可以用下面代码实现
            #nums[x], nums[start + end - x - 1] = nums[start + end - x - 1], nums[x]
        
        return nums
    
    

sol = Solution()

#print sol.rotate4([1,2,3,4,5,6],3)
print sol.reverse([1,2,3,4],0,3)







