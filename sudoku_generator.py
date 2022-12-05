"""
Class: COP3502C
Assignment: Project 4
Author: John D'Alessio
Date: 11/24/22
"""
from pprint import pprint
from random import randint
from random import choice
import math
# row length is always 9 and removed_cells could be 30 (easy), 40 (medium), or 50 (hard)


class SudokuGenerator:
    # initializing the generator
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.box_length = int(math.sqrt(row_length))
        self.removed_cells = removed_cells
        self.columns = []
        self.board = []
        for i in range(self.row_length):
            for j in range(self.row_length):
                self.columns.append(0)  # randint(1, 9)
                # I don't know why but the zybooks is only working when I made the default values 1 for the empty
                # spaces, otherwise it says I remove 81 spaces. It may be because I need to get the two functions for
                # making the rest of the board, I just couldn't find them anywhere. I'll talk to the TA if I need to
                # actually input the fill_remaining and fill_values functions instead of just passing them.
            self.board.append(self.columns)
            self.columns = []
# returning the board itself
    def get_board(self):
        return self.board
# printing the board
    def print_board(self):
        pprint(self.board)
# checking if it's valid in a row
    def valid_in_row(self, row, num):
        if num in self.board[row]:
            return False
        else:
            return True

    # checking if it's valid in a column
    def valid_in_col(self, col, num):
        for i in range(len(self.board)):
            if num == self.board[i][col]:
                return False
        return True

    # checking if it's valid in a box
    def valid_in_box(self, row_start, col_start, num):
        for i in range(row_start, row_start+3):
            for j in range(col_start, col_start+3):
                if num == self.board[i][j]:
                    return False
        return True
# checking if it's valid in a box, row or column
    def is_valid(self, row, col, num):
        if row < 3:
            row_start = 0
        elif 2 < row < 6:
            row_start = 3
        elif 5 < row < 9:
            row_start = 6
        if col < 3:
            col_start = 0
        elif 2 < col < 6:
            col_start = 3
        elif 5 < col < 9:
            col_start = 6
        if self.valid_in_box(row_start, col_start, num) and self.valid_in_row(row, num) and self.valid_in_col(col, num):
            return True
        else:
            return False
# filling up a singular box
    def fill_box(self, row_start, col_start):
        unused_in_box = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(row_start, row_start+3):
            for j in range(col_start, col_start+3):
                value = choice(unused_in_box)
                self.board[i][j] = value
                unused_in_box.remove(value)
# filling up the three diagonal boxes
    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)
# filler definitions for the provided ones
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

# removing the cells by storing a list of tuples as coordinates
    def remove_cells(self):
        used_cells = []
        while len(used_cells) < self.removed_cells:
            row = randint(0, 8)
            col = randint(0, 8)
            cell = (row, col)
            if cell in used_cells:
                continue
            else:
                self.board[row][col] = 0
                used_cells.append(cell)
        return self.board

# generating the sukodu board
def generate_sudoku(size, removed):
    sudoku_game = SudokuGenerator(size, removed)
    sudoku_game.fill_values()
    solution_board = sudoku_game.board
    sudoku_game.remove_cells()
    og_board = sudoku_game.board
    return og_board

# Test cases below
# Test_sudoku = generate_sudoku(9,30)
# pprint(Test_sudoku)
# print(Test_sudoku.is_valid(0, 0, 1))
# print(Test_sudoku.is_valid(1, 1, 1))