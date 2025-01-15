from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 10, 10, 40, 40, win, seed=42)
    win.wait_for_close()

main()