from window import Window
from maze import Maze

def main():
   win = Window(800, 600)
   maze = Maze(50, 50, 10, 10, 40, 40, win, seed=42)
   
   # Test reset_cells_visited
   maze._reset_cells_visited()
   
   # Print some cells to verify
   print(f"Cell [0][0] visited: {maze._cells[0][0].visited}")
   print(f"Cell [5][5] visited: {maze._cells[5][5].visited}")
   
   win.wait_for_close()

main()