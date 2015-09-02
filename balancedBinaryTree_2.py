# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:19:21 2015

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
    # @return {boolean}
    def isBalanced(self, root):
        if not root:
            return True
        
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
    def height(self,root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
        
    
    def isBalanced2(self, root):
        return self.dfsHeight(root) != -1
        
    def dfsHeight(self,root):
        if not root:
            return 0
        leftHeight = self.dfsHeight(root.left)
        if leftHeight == -1:
            return -1
        rightHeight = self.dfsHeight(root.right)
        if rightHeight == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1