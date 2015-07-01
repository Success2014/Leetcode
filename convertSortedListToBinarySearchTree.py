# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 17:32:03 2015
Given a singly linked list where elements are sorted in ascending order, 
convert it to a height balanced BST.


IMP:
In linked list, you no longer have random access to an element in O(1) time.

Idea:
Convert list to array, then from array to BST. O(n)

@author: Neo
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        if not head:
            return None
        tmp = head
        nums = []
        while tmp:
            nums.append(tmp.val)
            tmp = tmp.next
        return self.sortedArrayToBST(nums)
        
    def sortedArrayToBST(self, nums):
        if not nums:
                return None
            
        n = len(nums)
        mid = n / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root 
        