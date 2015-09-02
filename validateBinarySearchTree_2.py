# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:51:22 2015

@author: Neo
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        if not root:
            return True
        low = -2147483648 - 1
        high = 2147483647 + 1
        return self.valid(root,low,high)
        
    def valid(self, p, low, high):
        if not p:
            return True
        return (p.val > low) and (p.val < high) and (self.valid(p.left, low, p.val)) and (self.valid(p.right, p.val, high))
        
        