from src.cell import Cell
from src.geometry import Point
import time
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        wnd=None,
        seed=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._wnd = wnd
        self._cells = []
        self._create_cells()
        self._seed = seed
        if self._seed is not None:
            random.seed(self._seed)
        self._reset_cells_visited()

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

        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._animate()

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        self._draw_cell(entrance, 0, 0)

        exit = self._cells[-1][-1]
        exit.has_bottom_wall = False
        self._draw_cell(exit, len(self._cells) - 1, len(self._cells[-1]) - 1)

    def _draw_cell(self, cell, i, j):
        top_left = Point(self.x1, self.y1)
        x1 = top_left.x + j * self.cell_size_x
        x2 = x1 + self.cell_size_x
        y1 = top_left.y + i * self.cell_size_y
        y2 = y1 + self.cell_size_y
        cell.draw(x1, y1, x2, y2)

    def _animate(self):
        if self._wnd is None:
            return
        self._wnd.redraw()
        time.sleep(1)

    def _break_walls_r(self, i, j):
        curr = self._cells[i][j]
        curr.visited = True

        while True:
            to_visit = []

            possible_directions = 0
            if j > 0:
                left = self._cells[i][j - 1]
                if not left.visited:
                    to_visit.append((i, j - 1, "left"))
                    possible_directions += 1

            if j < self.num_cols - 1:
                right = self._cells[i][j + 1]
                if not right.visited:
                    to_visit.append((i, j + 1, "right"))
                    possible_directions += 1

            if i > 0:
                top = self._cells[i - 1][j]
                if not top.visited:
                    to_visit.append((i - 1, j, "top"))
                    possible_directions += 1

            if i < self.num_rows - 1:
                bottom = self._cells[i + 1][j]
                if not bottom.visited:
                    to_visit.append((i + 1, j, "bottom"))
                    possible_directions += 1

            if possible_directions == 0:
                self._draw_cell(curr, i, j)
                return

            dir_index = random.randint(0, len(to_visit) - 1)
            dir = to_visit[dir_index]

            chosen_cell = self._cells[dir[0]][dir[1]]
            match dir[2]:
                case "left":
                    chosen_cell.has_right_wall = False
                    curr.has_left_wall = False
                    self._break_walls_r(dir[0], dir[1])

                case "right":
                    chosen_cell.has_left_wall = False
                    curr.has_right_wall = False
                    self._break_walls_r(dir[0], dir[1])

                case "top":
                    chosen_cell.has_bottom_wall = False
                    curr.has_top_wall = False
                    self._break_walls_r(dir[0], dir[1])

                case "bottom":
                    chosen_cell.has_top_wall = False
                    curr.has_bottom_wall = False
                    self._break_walls_r(dir[0], dir[1])

    def _reset_cells_visited(self):
        for i in self._cells:
            for j in i:
                j.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        end = self._cells[self.num_rows - 1][self.num_cols - 1]
        self._animate()
        curr = self._cells[i][j]
        curr.visited = True

        if curr is end:
            return True

        if j > 0:
            left = self._cells[i][j - 1]
            if not left.visited and not left.has_right_wall:
                curr.draw_move(left)
                if self._solve_r(i, j - 1):
                    return True
                curr.draw_move(left, undo=True)

        if j < self.num_cols - 1:
            right = self._cells[i][j + 1]
            if not right.visited and not right.has_left_wall:
                curr.draw_move(right)
                if self._solve_r(i, j + 1):
                    return True
                curr.draw_move(right, undo=True)

        if i > 0:
            top = self._cells[i - 1][j]
            if not top.visited and not top.has_bottom_wall:
                curr.draw_move(top)
                if self._solve_r(i - 1, j):
                    return True
                curr.draw_move(top, undo=True)

        if i < self.num_rows - 1:
            bottom = self._cells[i + 1][j]
            if not bottom.visited and not bottom.has_top_wall:
                curr.draw_move(bottom)
                if self._solve_r(i + 1, j):
                    return True
                curr.draw_move(bottom, undo=True)

        return False
