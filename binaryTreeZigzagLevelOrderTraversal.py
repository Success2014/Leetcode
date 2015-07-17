# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:58:22 2015

Given a binary tree, return the zigzag level order traversal of its nodes' 
values. (ie, from left to right, then right to left for the next level and 
alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
confused what "{1,#,2,3}" means? > read more on how binary tree is 
serialized on OJ.

Tags: Tree Breadth-first Search Stack
Similar Problems: (E) Binary Tree Level Order Traversal


idea:
跟(E) Binary Tree Level Order Traversal相比，只需要多
用一个变量toggle来记录是否应该从后往前加入数值。



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
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        toggle = False
        res = []
        level = []
        que = [root, None]
        while que:
            node = que.pop(0)
            if node is None:
                if toggle:#只多了这么一个if判定
                    res.append(level[::-1])
                else:
                    res.append(level[:])
                level = []
                toggle = not toggle#和这句更新toggle
                if que:
                    que.append(None)
            
            else:
                level.append(node.val)                               
                if node.left:
                    que.append(node.left)
                if node.right:
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
print sol.zigzagLevelOrder(node1)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
