# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 23:48:12 2015

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Be care of:

10
/ \
5 15 -------- binary tree not binary search tree, since 6 should not be on the right of 10
  / \
  6 20

idea:
O(n) runtime, O(n) stack space – Top-down recursion:
We can avoid examining all nodes of both subtrees in each pass by passing down 
the low and high limits from the parent to its children.
Refer back to the binary tree above. As we traverse down the tree from node 
(10) to right node (15), we know for sure that the right node’s value fall 
between 10 and +inf. Then, as we traverse further down from node (15) to left 
node (6), we know for sure that the left node’s value fall between 10 and 15. 
And since (6) does not satisfy the above requirement, we can quickly determine 
it is not a valid BST.

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
    # @return {boolean}
    def isValidBST(self, root):
        return self.valid(root, -2147483648-1, 2147483647+1)
        
    def valid(self, p, low, high):
        if p is None:
            return True
        return (p.val > low) and (p.val < high) \
            and self.valid(p.left, low, p.val) and self.valid(p.right, p.val, high)
        
        
        