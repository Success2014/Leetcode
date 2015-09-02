# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 20:17:39 2015

Given a binary tree, find the maximum path sum.
The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

Tags: Tree Depth-first Search
Similar Problems: (E) Path Sum (M) Sum Root to Leaf Numbers


    1
   / \
  2   4
 / \
2   3
return 10.

Q: Does the maximum path have to go through the root node?
A: Not necessarily. For example, the below tree yield 6 as the maximum path 
sum and does not go through root.
   -5
   / \
  2   3
 / \
-1  4

Hint:
Anytime when you found that doing top down approach uses a lot of repeated
calculation, bottom up approach usually is able to be more efficient.

注意是binary tree, 不是BST,没有要求left < node < right.


        1
      /   \
   -2       6
   / \     / \
 -1   4   7   5

=>
        16
      /   \
    2       13
   / \     / \
  0   4   7   5

层层累积到最上面，有可能得到最大，也有可能在下面的子树得到最大7->6->5.
层层累积的过程中，左右两条路径的值，只有一条能被返回。

        1
      /   \
    -2      3
   / \     / \
 100   4   1   2
这样的情况也能找到左下角那个节点。

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
    def maxPathSum(self, root):
        Solution.max = -2147483648
        self.findMax(root)
        return Solution.max

    
    def findMax(self, root):
        """返回当前root下，左右两条路径中，大的那一条，包括root"""
        if not root:
            return 0                
        lval = self.findMax(root.left)            
        rval = self.findMax(root.right)            
        Solution.max = max(Solution.max, root.val + lval + rval)
        maxreturn = max(root.val + lval, root.val + rval)
        if maxreturn > 0:
            return maxreturn
        else:
            return 0
        
node1 = TreeNode(1)
node2 = TreeNode(-2)
node3 = TreeNode(6)
node4 = TreeNode(-1)
node5 = TreeNode(4)
node6 = TreeNode(7)
node7 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

sol = Solution()        
print sol.maxPathSum(node1)