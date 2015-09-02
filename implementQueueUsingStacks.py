# -*- coding: utf-8 -*-
"""
Created on Thu Jul 09 00:08:13 2015

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, 
peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate 
a stack by using a list or deque (double-ended queue), as long as you use only 
standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek 
operations will be called on an empty queue).

Tags: Stack Data Structure
Similar Problems (E) Implement Stack using Queues



@author: Neo
"""

"""这个方法是错的。没有用stack来实现queue"""
class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.queue = []
        

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue.append(x)
        

    # @return nothing
    def pop(self):
        self.queue.pop(0)

    # @return an integer
    def peek(self):
        return self.queue[0]

    # @return an boolean
    def empty(self):
        return len(self.queue)==0

"""Use two stacks.I have one input stack, onto which I push the incoming 
elements, and one output stack, from which I peek/pop. I move elements from 
input stack to output stack when needed, i.e., when I need to peek/pop but 
the output stack is empty. When that happens, I move all elements from input 
to output stack, thereby reversing the order so it's the correct order for 
peek/pop.

The loop in peek does the moving from input to output stack. Each element only 
ever gets moved like that once, though, and only after we already spent time 
pushing it, so the overall amortized cost for each operation is O(1)."""
class Queue2:
    # initialize your data structure here.
    def __init__(self):
        self.input = []
        self.output = []
        

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.input.append(x)
        

    # @return nothing
    def pop(self):
        self.peek()
        self.output.pop()

    # @return an integer
    def peek(self):
        if len(self.output) == 0:
            while not len(self.input) == 0:
                self.output.append(self.input.pop())
        return self.output[-1]

    # @return an boolean
    def empty(self):
        return len(self.input)==0 and len(self.output)==0


sol = Queue2()        
sol.push(1)
sol.push(2)
print sol.peek()
sol.push(3)
print sol.peek()