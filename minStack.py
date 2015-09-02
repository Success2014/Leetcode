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

Tags: Stack Data Structure
Similar Problems (H) Sliding Window Maximum

自己思考：如果是Min Queue呢？
http://stackoverflow.com/questions/12054415/get-min-max-in-o1-time-from-a-queue
参考Szymon的解答，他讲的是Max Queue：

There exist such a structure that acts like a queue but lets you retrieve 
min/max value in constant time, actually not strictly constant, it is 
amortized constant time (named min/max queue as you could quess). 
There are to ways of implementing it - using two stacks (and perhaps a queue, 
don't really know how to do it), using a queue and a deque. I know how to 
implement the second but never done anything in Java and so I will try to 
present it not sticking with any language.

so we have a deque of max elements, the one on the front is the desired max, 
and a standard queue.

Push operation:
If the queue is empty, just push the element on both, the queue and the deque.
If the queue is not empty, push the element on the queue, going from the back 
of the deque delete all elements that are strictly less than the one we are 
now pushing (they will surly not be the max, since the pushed element is 
larger and will last on the queue for longer) and push the current element 
on the back of the deque.

Remove operation:
If the front of the deque is equal to the front of the queue then pop both 
(deque from the front).
If the front of the deque is not equal to the front of the queue then pop 
just the queue, the poped element surely is not the largest one.

Get max:
It is just the first element of the deque.

The min version is done analogically.


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
