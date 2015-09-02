# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 08:35:51 2015

@author: Neo
"""

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None
        #copy every node
        tmp = head
        while tmp:
            newnode = RandomListNode(tmp.label)
            newnode.next = tmp.next
            tmp.next = newnode
            tmp = tmp.next.next
        #copy random pointer
        tmp = head
        while tmp:
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next
        #split list
        newhead = head.next
        pold = head
        pnew = newhead
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
#        pnew.next = None
        
        return newhead
        
    def copyRandomList2(self, head):
        if not head:
            return None
        
        dummy = RandomListNode(0)
        d = {} # recording the mapping
        # copy list and next pointer
        tmp = head
        newtmp = dummy
        while tmp:
            newnode = RandomListNode(tmp.label)
            newtmp.next = newnode
            d[tmp] = newnode
            tmp = tmp.next
            newtmp = newtmp.next
        
        # copy random pointer
        tmp = head
        newtmp = dummy
        while tmp:
            if tmp.random:
                newtmp.next.random = d.get(tmp.random,None)
            tmp = tmp.next
            newtmp = newtmp.next
        
        return dummy.next
        
        
node1 = RandomListNode(1)
sol = Solution()
print sol.copyRandomList(node1).label
        
        
        