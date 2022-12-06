import pygame
from cell import *
from sudoku_generator import generate_sudoku


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.selected_cell = None

        # uses the cell amount to the difficulty level
        if difficulty == "easy":
            self.removed_cells = 30
        if difficulty == "medium":
            self.removed_cells = 40
        if difficulty == "hard":
            self.removed_cells = 50
        # make the board
        self.board, self.solved_board = generate_sudoku(9, self.removed_cells)

    def draw(self):
        # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        pygame.draw.line(self.screen, "PINK", (0, self.height - (self.height / 3), self.width, self.height, (self.height / 3)), 3)
        # Draws every cell on this board.
        for i in range(0, 9):
            for j in range(0, 9):
                self.cells[j][i].draw()

    def select(self, row, col):
        # Marks the cell at (row, col) in the board as the current selected cell.
        self.row = row
        self.col = col
        # Once a cell has been selected, the user can edit its value or sketched value.

    def click(self, x, y):
        # If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
        # of the cell which was clicked. Otherwise, this function returns None.


    def clear(self)
    # Clears the value cell. Note that the user can only remove the cell values and sketched value that are filled by themselves.

    def sketch(self, value):
        # Sets the sketched value of the current selected cell equal to user entered value.
        # It will be displayed at top left corner of the cell using in the draw() function

    def place_number(self, value):
        # Sets the value of the current selected cell equal to user entered value.
        # Called when the user presses the Enter key.

    def reset_to_original(self):
        # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).

    def is_full(self):
        # Returns a Boolean value indicating whether the board is full or not.

    def update_board(self):
        # Updates the underlying 2D board with the values in all cells.

    def find_empty(self):
        # Finds an empty cell and returns its row and col as a tuple (x, y).

    def check_board(self):
        # Check whether the Sudoku board is solved correctly.










