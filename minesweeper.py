from tkinter import Button
import random
import config
import ctypes
import sys


class Cell(object):
    # class attributes
    cells = []
    game_over = False
    unrevealed_cells = config.CELL_COUNT

    # constructor
    def __init__(self, row, col, is_mine=False):
        self.row = row
        self.col = col
        self.is_mine = is_mine
        self.is_revealed = False
        self.is_flagged = False
        # each cell is going to be a clickable button
        self.cell_btn = None
        # appending new cell to the cells[]
        Cell.cells.append(self)

    # a method to generate clickable cell button
    def generate_btn(self, loc):
        btn = Button(loc, width=12, height=5)
        btn.bind('<Button-1>', self.handle_left_click)
        btn.bind('<Button-3>', self.handle_right_click)
        self.cell_btn = btn

    # a method to handle the left click event
    def handle_left_click(self, e):
        if self.is_mine:
            self.reveal_mine()
        else:
            if self.calculate_mines_count == 0:
                for cell in self.get_surrounded_cells:
                    cell.reveal_cell()
            self.reveal_cell()

            # In case the reminded cell count is equalled to the mine count, the player won!
            if Cell.unrevealed_cells == config.MINE_COUNT:
                Cell.game_over = True
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won the game!', 'Game Over!', 0)
        # Cancel left and right click actions on a cell once the cell is left-clicked
        self.cell_btn.unbind('<Button-1>')
        self.cell_btn.unbind('<Button-3>')

    # a method to reveal mine
    def reveal_mine(self):
        self.cell_btn.config(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked a mine!', 'Game Over!', 0)
        sys.exit()

    def get_cell_by_axis(self, row, col):
        for cell in Cell.cells:
            if cell.row == row and cell.col == col:
                return cell

    @property
    def get_surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(x, y) for x in range(self.row - 1, self.row + 2) for y in range(self.col - 1, self.col + 2) if (x, y) != (self.row, self.col)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def calculate_mines_count(self):
        count = 0
        for cell in self.get_surrounded_cells:
            if cell.is_mine:
                count += 1
        return count

    def reveal_cell(self):
        if not self.is_revealed:
            Cell.unrevealed_cells -= 1
            self.cell_btn.config(text=f'{self.calculate_mines_count}')
            self.cell_btn.config(bg='SystemButtonFace')
        self.is_revealed = True

    # a method to handle the left click event
    def handle_right_click(self, e):
        if not self.is_flagged:
            self.cell_btn.config(bg='orange')
            self.is_flagged = True
        else:
            self.cell_btn.config(bg='SystemButtonFace')
            self.is_flagged = False

    @staticmethod
    def generate_mines():
        cells = random.sample(Cell.cells, config.MINE_COUNT)
        # setting is_mine to True for randomly picked cells
        for cell in cells:
            cell.is_mine = True

    # magic method
    def __repr__(self):
        return f"Cell({self.row}, {self.col})"
