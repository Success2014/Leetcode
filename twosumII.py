# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:22:36 2015

Same as before. The only difference is that the input array is sorted.

Idea:
1.
Of course we could still apply the [Hash table] approach, but it costs us O(n) 
extra space, plus it does not make use of the fact that the input is already 
sorted.

O(n log n) runtime, O(1) space – Binary search:
For each element x, we could look up if target – x exists in O(log n) time by applying
binary search over the sorted array. Total runtime complexity is O(n log n).

2.
O(n) runtime, O(1) space – Two pointers:
Let’s assume we have two indices pointing to the ith and jth elements, Ai and Aj
respectively. The sum of Ai and Aj could only fall into one of these three possibilities:
i. Ai + Aj > target. Increasing i isn’t going to help us, as it makes the sum even
bigger. Therefore we should decrement j.
ii. Ai + Aj < target. Decreasing j isn’t going to help us, as it makes the sum even
smaller. Therefore we should increment i.
iii. Ai + Aj == target. We have found the answer.



@author: Neo
"""

def twoSum(nums, target):
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] == target:
            return (i + 1, j + 1)
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
        
    
nums = [1,2,3,4,5,9,12,15,19,20,22,24]
print twoSum(nums, 35)
    
    
    
    
    

