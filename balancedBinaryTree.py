# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:25:39 2015

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in 
which the depth of the two subtrees of every node never differ by more than 1.


Tag: Tree Depth-first Search
Similar Problems: (E) Maximum Depth of Binary Tree




idea:
在这道题里，平衡二叉树的定义是二叉树的任意节点的两颗子树之间的高度差小于等于1。
这实际上是AVL树的定义。首先要写一个计算二叉树高度的函数，二叉树的高度定义为：
树为空时，高度为0。然后递归求解：
树的高度 = max(左子树高度，右子树高度)+1(根节点要算上)。高度计算函数实现后，
递归求解每个节点的左右子树的高度差，如果有大于1的，则return False。
如果高度差小于等于1，则继续递归求解。




https://leetcode.com/discuss/22898/the-bottom-up-o-n-solution-would-be-better

This problem is generally believed to have two solutions: 
the top down approach and the bottom up way.

1.The first method checks whether the tree is balanced strictly according to 
the definition of balanced binary tree: the difference between the heights of 
the two sub trees are not bigger than 1, and both the left sub tree and right 
sub tree are also balanced. With the helper function depth(), we could easily 
write the code;

class solution {
public:
    int depth (TreeNode *root) {
        if (root == NULL) return 0;
        return max (depth(root -> left), depth (root -> right)) + 1;
    }

    bool isBalanced (TreeNode *root) {
        if (root == NULL) return true;

        int left=depth(root->left);
        int right=depth(root->right);

        return abs(left - right) <= 1 && isBalanced(root->left) 
        && isBalanced(root->right);
    }
};
For the current node root, calling depth() for its left and right children 
actually has to access all of its children, thus the complexity is O(N). 
We do this for each node in the tree, so the overall complexity of isBalanced 
will be O(N^2). This is a top down approach.

2.The second method is based on DFS. Instead of calling depth() explicitly for 
each child node, we return the height of the current node in DFS recursion. 
When the sub tree of the current node (inclusive) is balanced, the function 
dfsHeight() returns a non-negative value as the height. Otherwise -1 is 
returned. According to the leftHeight and rightHeight of the two children, 
the parent node could check if the sub tree is balanced, and decides its 
return value.

class solution {
public:
int dfsHeight (TreeNode *root) {
        if (root == NULL) return 0;

        int leftHeight = dfsHeight (root -> left);
        if (leftHeight == -1) return -1;
        int rightHeight = dfsHeight (root -> right);
        if (rightHeight == -1) return -1;

        if (abs(leftHeight - rightHeight) > 1)  return -1;
        return max (leftHeight, rightHeight) + 1;
    }
    bool isBalanced(TreeNode *root) {
        return dfsHeight (root) != -1;
    }
};
In this bottom up approach, each node in the tree only need to be accessed 
once. Thus the time complexity is O(N), better than the first solution.


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
    def isBalanced(self, root):
        """top down, worst case O(N^2), average O(NlogN)"""
        if not root:
            return True
        if abs(self.treeHeight(root.left) - self.treeHeight(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def treeHeight(self, root):
        if not root:
            return 0
        return max(self.treeHeight(root.left), self.treeHeight(root.right)) + 1
    
    def isBalanced2(self, root):
        """bottom up, O(N)"""
        return self.dfsHeight(root) != -1
        
    def dfsHeight(self, root):
        if not root:
            return 0
        leftHeight = self.dfsHeight(root.left)
        if leftHeight == -1:
            return -1
        rightHeight = self.dfsHeight(root.right)
        if rightHeight == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1

        