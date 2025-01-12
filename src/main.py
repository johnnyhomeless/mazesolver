from window import Window
from cell import Cell

def main():
    win = Window(800, 600)

    cell1 = Cell(50, 50, 100, 100, win)
    cell2 = Cell(150, 50, 200, 100, win)
    cell3 = Cell(250, 50, 300, 100, win)  

    cell1.draw()
    cell2.draw()
    cell3.draw()

    win.wait_for_close()

if __name__ == "__main__":
    main()