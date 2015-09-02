# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:42:25 2015

You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a 
single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Tags: Linked List Math
Similar Problems: (M) Multiply Strings (E) Add Binary


solution:
Keep track of the carry using a variable and simulate digits-by-digits sum from the head
of list, which contains the least-significant digit.
Take extra caution of the following cases:
- When one list is longer than the other.
- The sum could have an extra carry of one at the end, which is easy to forget. (e.g.,
(9 -> 9) + (1) = (0 -> 0 -> 1))

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
        dummy = ListNode(0)
        p = dummy
        carry = 0
        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) / 10
            l1 = l1.next
            l2 = l2.next
            p = p.next
        if l1:
            while l1:
                p.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) / 10
                l1 = l1.next
                p = p.next
        if l2:
            while l2:
                p.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) / 10
                l2 = l2.next
                p = p.next
        if carry == 1:
            p.next = ListNode(1)
        
        return dummy.next


n1 = ListNode(9)        
n2 = ListNode(9)
n3 = ListNode(1)
n1.next = n2

sol = Solution()
print sol.addTwoNumbers(n1, n3).val
print sol.addTwoNumbers(n1, n3).next.val
print sol.addTwoNumbers(n1, n3).next.next.val