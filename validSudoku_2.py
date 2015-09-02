# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:26:07 2015

@author: Neo
"""

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        # check row
        for i in xrange(9):
            d = {}
            for j in xrange(9):
                if board[i][j] != ".":
                    if d.has_key(board[i][j]):
                        return False
                    else:
                        d[board[i][j]] = 1
        
        # check column
        for j in xrange(9):
            d = {}
            for i in xrange(9):
                if board[i][j] != ".":
                    if d.has_key(board[i][j]):
                        return False
                    else:
                        d[board[i][j]] = 1
        
        # check sumboard
        for m in [0,3,6]:
            for n in [0,3,6]:
                d = {}
                for i in xrange(3):
                    for j in xrange(3):
                        tmp = board[m+i][n+j]
                        if tmp != ".":
                            if d.has_key(tmp):
                                return False
                            else:
                                d[tmp] = 1
        
        return True
                        
        
        
        