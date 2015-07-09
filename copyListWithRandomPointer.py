# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:31:29 2015

A linked list is given such that each node contains an additional random 
pointer which could point to any node in the list or null.
Return a deep copy of the list.


idea:
http://www.cnblogs.com/zuoyuan/p/3745126.html

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
        """O(n) runtime, O(1) extra space, 复制出来的不算. 
        You need at least O(n) space to keep the list copy, which is for the 
        output. So IMHO, it is correct to say that the space complexity is O(1).
        https://leetcode.com/discuss/22421/solution-constant-space-complexity-linear-time-complexity
        http://www.cnblogs.com/zuoyuan/p/3745126.html
        """
        if not head:
            return head
        # create new nodes            
        tmp = head
        while tmp:
            newNode = RandomListNode(tmp.label)
            newNode.next = tmp.next
            tmp.next = newNode
            tmp = tmp.next.next
        # copy random pointers
        tmp = head
        while tmp:
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next
        # split to two linked lists
        newhead = head.next
        pold = head
        pnew = newhead
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return newhead
    
    def copyRandomList2(self, head):
        """brute force, O(n2) time complexity. Time out on leetcode."""
        if not head:
            return head        
        newhead = RandomListNode(head.label)
        tmp = head
        tmpnew = newhead
        while tmp.next:
            tmp = tmp.next
            newnode = RandomListNode(tmp.label)
            tmpnew.next = newnode
            tmpnew = tmpnew.next
        
        tmpnew = newhead
        tmp = head
        while tmp:
            random_node = tmp.random
            if random_node: # traverse the copied linked list to search for the value
                traverse_node = newhead
                while traverse_node:
                    if traverse_node.label == random_node.label:
                        tmpnew.random = traverse_node
                        break
                    traverse_node = traverse_node.next
            
            tmp = tmp.next
            tmpnew = tmpnew.next
                
        
        return newhead
    
    def copyRandomList3(self, head):
        """O(n) runtime, O(n) space – Hash table.
        用hash table来存储新的node和原node的映射"""
        if not head:
            return head
        
        p = head 
        dummy = RandomListNode(0)
        d = {}
        q = dummy
        # copy nodes and next pointers
        while p:
            q.next = RandomListNode(p.label)
            d[p] = q.next
            p = p.next
            q = q.next
        # copy random pointers
        p = head
        q = dummy
        while p:
            q.next.random = d.get(p.random, None)
            p = p.next
            q = q.next
        return dummy.next
        
        


node1 = RandomListNode(1)
node2 = RandomListNode(2)
node3 = RandomListNode(3)
node1.next = node2
node2.next = node3
node1.random = node3
node2.random = node2
node3.random = node1

node4 = RandomListNode(4)


sol = Solution()
#print sol.copyRandomList3(node1).label
#print sol.copyRandomList3(node1).next.label
#print sol.copyRandomList3(node1).next.next.label
#print sol.copyRandomList3(node1).label
#print sol.copyRandomList3(node1).random.label
#print sol.copyRandomList3(node1).next.random.label


print sol.copyRandomList3(node4).label