# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 10:44:17 2015

Given a binary tree, return the bottom-up level order traversal of its nodes' 
values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]


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
        res = []
        levels = []
        que = [root, None]
        while que:
            node = que.pop(0)
            if node is None:
                res.insert(0, levels)
                levels = []
                if que:
                    que.append(None)
            else:
                levels.append(node.val)
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
        return res
        
        
        
        
        
        
node1 = TreeNode(3)        
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

sol = Solution()
print sol.levelOrderBottom(node1)        
        
        
        
        
        
        
        