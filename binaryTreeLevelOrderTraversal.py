# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 10:56:10 2015

Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]


idea: BFS. If encounter a None, then current level ends.

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
            
        res = []
        levels = []
        queue = [root, None]
        
        while queue:
            node = queue.pop(0)
            if node is None:
                res.append(levels)
                levels = [] # reset levels
                if queue:
                    queue.append(None)
            else:
                levels.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        
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
print sol.levelOrder(node1)
        
        
        
        
        
        
        
        
        
