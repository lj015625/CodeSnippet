""" According to Wikipedia's article: "The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
1) Any live cell with fewer than two live neighbors dies as if caused by under-population.
2) Any live cell with two or three live neighbors lives on to the next generation.
3) Any live cell with more than three live neighbors dies, as if by over-population.
4) Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
Given the current state of the m x n grid board, return the next state."""


def gameOfLife(board):
    """
    :type board: List[List[int]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    m = len(board)  # row
    n = len(board[0])  # column
    # use deep copy
    copy = []
    for i in range(len(board)):
        arr = []
        for j in range(len(board[0])):
            arr.append(board[i][j])
        copy.append(arr)

    for i in range(m):
        for j in range(n):
            top_left = copy[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0
            top_middle = copy[i - 1][j] if i - 1 >= 0 else 0
            top_right = copy[i - 1][j + 1] if i - 1 >= 0 and j + 1 < n else 0
            left = copy[i][j - 1] if j - 1 >= 0 else 0
            right = copy[i][j + 1] if j + 1 < n else 0
            bottom_left = copy[i + 1][j - 1] if i + 1 < m and j - 1 >= 0 else 0
            bottom_middle = copy[i + 1][j] if i + 1 < m else 0
            bottom_right = copy[i + 1][j + 1] if i + 1 < m and j + 1 < n else 0
            total = top_left + top_middle + top_right + left + right + bottom_left + bottom_middle + bottom_right

            # apply Conway's rules
            if board[i][j] == 1 and total < 2 or total > 3:  # Rule 1 or Rule 3
                board[i][j] = 0
            elif board[i][j] == 0 and total == 3:  # Rule 4
                board[i][j] = 1
    return board


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
print(board)
print(gameOfLife(board))

""" Save memory. """
def gameOfLife2(board):
    """
    :type board: List[List[int]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    m = len(board)  # row
    n = len(board[0])  # column
    directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    for i in range(m):
        for j in range(n):
            total = 0
            for x, y in directions:  # check and count neighbors in all directions
                # 1 is live, 2 is previous live
                if (m > i + x >= 0) and (n > j + y >= 0) and (board[i + x][j + y] == 1 or board[i + x][j + y] == 2):
                    total += 1

            # apply Conway's rules
            if board[i][j] == 1 and (total < 2 or total > 3):  # current live -> next died
                board[i][j] = 2
            elif board[i][j] == 0 and total == 3:  # current died -> next live
                board[i][j] = 3
    # reset board to 1s and 0s
    for i in range(len(board)):
        for j in range(len(board[0])):
            # live, or next live
            if board[i][j] in (1, 3):
                board[i][j] = 1
            else:
                board[i][j] = 0
    return board


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
print(board)
print(gameOfLife2(board))
