from shapes import Line, Point

class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self):
        if self.has_left_wall:
            point1 = Point(self.x1, self.y1) 
            point2 = Point(self.x1, self.y2) 
            line = Line(point1, point2)
            self._win.draw_line(line, "black")

        if self.has_top_wall:
            point1 = Point(self.x1, self.y1)
            point2 = Point(self.x2, self.y1)
            line = Line(point1, point2)
            self._win.draw_line(line, "black")

        if self.has_right_wall:
            point1 = Point(self.x2, self.y1) 
            point2 = Point(self.x2, self.y2) 
            line = Line(point1, point2)
            self._win.draw_line(line, "black")

        if self.has_bottom_wall:
            point1 = Point(self.x1, self.y2) 
            point2 = Point(self.x2, self.y2) 
            line = Line(point1, point2)
            self._win.draw_line(line, "black")
