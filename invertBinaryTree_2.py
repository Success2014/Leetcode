# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 14:40:31 2015

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
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return None
        que = [root]
        while que:
            node = que.pop(0)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
            node.left,node.right = node.right,node.left
        return root
            
        