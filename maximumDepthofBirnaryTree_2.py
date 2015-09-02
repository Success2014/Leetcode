# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 19:58:05 2015

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
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
    def maxDepth2(self, root):
        if not root:
            return 0
        depth = 1
        nodes = [root]
        levels = [1]
        while nodes:
            node = nodes.pop()
            l = levels.pop()
            if l > depth:
                depth = l
            if node.left:
                nodes.append(node.left)
                levels.append(l+1)
            if node.right:
                nodes.append(node.right)
                levels.append(l+1)
        return depth