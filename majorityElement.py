# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:10:50 2015

Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always 
exist in the array.

Tags: Divide and Conquer Array Bit Manipulation
Similar Problems (M) Majority Element II


Answers:

1. Runtime: O(n2) — Brute force solution: 
Check each element if it is the majority element.

2. Runtime: O(n), Space: O(n) — Hash table: 
Maintain a hash table of the counts of each element, then find the most common one.

3. Runtime: O(n log n) — Sorting: As we know more than 
half of the array are elements of the same value, we can 
sort the array and all majority elements will be grouped 
into one contiguous chunk. Therefore, the middle (n/2th) 
element must also be the majority element.

4. Average runtime: O(n), Worst case runtime: Infinity — Randomization: 
Randomly pick an element and check if it is the majority element. 
If it is not, do the random pick again until you find the majority element. 
As the probability to pick the majority element is greater than 1/2, 
the expected number of attempts is < 2.

5. Runtime: O(n log n) — Divide and conquer: Divide the array into two halves, 
then find the majority element A in the first half and the majority element B 
in the second half. The global majority element must either be A or B. If A == B, 
then it automatically becomes the global majority element. If not, then both A 
and B are the candidates for the majority element, and it is suffice to check 
the count of occurrences for at most two candidates. The runtime complexity, 
T(n) = T(n/2) + 2n = O(n log n).

6. Runtime: O(n) — Moore voting algorithm: We maintain a current candidate 
and a counter initialized to 0. As we iterate the array, we look at the current element x:
If the counter is 0, we set the current candidate to x and the counter to 1.
If the counter is not 0, we increment or decrement the counter based on whether 
x is the current candidate.
After one pass, the current candidate is the majority element. 
Runtime complexity = O(n).

7. Runtime: O(n) — Bit manipulation: We would need 32 iterations, each calculating the number of 1's for the ith bit of all n numbers. Since a majority must exist, therefore, either count of 1's > count of 0's or vice versa (but can never be equal). The majority number’s ith bit must be the one bit that has the greater count.

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        nums_dict = {}
        n = len(nums)
        
        for num in nums:
            if nums_dict.has_key(num):                
                nums_dict[num] += 1
                if nums_dict[num] > n/2:
                    return num
            else:
                nums_dict[num] = 1
                if nums_dict[num] > n/2:
                    return num
    """
    思想可以延伸到出现次数大于n/k的情况（当然基于hash的方法也可以）
    """
    def majorityElement2(self, nums): 
        """moore voting algorithm, count must be > 0 at last
        最多只有1个这样的数。[n/2]=n/2 or (n-1)/2.大于[n/2],则需要
        (n/2 + 1) or (n+1)/2.两个这样的数则总共需要(n+2) or (n+1)个数。"""
        if len(nums) == 1:
            return nums[0]
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate


sol = Solution()
print sol.majorityElement2([1,2,2,2,3,2])

