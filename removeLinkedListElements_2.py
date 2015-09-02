# -*- coding: utf-8 -*-
"""
Created on Sat Aug 08 20:37:17 2015

@author: Neo
"""

# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if not head:
            return head
        dummy = ListNode(0)
        prev = dummy
        while head:
            if head.val != val:
                prev.next = head
                prev = prev.next
            else:
                prev.next = head.next
            
            head = head.next
        return dummy.next
        
node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
sol = Solution()
print sol.removeElements(node1,1)


        