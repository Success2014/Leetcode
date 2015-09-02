# -*- coding: utf-8 -*-
"""
Created on Sun Aug 02 22:05:13 2015

@author: Neo
"""

class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        stack = []
        operators = ["+","-","*","/"]
        for s in tokens:
            if s not in operators:
                stack.append(int(s))
            
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if s == "+":
                    stack.append(b+a)
                elif s == "-":
                    stack.append(b-a)
                elif s == "*":
                    stack.append(b*a)
                else:
                    if a*b < 0:
                        stack.append(-(-b/a))
                    else:
                        stack.append(b/a)
        
        return stack[0]