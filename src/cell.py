from src.geometry import Line
from src.geometry import Point


class Cell:
    def __init__(
        self,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True,
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self, canvas, top_left, bottom_right, fill_color="black"):
        if self.has_left_wall:
            line = Line(top_left, Point(top_left.x, bottom_right.y))
            line.draw(canvas, fill_color)
        if self.has_right_wall:
            line = Line(Point(bottom_right.x, top_left.y), bottom_right)
            line.draw(canvas, fill_color)
        if self.has_top_wall:
            line = Line(top_left, Point(bottom_right.x, top_left.y))
            line.draw(canvas, fill_color)
        if self.has_bottom_wall:
            line = Line(Point(top_left.x, bottom_right.y), bottom_right)
            line.draw(canvas, fill_color)
