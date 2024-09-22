from src.maze import Maze
from src.window import Window


def main():
    width = 1000
    height = 1000
    wnd = Window(width, height)
    x1 = 0
    y1 = 0
    num_rows = 10
    num_cols = 10
    cell_size_x = width / num_cols
    cell_size_y = height / num_rows
    maze = Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, wnd)
    wnd.wait_for_close()


if __name__ == "__main__":
    main()
