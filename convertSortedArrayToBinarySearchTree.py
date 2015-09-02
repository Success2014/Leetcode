# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 17:17:44 2015

Given an array where elements are sorted in ascending order, 
convert it to a height balanced BST.

Tags: Tree Depth-first Search
Similar Problems: (M) Convert Sorted List to Binary Search Tree


@author: Neo
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        """O(n) runtime, O(log n) stack space – Divide and conquer:
            If you would have to choose an array element to be the root of a balanced 
            BST, which element would you pick? The root of a balanced BST should 
            be the middle element from the sorted array.
            You would pick the middle element from the sorted array in each iteration. 
            You then create a node in the tree initialized with this element. 
            After the element is chosen, what is left? Could you identify the 
            sub-problems within the problem? There are two arrays left — The 
            one on its left and the one on its right. These two arrays are the 
            sub-problems of the original problem, since both of them are sorted. 
            Furthermore, they are subtrees of the current node’s left and right child.
            The code below creates a balanced BST from the sorted array in O(n) 
            time (n is the number of elements in the array). Compare how similar 
            the code is to a binary search algorithm. Both are using the divide 
            and conquer methodology. Because the input array could be subdivided 
            in at most log(n) times, the extra stack space used by the recursion is
            in O(log n)."""
        if not nums:
            return None
        
        n = len(nums)
        mid = n / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
        