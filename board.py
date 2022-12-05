import pygame
from sudoku_generator import generate_sudoku


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.selected_cell = None

        # determines how many cells to remove
        if difficulty == "easy":
            self.removed_cells = 30
        if difficulty == "medium":
            self.removed_cells = 40
        if difficulty == "hard":
            self.removed_cells = 50
    # create the board and keeps it constant
        self.board, self.solved_board= generate_sudoku(9, self.removed_cells)
        self.list1 = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.list1.append(Cell(self.board[i][j], i, j, self.screen))

