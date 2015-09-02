# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 15:23:08 2015

Given a binary tree, check whether it is a mirror of itself 
(ie, symmetric around its center).
For example, this binary tree is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

OJ's Binary Tree Serialization:
The serialization of a binary tree follows a level order traversal, 
where '#' signifies a path terminator where no node exists below.
Here's an example:
   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}"


@author: Neo
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    """
    recursive.看两个节点是否相等，是看是否本身的值是否相等，
    并且left=right,right=left
    """
    def isSymmetric(self, root):
        if not root:
            return True
        return self.helper(root.left, root.right)
        
    def helper(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 and node2 and node1.val == node2.val:
            return self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)
        return False
        
        
    """
    iterative soluton, use two queues, traverse the tree using BFS
    """        
    def isSymmetricIter(self, root):
        if not root:
            return True
        
        node1 = root.left
        node2 = root.right
        
        q1 = [node1] # queue1, all the left children
        q2 = [node2] # queue2, all the right children
        while q1 and q2: # not return True until queues are both empty
            p1 = q1.pop(0)
            p2 = q2.pop(0)            
            if p1 is None and p2 is None:
                continue
            if p1 is None and p2 is not None:
                return False
            if p1 is not None and p2 is None:
                return False
            if p1.val != p2.val:
                return False
            
            if p1.left is not None: # notice the order
                q1.append(p1.left)                            
            if p2.right is not None:
                q2.append(p2.right)          
            if p1.right is not None:
                q2.append(p1.right)
            if p2.left is not None:
                q1.append(p2.left)            
        
        if len(q1) != len(q2):
            return False
        return True
    
    
    """
    iterative soluton, use two stacks, traverse the tree using DFS
    """        
    def isSymmetricIterS(self, root):
        if not root:
            return True
        
        node1 = root.left
        node2 = root.right
        
        s1 = [node1] # stack1, all the left children
        s2 = [node2] # stack2, all the right children
        
        while s1 and s2:
            p1 = s1.pop()
            p2 = s2.pop()
            
            if p1 is None and p2 is None:
                continue
            if p1 is not None and p2 is None:
                return False
            if p1 is None and p2 is not None:
                return False
            if p1.val != p2.val:
                return False
                
            if p1.left: # notice the order
                s1.append(p1.left)
            if p2.right:
                s2.append(p2.right)
            if p1.right:
                s2.append(p1.right)
            if p2.left:
                s1.append(p2.left)
        
        if len(s1) != len(s2):
            return False
        return True
    
    
    def isSymmetric2(self, root):
        """写法更简洁"""
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
        

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(3)
node5 = TreeNode(4)
node6 = TreeNode(4)
node7 = TreeNode(3)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

sol = Solution()
print sol.isSymmetricIterS(node1)




#http://blog.csdn.net/disappearedgod/article/details/24153001










