# -*- coding: utf-8 -*-
"""
Created on Sun Aug 09 12:08:25 2015

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

Tags Linked List
Similar Problems (E) Reverse Linked List

idea:
题目主要考察链表的“就地逆置”操作（不改变链表的值，只操作指针）。

链表的就地逆置代码片段如下：

def reverse(head):
    p = head
    start = None
    while p
        next = p.next
        p.next = start
        start = p
        p = next
    return start

在上述代码的基础上，先用两个指针，一个走到第m个节点，一个走到第m-1个节点。
将原链表经过逆置部分及其前后的链表片段拼接即可。

使用“哑节点”（dummy node），可以使代码简化。



@author: Neo
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        """最重要的三个指针：prev, start,end"""
        if m == n:
            return head
        dummy = ListNode(0)
        prev = dummy
        node = head
        
        for i in xrange(m-1):
            prev.next = node
            prev = prev.next
            node = node.next
        
        start = node#开始反转的位置，反转后在末尾
        tmp = None
        
        for j in xrange(m, n+1):
            nxt = node.next
            node.next = tmp
            tmp = node
            node = nxt
        end = tmp#结束反转的位置，反转后在开头
        
        prev.next = end
        start.next = nxt
        
        return dummy.next
        
        
        
        
        
        
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

sol = Solution()
print sol.reverseBetween(node1,2,4).val

        
        
        
        




