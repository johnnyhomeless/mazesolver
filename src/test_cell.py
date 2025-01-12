import unittest
from cell import Cell
from window import Window

class TestCell(unittest.TestCase):
    def setUp(self):
        self.window = Window(800, 600)
        self.cell = Cell(100, 100, 200, 200, self.window)

    def tearDown(self):
        self.window.close()

    def test_cell_creation(self):
        self.assertEqual(self.cell.x1, 100)
        self.assertEqual(self.cell.y1, 100)
        self.assertEqual(self.cell.x2, 200)
        self.assertEqual(self.cell.y2, 200)

    def test_default_walls(self):
        self.assertTrue(self.cell.has_left_wall)
        self.assertTrue(self.cell.has_right_wall)
        self.assertTrue(self.cell.has_top_wall)
        self.assertTrue(self.cell.has_bottom_wall)

    def test_wall_removal(self):
        self.cell.has_left_wall = False
        self.assertFalse(self.cell.has_left_wall)

if __name__ == '__main__':
    unittest.main()