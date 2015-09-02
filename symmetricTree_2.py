# -*- coding: utf-8 -*-
"""
Created on Sun Aug 09 23:53:36 2015

@author: Neo
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if not root:
            return True
        return self.dfs(root.left, root.right)
        
    def dfs(self, p, q):
        if p is None and q is None:
            return True
        if p and q and p.val==q.val:
            return self.dfs(p.left,q.right) and self.dfs(p.right,q.left)
        else:
            return False
        
    
    def isSymmetric2(self, root):
        if not root:
            return True
        q1 = [root.left]
        q2 = [root.right]
        
        while q1 and q2:
            p1 = q1.pop(0)
            p2 = q2.pop(0)
            
            if p1 is None and p2 is None:
                continue
            if p1 is None or p2 is None:
                return False
            
            if p1.val == p2.val:
                q1.append(p1.left)
                q2.append(p2.right)
                q1.append(p1.right)
                q2.append(p2.left)
            else:
                return False
        
        return True