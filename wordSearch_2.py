# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 21:59:40 2015

@author: Neo
"""

class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, word[1:], i, j):
                        return True                
        return False
    
    def dfs(self, board, word, x, y):
        if not word:
            return True
        m = len(board)
        n = len(board[0])
        
        #up
        if x > 0 and board[x-1][y] == word[0]:
            board[x][y], tmp = "#", board[x][y]
            if self.dfs(board, word[1:],x-1,y):
                return True
            board[x][y] = tmp
        #down
        if x < m -1 and board[x+1][y] == word[0]:
            board[x][y], tmp = "#", board[x][y]
            if self.dfs(board, word[1:],x+1,y):
                return True
            board[x][y] = tmp
        #left
        if y > 0 and board[x][y-1] == word[0]:
            board[x][y], tmp = "#", board[x][y]
            if self.dfs(board, word[1:],x,y-1):
                return True
            board[x][y] = tmp
        #right
        if y < n - 1 and board[x][y+1] == word[0]:
            board[x][y], tmp = "#", board[x][y]
            if self.dfs(board, word[1:],x,y+1):
                return True
            board[x][y] = tmp
        
        return False

board1 = [['a','a']]
word1 = "aaa"
sol = Solution()
print sol.exist(board1,word1)
            
            
        
        
        
        
        