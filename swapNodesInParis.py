# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:00:26 2015
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. 
You may not modify the values in the list, only nodes itself can be changed.

Example Questions Candidate Might Ask:
Q: What if the number of nodes in the linked list has only odd number of nodes?
A: The last node should not be swapped.

Solution:
Let’s assume p, q, r are the current, next, and next’s next node.
We could swap the nodes pairwise by adjusting where it’s pointing next:
q.next = p;
p.next = r;
The above operations transform the list from { p -> q -> r -> s } to { q -> p -> r -> s }.
If the next pair of nodes exists, we should remember to connect p’s next to s. Therefore,
we should record the current node before advancing to the next pair of nodes.
To determine the new list’s head, you look at if the list contains two or more elements.
Basically, these extra conditional statements could be avoided by inserting an extra node
(also known as the dummy head) to the front of the list.

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
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        p = head
        prev = dummy
        while p is not None and p.next is not None:
            q = p.next
            r = p.next.next
            
            prev.next = q
            q.next = p
            p.next = r
            prev = p
            p = r
        return dummy.next
        
    def swapPairs2(self, head):
        """recursive."""
        if head is None or head.next is None:
            return head
        
        t = head.next
        head.next = self.swapPairs2(t.next)
        t.next = head
        
        return t
        
        
        