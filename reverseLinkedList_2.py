# -*- coding: utf-8 -*-
"""
Created on Sun Aug 09 11:44:00 2015

@author: Neo
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):        
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
    
    def reverseList2(self, head):
        return self.helper(head, None)
        
    def helper(self, node, prev):
        if not node:
            return prev
        nxt = node.next
        node.next = prev
        return self.helper(nxt, node)
        