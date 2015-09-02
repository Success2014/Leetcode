# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 09:48:18 2015

@author: Neo
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        
        L = 0
        R = len(nums) - 1
        
        M = (L + R) / 2
        root = TreeNode(nums[M])
        if M > 0:
            root.left = self.sortedArrayToBST(nums[:M])
        if M < R:
            root.right = self.sortedArrayToBST(nums[M+1:])
        return root
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        