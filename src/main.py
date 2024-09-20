from src.cell import Cell
from src.geometry import Point
from src.window import Window


def main():
    wnd = Window(500, 500)
    top_left = Point(100, 100)
    bottom_right = Point(300, 300)
    wnd.draw_cell(Cell(), top_left, bottom_right, "red")
    wnd.wait_for_close()


if __name__ == "__main__":
    main()
