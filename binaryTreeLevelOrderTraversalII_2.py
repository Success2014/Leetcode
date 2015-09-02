# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 23:59:36 2015

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
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        if not root:
            return []
        
        que = [root, None]
        res = []
        level = []
        while que:
            node = que.pop(0)
            if node is None:
                res.insert(0,level)
                if que:
                    que.append(None)
                    level = []
            else:
                level.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return res
                    
                    
                    
                    