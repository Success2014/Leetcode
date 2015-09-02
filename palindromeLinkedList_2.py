# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 15:11:33 2015

@author: Neo
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if not head:
            return True
        
        slow = head 
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        prev = None
        
        while mid:
            nxt = mid.next
            
            mid.next = prev
            prev = mid
            mid = nxt
        
        p1 = head
        p2 = prev
        
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        
        return True
        
        

        