# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 15:43:32 2015

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Tags Tree Depth-first Search


题意：判断两棵树是否是同一棵树。

解题思路：这题比较简单。
用递归来做。首先判断两个根节点的值是否相同，如果相同，递归判断根的左右子树。



@author: Neo
"""

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False


tree1 = TreeNode([0])
tree2 = TreeNode([0])

sol = Solution()
print sol.isSameTree(tree1, tree2)