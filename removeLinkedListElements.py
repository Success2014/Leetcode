# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:56:39 2015

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

Tags: Linked List
Similar Problems (E) Remove Element (E) Delete Node in a Linked List


Solution: 使用指针，注意头结点，涉及到链表的题大抵离不开这两点。

@author: Neo
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        while (head is not None) and head.val == val:
            head = head.next
        if head is None:
            return None
        curt = head
        nxt = curt.next
        while nxt is not None:
            if nxt.val == val:
                nxt = nxt.next
                #curt remain unchanged, temporarily set curt.next
                curt.next = nxt
            else:
                curt = nxt
                nxt = curt.next
        return head
        
        

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(6)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(5)
node7 = ListNode(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

node8 = ListNode(1)
node9 = ListNode(1)
node8.next = node9

def printLinkedList(head):
    tmp = head
    while tmp is not None:
        print tmp.val
        tmp = tmp.next

printLinkedList(node8)
print 

sol = Solution()
head = sol.removeElements(node8, 2)        

printLinkedList(head)
        
        
        
        
        
        
        
        
        