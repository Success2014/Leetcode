# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 20:29:37 2015

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
    def minDepth(self, root):
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left)+1,self.minDepth(root.right)+1)
        elif root.left:
            return self.minDepth(root.left)+1
        elif root.right:
            return self.minDepth(root.right)+1
        else:
            return 1
    
    def minDepth2(self, root):
        if not root:
            return 0
        depth = 1
        que = [root]
        level_remain = 1
        next_level = 0
        
        while que:
            node = que.pop(0)
            level_remain -= 1
            if node.left:
                que.append(node.left)
                next_level += 1
            if node.right:
                que.append(node.right)
                next_level += 1
            if node.left is None and node.right is None:
                return depth
            
            if level_remain == 0:
                depth += 1
                level_remain = next_level
                next_level = 0
        
        