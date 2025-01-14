from cell import Cell
from window import Window
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        if x1 < 0 or y1 < 0:
         raise ValueError("x1 and y1 must be positive")
        if num_rows <= 0 or num_cols <= 0:
            raise ValueError("Number of rows and columns must be positive")
        if cell_size_x <= 0 or cell_size_y <= 0:
            raise ValueError("Cell sizes must be positive")
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                x1 = self.x1 + (j * self.cell_size_x)
                y1 = self.y1 + (i * self.cell_size_y)
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                cell = Cell(x1, y1, x2, y2, self._win)
                row.append(cell)
            self._cells.append(row)
        for i in range(self.num_rows):
                for j in range(self.num_cols):
                    self._draw_cell(i, j)
        self._break_entrance_and_exit()

    def _draw_cell(self, i, j):
        cell = self._cells[i][j] 
        cell.draw()
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[self.num_rows - 1][self.num_cols - 1]
        entrance.has_top_wall = False
        exit.has_bottom_wall = False  
        self._draw_cell(0, 0)  
        self._draw_cell(self.num_rows - 1, self.num_cols - 1)

