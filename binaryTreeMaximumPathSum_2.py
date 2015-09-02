# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 00:38:50 2015

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
    # @return {integer}
    def maxPathSum(self, root):
        Solution.max = - 2147483648
        self.findMax(root)
        return Solution.max
        
    def findMax(self, root):
        if not root:
            return 0
        lval = self.findMax(root.left)
        rval = self.findMax(root.right)
        Solution.max = max(Solution.max, root.val + lval + rval)
        maxval = max(lval + root.val, rval + root.val)
        if maxval > 0:
            return maxval
        else:
            return 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        