# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:42:17 2015

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

Tags: Linked List, Two Pointers
Similar Problems:
(E) Palindrome Number (E) Valid Palindrome (E) Reverse Linked List


@author: Neo
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        """O(n) time O(n) space. Use a list to record all the values."""
        vals = []
        while head:
            vals.append(head.val)
            head = head.next            
        return vals == vals[::-1]
    
    def isPalindrome2(self, head):
        """O(n) time O(1) space
        1). 使用快慢指针寻找链表中点
        2). 将链表的后半部分就地逆置，然后比对前后两半的元素是否一致
        3). 恢复原始链表的结构（可选）"""
        if not head:
            return True
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # reverse from the middle    
        mid = slow.next#无论链表长度奇偶，都是这个数开始翻转
        prev = None
        while mid:
            nxt = mid.next
            mid.next = prev
            prev = mid
            mid = nxt
        # check if palindrome use two pointers
        p1 = head # the first one
        p2 = prev # the last one
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
        

sol = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4


print sol.isPalindrome2(node1)

        
        