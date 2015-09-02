# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 15:18:57 2015

@author: Neo
"""

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        d = {}
        que = [node]
        newhead = UndirectedGraphNode(node.label)
        d[node] = newhead
        while que:
            nd = que.pop(0)
            nd_copy = d[nd]
            
            for neb in nd.neighbors:
                
                if neb in d:
                    neb_copy = d[neb]
                else:
                    neb_copy = UndirectedGraphNode(neb.label)
                    d[neb] = neb_copy
                    que.append(neb)
                nd_copy.neighbors.append(neb_copy)
        
        
        
        return newhead
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        