#!/usr/bin/python3

import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's.
    Args:
        n: integer to initialize

    Return: list of chessboard
    """
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Creates a deepcopy of a chessboard.
    Arg:
        board: chessboard to make copy from.

    Return: a deepcopy of a chessboard.
    """
    if isinstance(board, list):
        return list(map(board_deepcopy, board))

