# -*- coding: utf-8 -*-
"""
Created on Sat Aug 08 21:29:02 2015

@author: Neo
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        """这个实现是快指针先走了n-1步，所以当快指针走到终点，下一个是None时，
        慢指针就是要删除的节点。
        还是走n步，实现方便一点。"""
        if not head:
            return None
        dummy = ListNode(0)
        prev = dummy
        prev.next = head
        slow = head
        fast = head
        for i in xrange(n-1):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
            prev = prev.next
        prev.next = slow.next
        return dummy.next
            
            
        