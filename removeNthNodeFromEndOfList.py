# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:24:53 2015

Given a linked list, remove the nth node from the end of list and return its 
head. For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, 
   the linked list becomes 1->2->3->5.

Note:

Given n will always be valid.
Try to do this in one pass.

idea:
经典题。双指针，一个指针先走n步，然后两个同步走，直到第一个走到终点(下一个是None)，
第二个指针的下一个节点就是需要删除的节点。
唯一要注意的就是头节点的处理，比如，
1->2->NULL, n =2; 这时，要删除的就是头节点。


@author: Neo
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        
        p1 = dummy
        p2 = dummy
        
        for i in xrange(n):
            p1 = p1.next
        
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
                
        return dummy.next
        
        
        
        
        
        