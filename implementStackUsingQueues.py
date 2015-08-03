# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 16:13:30 2015

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to 
back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may 
simulate a queue by using a list or deque (double-ended queue), as long as 
you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top 
operations will be called on an empty stack).


@author: Neo
"""
"""一些人用deque实现，其实idea是一样的，比如
https://leetcode.com/discuss/41728/python-solution-o-1-o-n-for-push-48ms
https://leetcode.com/discuss/48641/python-easy-to-understand-solutions-one-queue-two-queues
"""
class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []        

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        """Rotate the array (n-1) times to facilitate pop and top operation"""
        for i in xrange(len(self.stack)-1):
            self.stack.append(self.stack.pop(0))

    # @return nothing
    def pop(self):        
        return self.stack.pop(0)

    # @return an integer
    def top(self):
        return self.stack[0]
        

    # @return an boolean
    def empty(self):
        return len(self.stack) == 0
        


