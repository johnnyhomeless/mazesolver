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

if __name__ == '__main__':
    unittest.main()