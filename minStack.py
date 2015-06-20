# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:39:22 2015
Question:
Design a stack that supports push, pop, top, and retrieving
the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Hints from clean code hand book:
Consider space-time tradeoff. How would you keep track of the minimums using
extra space?
Make sure to consider duplicate elements.

@author: Neo
"""

class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.stack = []
        self.minstack = []
        
    def push(self, x):
        self.stack.append(x)
        if len(self.minstack) == 0 or x <= self.minstack[-1]: # must be <=, otherwise 0,1,0 would fail
            self.minstack.append(x)
        

    # @return nothing
    def pop(self):
        tmp = self.stack.pop()
        if tmp == self.minstack[-1]:
            self.minstack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]
        

    # @return an integer
    def getMin(self):
        return self.minstack[-1]

    def __str__(self):
        return str(self.stack).strip('[]')




ms = MinStack()
ms.push(0)
ms.push(1)        
ms.push(0)
print ms.getMin()
ms.pop()
print ms.getMin()
