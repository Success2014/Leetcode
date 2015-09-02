# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:48:53 2015

@author: Neo
"""

class twosumIII:
    def __init__(self):
        self.d = {}
    
    def add(self,x):
        if self.d.has_key(x):
            self.d[x] += 1
        else:
            self.d[x] = 1       
        
    def find(self,y):
        for k in self.d.keys():
            if k + k == y:#要特别注意，如果2k=y的话，不能进下一个判断语句
                if self.d[k] > 1:
                    return True
            else:
                if self.d.has_key(y-k):
                    return True   
        return False
        
        
sol = twosumIII()        
sol.add(1)
sol.add(2)
sol.add(3)
sol.add(4)
sol.add(5)
print sol.find(10)
sol.add(5)
print sol.find(10)
print sol.find(11)