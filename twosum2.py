# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 08:37:41 2015

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
     