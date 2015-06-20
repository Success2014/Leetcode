# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 15:23:08 2015

Given a binary tree, check whether it is a mirror of itself 
(ie, symmetric around its center).
For example, this binary tree is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

OJ's Binary Tree Serialization:
The serialization of a binary tree follows a level order traversal, 
where '#' signifies a path terminator where no node exists below.
Here's an example:
   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}"


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
    """
    recursive.看两个节点是否相等，是看是否本身的值是否相等，
    并且left=right,right=left
    """
    def isSymmetric(self, root):
        if not root:
            return True
        return self.helper(root.left, root.right)
        
    def helper(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 and node2 and node1.val == node2.val:
            return self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)
        return False
        

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(3)
node5 = TreeNode(4)
node6 = TreeNode(4)
node7 = TreeNode(3)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

sol = Solution()
print sol.isSymmetric([])















