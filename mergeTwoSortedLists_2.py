# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 10:00:40 2015

@author: Neo
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = ListNode(0)
        head = dummy
        
        while l1 and l2:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
                head = head.next
            else:
                head.next = l1
                l1 = l1.next
                head = head.next
        if l1 is None:
            head.next = l2
            #l2 = l2.next
            #head = head.next
        else:
            head.next =l1
            #l1 = l1.next
            #head = head.next
        
        return dummy.next
                
        