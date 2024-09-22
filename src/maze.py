from src.cell import Cell
from src.geometry import Point
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, wnd):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._wnd = wnd
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_rows):
            column = []
            for j in range(self.num_cols):
                cell = Cell(self._wnd)
                column.append(cell)
            self._cells.append(column)

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(self._cells[i][j], i, j)

        self._animate()

    def _draw_cell(self, cell, i, j):
        top_left = Point(self.x1, self.y1)
        x1 = top_left.x + j * self.cell_size_x
        x2 = x1 + self.cell_size_x
        y1 = top_left.y + i * self.cell_size_y
        y2 = y1 + self.cell_size_y
        cell.draw(x1, y1, x2, y2)

    def _animate(self):
        self._wnd.redraw()
        time.sleep(1)
