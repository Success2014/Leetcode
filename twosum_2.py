# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 08:37:41 2015

Given an array of integers, find two numbers such that they add up to a 
specific target number.
The function twoSum should return indices of the two numbers such that 
they add up to the target, where index1 must be less than index2. 
Please note that your returned answers (both index1 and index2) are 
not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

idea: use dictonray for fast search.
Use dictionary to record the index of the found item.

@author: Neo
"""

def twoSum(nums, target):
    allnum = {}
    for ind, num in enumerate(nums):
        tmp = allnum.get(target - num, -1)
        if tmp >= 0:
            return (tmp + 1, ind + 1)
        else:
            allnum[num] = ind
        

numbers = [2,7,11,15]
target = 9

print twoSum(numbers, target)
     