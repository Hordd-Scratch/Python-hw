"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    binar = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for o in range(3):
        for x in range(3):
            if board[o][x] == '-':
                return 'unfinished'
            elif board[o][x] == 'o':
                binar[o][x] = 0
            elif board[o][x] == 'x':
                binar[o][x] = 1

    o_bool = False
    x_bool = False

    for i in range(3):
        if binar[i][0] + binar[i][1] + binar[i][2] == 3 or binar[0][i] + binar[1][i] + binar[2][i] == 3:
            x_bool = True
        elif binar[i][0] + binar[i][1] + binar[i][2] == 0 or binar[0][i] + binar[1][i] + binar[2][i] == 0:
            o_bool = True

    if binar[0][0] + binar[1][1] + binar[2][2] == 3 or binar[0][2] + binar[1][1] + binar[2][0] == 3:
        x_bool = True
    if binar[0][0] + binar[1][1] + binar[2][2] == 0 or binar[0][2] + binar[1][1] + binar[2][0] == 0:
        o_bool = True

    if o_bool and x_bool:
        return 'draw '
    elif o_bool:
        return 'o wins'
    elif x_bool:
        return 'x wins'