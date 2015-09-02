# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:33:19 2015

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
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if root.val == sum and (root.left is None and root.right is None):
            return True
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
        
    def hasPathSum2(self, root, sum):
        if not root:
            return False
        #改一点点可以快一些
        if root.left is None and root.right is None:
            return root.val == sum 
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
        
