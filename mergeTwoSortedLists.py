# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:00:57 2015

Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two 
lists.

idea:
就像把两个有序数组变成一个有序数组。
挨个比较，小的添加到新的数组末尾。

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
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
            
        dummy = ListNode(0) # dummy node
        head = dummy # dummy head
        
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
                head = head.next
            else:
                head.next = l2
                l2 = l2.next
                head = head.next
        
        if l1 is None: # l1 is empty, l2 has remaining elements
            head.next = l2
        else:
            head.next = l1

        return dummy.next # exclude the dummy node
        











