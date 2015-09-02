# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 17:35:16 2015

Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.

解题思路：归并k个已经排好序的链表。使用堆这一数据结构，首先将每条链表的头节点进入堆中，
然后将最小的弹出，并将最小的节点这条链表的下一个节点入堆，依次类推，
最终形成的链表就是归并好的链表。
@author: Neo
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        """O(nk log k) runtime, O(k) space – Heap.
        We could use a min heap of size k. The heap is first initialized with 
        the smallest element from each list. Then as we extract the nodes out 
        from the heap, we must remember to insert its next node into the heap. 
        As each insert operation into the heap costs log(k) and there are a 
        total of nk elements, the total runtime complexity is O(nk log k).
        
        Ignoring the extra space that is used to store the output list, we 
        only use extra space of O(k) due to the heap.
        
        In python heapq, Heap elements can be tuples."""
        import heapq
        heap = []
        for list_head in lists:
            if list_head:
                heap.append((list_head.val, list_head))
        
        heapq.heapify(heap)
        head = ListNode(0)
        curr = head
        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])# or =pop[1]
            curr = curr.next
            if pop[1].next:
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return head.next