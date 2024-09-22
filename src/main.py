from src.cell import Cell
from src.window import Window


def main():
    wnd = Window(1000, 1000)
    length = 200

    left = Cell(wnd, has_right_wall=False)
    left.draw(100, 100, 100 + length, 100 + length, "black")

    mid = Cell(wnd, has_left_wall=False, has_right_wall=False)
    mid.draw(300, 100, 300 + length, 100 + length, "black")

    right = Cell(wnd, has_left_wall=False)
    right.draw(500, 100, 500 + length, 100 + length, "black")

    left.draw_move(mid, undo=True)
    mid.draw_move(right, undo=True)
    wnd.wait_for_close()


if __name__ == "__main__":
    main()
