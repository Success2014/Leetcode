# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 20:37:45 2015

https://www.youtube.com/watch?v=sYcOK51hl-A

head is the head of the linked list

idea:
keep track of three variables: prev, cur, nxt

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
    def reverseList(self, head): # iterative solution
        if head is None or head.next is None:
            return head
        prev = None
        curt = head
        while curt is not None:
            nxt = curt.next # tracking, temporary variable
            curt.next = prev # doing the job, linked list only need to set this
            prev = curt # tracking
            curt = nxt # tracking
        head = prev
        return head
    def reverseList2(self, head):
        """idea与上面一样，更简洁的实现。每次都只翻转一个指针。"""
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
    
    def reverseList_rec(self, head): # recursive solution
        return self._reverse(head)
        
    def _reverse(self, node, prev = None): # helper function
        if not node:
            return prev
        nxt = node.next
        node.next = prev
        return self._reverse(nxt, node)

            
node1 = ListNode(4)
node2 = ListNode(5)
node3 = ListNode(6)
node1.next = node2
node2.next = node3

#print node1.val
#print node1.next.val
#print node1.next.next.val

sol = Solution()
head = sol.reverseList_rec(node1)
print head.val
print head.next.val
print head.next.next.val

        