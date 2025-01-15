import unittest
from maze import Maze
from window import Window

class TestMaze(unittest.TestCase):
    def setUp(self):
        self.window = Window(800, 600)
    
    def tearDown(self):
        self.window.close()
    
    def test_maze_creation(self):
        maze = Maze(50, 50, 10, 10, 40, 40, self.window)
        self.assertEqual(maze.x1, 50)
        self.assertEqual(maze.y1, 50)
        self.assertEqual(maze.num_rows, 10)
        self.assertEqual(maze.num_cols, 10)
        self.assertEqual(maze.cell_size_x, 40)
        self.assertEqual(maze.cell_size_y, 40)

    def test_maze_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            Maze(-50, 50, 10, 10, 40, 40, self.window)
        
        with self.assertRaises(ValueError):
            Maze(50, -50, 10, 10, 40, 40, self.window)
            
        with self.assertRaises(ValueError):
            Maze(50, 50, -10, 10, 40, 40, self.window) 
            
        with self.assertRaises(ValueError):
            Maze(50, 50, 10, -10, 40, 40, self.window) 

    def test_reset_cells_visited(self):
        maze = Maze(50, 50, 3, 3, 40, 40, self.window)
        
        # Verify some cells are visited after maze creation
        visited_found = False
        for i in range(maze.num_rows):
            for j in range(maze.num_cols):
                if maze._cells[i][j].visited:
                    visited_found = True
                    break
        self.assertTrue(visited_found)
        
        # Reset cells
        maze._reset_cells_visited()
        
        # Verify all cells are not visited
        for i in range(maze.num_rows):
            for j in range(maze.num_cols):
                self.assertFalse(maze._cells[i][j].visited)

if __name__ == '__main__':
    unittest.main()