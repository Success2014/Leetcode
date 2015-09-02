# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:46:10 2015

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
    def levelOrder(self, root):
        if not root:
            return []
        que = [root, None]
        res = []
        tmp = []
        while que:
            node = que.pop(0)
            if node is None:
                res.append(tmp)
                tmp = []
                if len(que) > 0:
                    que.append(None)
            else:
                tmp.append(node.val)
                if node.left:
                    que.append(node.left)
                    
                if node.right:
                    que.append(node.right)
                    
            
        
        return res
        
        