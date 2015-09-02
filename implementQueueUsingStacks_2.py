# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 15:56:05 2015

@author: Neo
"""

class Queue:
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
        return self.output.pop()

    # @return an integer
    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
        

    # @return an boolean
    def empty(self):
        return len(self.input)==0 and len(self.output)==0
        