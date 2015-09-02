# -*- coding: utf-8 -*-
"""
Created on Sat Aug 08 15:08:32 2015

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
    def deleteDuplicates(self, head):
        dummy = head
        while dummy and dummy.next:
            if dummy.val == dummy.next.val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        return head
        
        
        
        
        
        