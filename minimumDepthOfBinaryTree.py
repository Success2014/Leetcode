# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:00:45 2015

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root 
node down to the nearest leaf node.

Tags: Tree Depth-first Search Breadth-first Search
Similar Problems (E) Binary Tree Level Order Traversal 
(E) Maximum Depth of Binary Tree


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
    # @return {integer}
    def minDepth(self, root):
        if not root:
            return 0
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
    def minDepth2(self, root):
        """
        use a queue, when all nodes descovered in a level, increase depth by 1 
        """
        if not root:
            return 0
        que = [root]
        depth = 1        
        level_remain = 1 # node not discovered in current depth
        next_level = 0 # number of nodes next level
        while que:
            node = que.pop(0)
            level_remain -= 1
            
            if node.left is not None:
                que.append(node.left)
                next_level += 1
            if node.right is not None:
                que.append(node.right)
                next_level += 1
            
            if node.left is None and node.right is None:
                return depth
            else:
                if level_remain == 0:
                    depth += 1
                    level_remain = next_level
                    next_level = 0
                    
    def minDepth3(self, root):
        """
        use a queue, insert None to separate levels.
        Still need to count the number of nodes in the next level.
        No improvement over the second method.        
        """
        if not root:
            return 0
        
        que = [root, None]
        depth = 0
        while que:
            node = que.pop(0)
            
            if node is None:                
                depth += 1
                if que:
                    que.append(None)
            else:
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
        
        return depth
                
    



node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node2.left = node3
node3.left = node4
node4.left = node5

sol = Solution()
print sol.minDepth2(node1)