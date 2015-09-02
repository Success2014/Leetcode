# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:36:43 2015

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
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head # for single node case
        prev = dummy
        while head and head.next:
            nxt = head.next
            tmp = nxt.next
            
            prev.next = nxt
            nxt.next = head
            head.next = tmp #没有这句的话，最后的节点的next不是None
            
            prev = head
            head = tmp
            
        
        return dummy.next
            
        
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
sol = Solution()
print sol.swapPairs(node1).val
print sol.swapPairs(node1).next.val
#print sol.swapPairs(node1).next.next.val
#print sol.swapPairs(node1).next.next.next.val
        
        
        
        
        