# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:40:28 2015

@author: Neo
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        if not head:
            return None
        
        array = []
        tmp = head
        while tmp:
            array.append(tmp.val)
            tmp = tmp.next
        newhead = self.helper(array)
        return newhead
        
    def helper(self, array):
        if not array:
            return None
        M = (len(array)-1)/2
        root = TreeNode(array[M])
        root.left = self.helper(array[:M])
        root.right = self.helper(array[M+1:])
        return root
        
        
        
        
        
        
        
        
        
        
        
        