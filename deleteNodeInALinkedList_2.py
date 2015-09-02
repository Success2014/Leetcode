# -*- coding: utf-8 -*-
"""
Created on Sun Aug 02 16:51:14 2015

@author: Neo
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        