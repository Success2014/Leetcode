# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 10:59:58 2015

@author: Neo
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        import heapq
        heap = []
        for list_head in lists:
            if list_head:
                heap.append((list_head.val,list_head))
        
        dummy = ListNode(0)
        head = dummy
        
        heapq.heapify(heap)
        
        while heap:
            node = heapq.heappop(heap)
            head.next = node[1]
            head = head.next
            if node[1].next:
                heapq.heappush(heap,(node[1].next.val,node[1].next))
        
        return dummy.next
        
        
        
        
        
        