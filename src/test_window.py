import unittest
from window import Window
from tkinter import Canvas

class TestWindow(unittest.TestCase):
    def setUp(self):
        self.window = Window(800, 600)
    
    def tearDown(self):
        self.window.close()

    def test_window_initializes(self):
        self.assertFalse(self.window._Window__running)
    
    def test_window_close(self):
        self.window._Window__running = True
        self.window.close()
        self.assertFalse(self.window._Window__running)

    def test_window_dimensions(self):
        expected_width = 800
        expected_height = 600
        self.window.redraw()
        actual_width = self.window._Window__root.winfo_width()
        actual_height = self.window._Window__root.winfo_height()
        self.assertEqual(expected_width, actual_width)
        self.assertEqual(expected_height, actual_height)

    def test_title_setting(self):
        expected_title = "Maze Solver"
        actual_title = self.window._Window__root.title()
        self.assertEqual(expected_title, actual_title)
    
    def test_canvas_exists(self):
        self.assertIsNotNone(self.window._Window__canvas)
        self.assertIsInstance(self.window._Window__canvas, Canvas)

    def test_redraw_method(self):
        try:
            self.window.redraw()
            test_passed = True
        except Exception as e:
            test_passed = False
        self.assertTrue(test_passed)

    def test_wait_for_close_initial_state(self):
        self.assertFalse(self.window._Window__running)
        self.window._Window__running = True
        self.assertTrue(self.window._Window__running)
    
    def test_window_invalid_type(self):
        with self.assertRaises(TypeError):
            Window("not a number", 600)
        with self.assertRaises(TypeError):
            Window(800, "not a number")

    def test_window_negative_size(self):
        with self.assertRaises(ValueError):
            Window(-800, 600)
        with self.assertRaises(ValueError):
            Window(800, -600)

    def test_window_zero_size(self):
        with self.assertRaises(ValueError):
            Window(0, 600)
        with self.assertRaises(ValueError):
            Window(800, 0)

    def test_window_too_small(self):
        with self.assertRaises(ValueError):
            Window(50, 600)
        with self.assertRaises(ValueError):
            Window(800, 50)

    def test_window_too_large(self):
        with self.assertRaises(ValueError):
            Window(4000, 600)
        with self.assertRaises(ValueError):
            Window(800, 4000)

if __name__ == '__main__':
    unittest.main()