# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:33:59 2015

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
    # @return {TreeNode}
    def invertTree(self, root): # recursive
        if not root:
            return
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
    
    def invertTreeIter(self, root): # iterative
        if not root:
            return 
        
        node_list = [root]

        while node_list:
            node = node_list.pop(0)            
            
            if node.left:
                node_list.append(node.left)
            if node.right:
                node_list.append(node.right)
            
            node.left, node.right = node.right, node.left
        return root
            


node1 = TreeNode(4)            
node2 = TreeNode(2)
node3 = TreeNode(7)
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(6)
node7 = TreeNode(9)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

print node1.val
print node1.left.val
print node1.right.val
print node1.left.left.val
print node1.left.right.val
print node1.right.left.val
print node1.right.right.val

print 
sol = Solution()
sol.invertTree(node1)

print node1.val
print node1.left.val
print node1.right.val
print node1.left.left.val
print node1.left.right.val
print node1.right.left.val
print node1.right.right.val

