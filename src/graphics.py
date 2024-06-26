from tkinter import BOTH, Canvas, Tk


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.resizable(False, False)
        self.__root.title("MazeSolver v.0")
        self.__canvas = Canvas(self.__root, width=width, height=height, bg="black")
        self.__canvas.pack(fill=BOTH, expand=1)
        # self.__canvas.pack(fill="none", expand=0)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        # self.__root.mainloop()

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def draw_line(self, line, fill_color="white"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False
        # self.__root.destroy()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2

    def draw(self, canvas, fill_color="white"):
        canvas.create_line(
            self.__point1.x,
            self.__point1.y,
            self.__point2.x,
            self.__point2.y,
            fill=fill_color,
            width=2,
        )
        canvas.pack(fill=BOTH, expand=1)
