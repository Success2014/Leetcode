# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 12:05:51 2015

@author: Neo
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lenA = self.getLen(headA)
        lenB = self.getLen(headB)
        if lenA == 0 or lenB == 0:
            return None
        if lenA < lenB:
            return self.getIntersectionNode(headB, headA)
        for i in xrange(lenA-lenB):
            headA = headA.next
        for i in xrange(lenB):
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
                
    
    def getLen(self,head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count