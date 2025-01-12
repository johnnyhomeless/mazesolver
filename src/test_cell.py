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

    def test_get_center(self):
        cell = Cell(0, 0, 10, 10, self.window)
        center = cell.get_center()
        self.assertEqual(center.x, 5)
        self.assertEqual(center.y, 5)

    def test_get_center_different_size(self):
        cell = Cell(0, 0, 20, 40, self.window)
        center = cell.get_center()
        self.assertEqual(center.x, 10)
        self.assertEqual(center.y, 20)

    def test_draw_move(self):
        cell1 = Cell(0, 0, 10, 10, self.window)
        cell2 = Cell(20, 0, 30, 10, self.window)
        
        try:
            cell1.draw_move(cell2)
            cell1.draw_move(cell2, True) 
            test_passed = True
        except Exception as e:
            test_passed = False
        self.assertTrue(test_passed)

if __name__ == '__main__':
    unittest.main()