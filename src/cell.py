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
        self.visited = False
        
    def draw(self):
        point1 = Point(self.x1, self.y1) 
        point2 = Point(self.x1, self.y2) 
        line = Line(point1, point2)
        color = "black" if self.has_left_wall else "#F0F0F0"
        self._win.draw_line(line, color)

        point1 = Point(self.x1, self.y1)
        point2 = Point(self.x2, self.y1)
        line = Line(point1, point2)
        color = "black" if self.has_top_wall else "#F0F0F0"
        self._win.draw_line(line, color)

        point1 = Point(self.x2, self.y1) 
        point2 = Point(self.x2, self.y2) 
        line = Line(point1, point2)
        color = "black" if self.has_right_wall else "#F0F0F0"
        self._win.draw_line(line, color)

        point1 = Point(self.x1, self.y2) 
        point2 = Point(self.x2, self.y2) 
        line = Line(point1, point2)
        color = "black" if self.has_bottom_wall else "#F0F0F0"
        self._win.draw_line(line, color)

    def get_center(self):
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        return Point(center_x, center_y)
    
    def draw_move(self, to_cell, undo=False):
        start = self.get_center()
        end = to_cell.get_center()
        
        line = Line(start, end)
        
        color = "gray" if undo else "red"
        
        self._win.draw_line(line, color)