from src.geometry import Line
from src.geometry import Point


class Cell:
    def __init__(
        self,
        wnd,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True,
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = -1
        self._y1 = -1
        self._x2 = -1
        self._y2 = -1
        self._wnd = wnd

    def draw(self, x1, y1, x2, y2, fill_color="black"):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._wnd.draw_line(line, fill_color)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._wnd.draw_line(line, fill_color)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._wnd.draw_line(line, fill_color)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._wnd.draw_line(line, fill_color)

    def get_center(self):
        if (self._x1 or self._y1 or self._x2 or self._y2) is None:
            raise Exception("values are wrong")
        center = Point(
            self._x1 + (self._x2 - self._x1) / 2, self._y1 + (self._y2 - self._y1) / 2
        )
        return center

    def draw_move(self, to_cell, undo=False):
        this_center = self.get_center()
        other_center = to_cell.get_center()
        line = Line(this_center, other_center)
        if undo:
            self._wnd.draw_line(line, "red")
            return
        self._wnd.draw_line(line, "gray")
