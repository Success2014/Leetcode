# -*- coding: utf-8 -*-
"""
Created on Sat Aug 08 16:15:26 2015

Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

Tags Linked List

idea:
Use 3 pointers: prev, cur, nxt.
The key point is how to delete node with duplicaiton? Use a while loop to get
over all the nodes with duplication.

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
        """"""
        dummy = ListNode(0)#dummy node
        prev = dummy
        cur = head
        while cur:
            nxt = cur.next
            # check if reaching end of list or current has unique value
            if nxt is None or cur.val != nxt.val:
                # attach current to prev and set prev to current
                prev.next = cur
                prev = prev.next
                cur = cur.next
            
            else:
                # iterate through list till different value appears
                while nxt is not None and nxt.val == cur.val:
                    nxt = nxt.next
                # attach next to prev, but keep prev untouched
                # prevent error for [2,3,3,3,4,4,5]
                prev.next = nxt
                cur = nxt
        return dummy.next
        

        