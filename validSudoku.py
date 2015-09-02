# -*- coding: utf-8 -*-
"""
Created on Thu Jun 04 09:31:20 2015
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with 
the character '.'.
Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the 
filled cells need to be validated.

idea: 
1. scan each row
2. scan each column
3. scan each subboard

@author: Neo
"""

def isValidSudoku(board):
    
    # check row
    for row in board:
        dup = []
        for box in row:
            if box != '.':
                if box in dup:
                    return False
                else:
                    dup.append(box)
                    
    # check column
    for i in xrange(9):
        dup = []
        for j in xrange(9):
            box = board[j][i]
            if box != '.':
                if box in dup:
                    return False
                else:
                    dup.append(box)
    
    # check each subboard
    for i in [0,3,6]:
        for j in [0,3,6]:
            dup = []
            for m in xrange(3):
                for n in xrange(3):
                    box = board[i+m][j+n]
                    if box != '.':
                        if box in dup:
                            return False
                        else:
                            dup.append(box)
    return True

board = ["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....", \
".15......",".....2...",".2.9.....","..4......"]
print isValidSudoku(board)