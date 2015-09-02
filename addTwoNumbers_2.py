# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:53:48 2015

@author: Neo
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        res = ListNode(0)
        head = res
        carry = 0
        
        while l1 and l2:
            head.val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) / 10
            
            if l1.next or l2.next:
                nxt = ListNode(0)
                head.next = nxt
                head = head.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            head.val = (l1.val + carry) % 10
            carry = (l1.val + carry) / 10
            
            if l1.next:
                nxt = ListNode(0)
                head.next = nxt
                head = head.next
            l1 = l1.next
        while l2:
            head.val = (l2.val + carry) % 10
            carry = (l2.val + carry) / 10
            
            if l2.next:
                nxt = ListNode(0)
                head.next = nxt
                head = head.next
            l2 = l2.next
        
        if carry == 1:
            nxt = ListNode(1)
            head.next = nxt
            
        return res
        
        
        