# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 10:27:54 2015

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.


Tags: Array Backtracking
Similar Problems: (H) Word Search II


Idea:
Use DFS.

注意：
tmp, board[x][y] = board[x][y], "#" 
输入只能是list of list.不能是list of string, e.g.["ABCE","SFCS","ADEE"].

@author: Neo
"""

class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        self.m = len(board)
        self.n = len(board[0])
        for i in xrange(self.m):
            for j in xrange(self.n):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, word[1:]):
                        return True
        return False
        
        
    def dfs(self, board, x, y, word):
        """x,y is the position on board. Look up, down, left, right. If matches,
        change it to # so that in later recursion, it will not be used again."""
        #base case
        if len(word) == 0:
            return True
        #up
        if x > 0 and board[x-1][y] == word[0]:
            tmp, board[x][y] = board[x][y], "#" 
#            tmp = board[x][y]
#            board[x] = board[x][:y] + "#" + board[x][y+1:]
            
            if self.dfs(board, x-1, y, word[1:]):
                return True
#            board[x] = board[x][:y] + tmp + board[x][y+1:]
            board[x][y] = tmp
        #down
        if x < self.m - 1 and board[x+1][y] == word[0]:
            tmp, board[x][y] = board[x][y], "#"
#            tmp = board[x][y]
#            board[x] = board[x][:y] + "#" + board[x][y+1:]
            if self.dfs(board, x+1, y, word[1:]):
                return True
#            board[x] = board[x][:y] + tmp + board[x][y+1:]
            board[x][y] = tmp
        #left
        if y > 0 and board[x][y-1] == word[0]:
            tmp, board[x][y] = board[x][y], "#"
#            tmp = board[x][y]
#            board[x] = board[x][:y] + "#" + board[x][y+1:]
            if self.dfs(board, x, y-1, word[1:]):
                return True
#            board[x] = board[x][:y] + tmp + board[x][y+1:]
            board[x][y] = tmp
        #right
        if y < self.n - 1 and board[x][y+1] == word[0]:
            tmp, board[x][y] = board[x][y], "#"
#            tmp = board[x][y]
#            board[x] = board[x][:y] + "#" + board[x][y+1:]
            if self.dfs(board, x, y+1, word[1:]):
                return True
#            board[x] = board[x][:y] + tmp + board[x][y+1:]
            board[x][y] = tmp
        return False
        
        
        
board1 = ["ABCE","SFCS","ADEE"]
board2 = ["bb","ab","ba"]
board3 = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
board4 = [['b','b'],['a','b'],['b','a']]
sol = Solution()
print sol.exist(board3, "ABCCED")
print sol.exist(board4, "a")
        
        
        
        
        
        
        
        
        
        