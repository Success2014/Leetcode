# -*- coding: utf-8 -*-
"""
Created on Thu Jul 02 15:33:35 2015
Clone an undirected graph. Each node in the graph contains a label and a list 
of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and 
each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as 
separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming 
a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
         

Solution:
There are two main ways to traverse a graph: breadth-first or depth-first.

O(n) runtime, O(n) space – Depth-first traversal:
A graph is simply represented by a graph node that serves as its starting point. 
In fact, the starting point could be any other graph nodes and it does not affect 
the cloning algorithm.

As each of its neighbors is a graph node too, we could recursively clone each of its
neighbors and assign it to each neighbor of the cloned node. We can easily see that it is
doing a depth-first traversal of each node.
Note that the graph could contain cycles, for example a node could have a neighbor that
points back to it. Therefore, we should use a map that records each node’s copy to avoid
infinite recursion.
         
@author: Neo
"""

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        """DFS"""
        if not node:
            return None
        return self.dfs(node, {})
    
    def dfs(self, node, d):
        if d.has_key(node):
            return d[node]
        node_copy = UndirectedGraphNode(node.label)
        d[node] = node_copy
        for neb in node.neighbors:
            node_copy.neighbors.append(self.dfs(neb,d))
        return node_copy
    
    
    
    def cloneGraph2(self, node):
        """BFS
        A<->B. use a hash table to see if a node has been copied.
        As we copy a node, we insert it into the table. If we later
        find that one of a node’s neighbors is already in the table, 
        we do not make a copy of that neighbor, but to push its neighbor’s 
        copy to its copy instead. Therefore, the hash table would need to 
        store a mapping of key-value pairs, where the key is a node in the 
        original graph and its value is the node’s copy."""
        if not node:
            return None
        newhead = UndirectedGraphNode(node.label)
        queue = [node]
        d = {node : newhead}
        while queue:
            nd = queue.pop(0)           
            nd_copy = d[nd]
            for neb in nd.neighbors:
                if d.has_key(neb):
                    neb_copy = d[neb]
                else:
                    queue.append(neb)
                    neb_copy = UndirectedGraphNode(neb.label)
                    d[neb] = neb_copy
                nd_copy.neighbors.append(neb_copy)
        
        return newhead
            
        
        
        
        
        
        






