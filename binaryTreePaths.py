# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 23:15:17 2015

@author: Neo
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        path = ""
        self.dfs(root, res, path)
        return res
        
    
    def dfs(self, node, res, path):        
        if node.left is None and node.right is None:
            if path is not None:
                return res.append(path + str(node.val))
        if node.left:
            self.dfs(node.left, res, path + str(node.val) + "->")
        if node.right:
            self.dfs(node.right, res, path + str(node.val) + "->")
        return

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node1.left = node2
node1.right = node3
node2.left = node4
sol = Solution()
print sol.binaryTreePaths(node1)
        