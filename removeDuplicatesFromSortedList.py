# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:08:48 2015

Given a sorted linked list, delete all duplicates such that each 
element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

Tag: Linked List

idea:
如果遇到重复则把当前节点的next指向下一个的next,并且保持当前节点不动。
如果没有重复，则当前节点到下一个节点。

@author: Neo
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        
        p = head
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
        







