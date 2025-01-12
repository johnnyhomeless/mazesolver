from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Width and height must be numbers")
      
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive") 
           
        if width > 3840 or height > 2160:  
            raise ValueError("Window dimensions too large")
        
        if width < 100 or height < 100:   
            raise ValueError("Window dimensions too small")

        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{int(width)}x{int(height)}")
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def close(self):
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True

        while self.__running:
            self.redraw()
    
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)




