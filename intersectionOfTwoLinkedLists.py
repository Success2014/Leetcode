# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:04:21 2015

Write a program to find the node at which the intersection of two singly 
linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function 
returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

Tags: Linked List

idea:
首先这道题目有他的特殊性，这个特殊性就在这里的两个链表如果有交集的话，
那么他们在最后面的一定都是相同的。
所以这里催生了两种想法：

1. 从后往前比较，找到最后形同的那个
2. 从前往后比较，但是这里要用到一个技巧。我们首先要去获取到这两个链表的长度，
然后让长度长的那个先多走长度差的距离，最后再开始比较，第一个相同的即是。


官方：
1. 蛮力法枚举（O(mn) 时间, O(1) 空间）
对于链表A中的每个节点ai，遍历整个链表B，检查B中是否有节点与ai重合

2. 哈希表解法（O(n+m) 时间, O(n) or O(m) 空间）
遍历链表A并将每个节点的地址/引用存储在哈希表中。然后检查链表B中的每个节点bi：
如果bi出现在哈希表中，则bi就是交点。

3. 双指针解法 (O(n+m) 时间, O(1) 空间):
维护两个指针pA和pB，初始分别指向A和B。然后让它们分别遍历整个链表，每步一个节点。
当pA到达链表末尾时，让它指向B的头节点（没错，是B）；类似的当pB到达链表末尾时，
重新指向A的头节点。

如果pA在某一点与pB相遇，则pA/pB就是交点。

下面来看下为什么这个算法可行，考虑两个链表：A = {1,3,5,7,9,11} B = {2,4,9,11}，
它们的交点是节点'9'。由于B的长度是4 小于 A的长度6，pB会首先到达链表的末尾，
由于pB比pA恰好少走2个节点。通过把pB指向A的头，把pA指向B的头，
我们现在让pB比pA恰好多走2个节点。所以在第二轮，它们可以保证同时在交点相遇。

如果两个链表有交点，则它们的最后一个节点一定是同一个节点。
所以当pA/pB到达链表末尾时，分别记录下A和B的最后一个节点。
如果两个链表的末尾节点不一致，说明两个链表没有交点。

如果假设，pA已经走完了A， pB已经走了B和A开头的部分，这个算法其实和自己的
idea是一样的。


@author: Neo
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lenA = self.getListLen(headA)
        lenB = self.getListLen(headB)
        
        if lenA == 0 or lenB == 0:
            return None
        
        if lenA < lenB:
            return self.getIntersectionNode(headB, headA)
        
        for i in xrange(lenA-lenB): # 让一个先走几步(长度之差)
            headA = headA.next
        
        for j in xrange(lenB):
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
    
    def getListLen(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count



sol = Solution()
print sol.getIntersectionNode([],[])






