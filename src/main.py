from window import Window
from maze import Maze

def main():
    # Create a window of 800x600 pixels
    win = Window(800, 600)
    
    # Create a maze with:
    # Starting at (50,50)
    # 10 rows and 10 columns
    # Cells of size 40x40 pixels
    maze = Maze(50, 50, 10, 10, 40, 40, win)
    
    win.wait_for_close()

main()