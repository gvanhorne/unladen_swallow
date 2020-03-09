class GameBoard(object):
    """Create a 2D array representing the game board."""

    def __init__(self, height, width, value=0):
        self.height = height
        self.width = width
        self.board = [[value] * self.height for n in range(self.width)]

    def mark_cell(self, cell, value):
        self.board[cell[0]][cell[1]] = value

    def make_board(self):
        grid = self.board
        for row in grid:
                print(row)
