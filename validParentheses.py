# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 10:56:23 2015

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

idea:
判断括号匹配的合法性。使用一个栈来解决问题。遇到左括号入栈，遇到右括号，
检查栈顶的左括号是否匹配，如果匹配，弹栈，如果不匹配，返回错误。
如果栈为空，而遇到右括号，同样返回错误。遍历完后，栈如果不空，同样返回错误。

avoid using too many if else statement

@author: Neo
"""

def isValid(s):
    dct = {'(':')', '{':'}', '[':']'}
    
#    if len(s) == 0: # no need
#        return True
    stack = []
    for c in s: # each character in s
        if dct.get(c, None): # left parenthesis
            stack.append(c)
        elif len(stack) == 0 or dct[stack[-1]] != c:
            return False
        else:
            stack.pop()
            
    return True if len(stack) == 0 else False



s = "({}[])"        
print isValid(s)