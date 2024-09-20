from src.geometry import Line, Point
from src.window import Window


def main():
    wnd = Window(500, 500)
    p1 = Point(250, 250)
    p2 = Point(250, 150)
    wnd.draw_line(Line(p1, p2), "red")
    wnd.wait_for_close()


if __name__ == "__main__":
    main()
