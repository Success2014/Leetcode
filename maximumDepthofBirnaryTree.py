# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 12:52:21 2015

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Tags: Tree Depth-first Search
Similar Problems (E) Balanced Binary Tree (E) Minimum Depth of Binary Tree


@author: Neo
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    """
    recursive
    """
    def maxDepth(self, root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
    """
    iterative, use two stacks, one for node, one for tracking node level
    """
    def maxDepthIter(self, root):
        if root is None:
            return 0
        depth = 1
        stack = [root] # stack
        level = [1]
        while stack:
            s = stack.pop()
            l = level.pop()
            if l > depth:
                depth = l
            if s.left is not None:
                stack.append(s.left)
                level.append(l + 1)
            if s.right is not None:
                stack.append(s.right)
                level.append(l + 1)
        
        return depth
        
