# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 12:13:57 2015

@author: Neo
"""

class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        self.mins = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        if self.mins:
            if x <= self.mins[-1]:
                self.mins.append(x)
        else:
            self.mins.append(x)

    # @return nothing
    def pop(self):
        if self.stack:
            tmp = self.stack.pop()
        if self.mins and tmp == self.mins[-1]:
            self.mins.pop()
        

    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    # @return an integer
    def getMin(self):
        if self.mins:
            return self.mins[-1]
        else:
            return None
        