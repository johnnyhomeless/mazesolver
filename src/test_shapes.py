import unittest
from shapes import Point, Line

class TestPoint(unittest.TestCase):
    def test_point_coordinates(self):
        point = Point(3, 5)
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 5)

class TestLine(unittest.TestCase):
    def test_line_points(self):
        point1 = Point(0, 0)
        point2 = Point(10, 10)
        line = Line(point1, point2)
        self.assertEqual(line.point1, point1)
        self.assertEqual(line.point2, point2)

    def test_line_draw(self):
        class MockCanvas:
            def __init__(self):
                self.called_with = None

            def create_line(self, x1, y1, x2, y2, fill, width):
                self.called_with = (x1, y1, x2, y2, fill, width)

        point1 = Point(10, 20)
        point2 = Point(30, 40)
        line = Line(point1, point2)
        mock_canvas = MockCanvas()

        line.draw(mock_canvas, "blue")
        self.assertEqual(mock_canvas.called_with, (10, 20, 30, 40, "blue", 2))

    def test_point_zero_coordinates(self):
        point = Point(0, 0)
        self.assertEqual(point.x, 0)
        self.assertEqual(point.y, 0)

    def test_point_negative_coordinates(self):
        point = Point(-5, -10)
        self.assertEqual(point.x, -5)
        self.assertEqual(point.y, -10)

    def test_point_large_coordinates(self):
        point = Point(999999, 888888)
        self.assertEqual(point.x, 999999)
        self.assertEqual(point.y, 888888)

    def test_invalid_points(self):
        with self.assertRaises(TypeError):
            Line("not a point", Point(1, 1))
    
if __name__ == '__main__':
    unittest.main()