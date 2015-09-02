# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:10:35 2015

@author: Neo
"""

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        lista = list(a)[::-1]
        listb = list(b)[::-1]
        
        if len(lista) < len(listb): # make sure lista is longer
            lista,listb = listb,lista
        
        carry = 0
        res = []
        for i in xrange(len(lista)):
            if i < len(listb):
                tmp = (int(lista[i]) + int(listb[i]) + carry)%2
                carry = (int(lista[i]) + int(listb[i]) + carry)/2
                res.append(str(tmp))
            else:
                tmp = (int(lista[i]) + carry)%2
                carry = (int(lista[i]) + carry)/2
                res.append(str(tmp))
        if carry == 1:
            res.append('1')
        #print res
#        return ''.join(res.reverse()) # will give error
        # res.reverse() will reverse the list list in place and return None
        return ''.join(reversed(res)) # correct
#        return ''.join(res[::-1]) # correct
                
                
                

sol = Solution()                
print sol.addBinary('1','1')