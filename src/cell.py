from graphics import Line, Point


class Cell:
    def __init__(
        self,
        x1,
        y1,
        x2,
        y2,
        win,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = win
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.has_right_wall = has_right_wall
        self.has_left_wall = has_left_wall
        self.top_left = Point(self.__x1, self.__y1)
        self.top_right = Point(self.__x2, self.__y1)
        self.bottom_left = Point(self.__x1, self.__y2)
        self.bottom_right = Point(self.__x2, self.__y2)
        self.visited = False

    def draw(self, fill_color="white"):

        if self.has_top_wall:
            self.draw_top_wall(fill_color)
        else:
            self.draw_top_wall("black")

        if self.has_bottom_wall:
            self.draw_bottom_wall(fill_color)
        else:
            self.draw_bottom_wall("black")

        if self.has_left_wall:
            self.draw_left_wall(fill_color)
        else:
            self.draw_left_wall("black")

        if self.has_right_wall:
            self.draw_right_wall(fill_color)
        else:
            self.draw_right_wall("black")

    def draw_top_wall(self, fill_color="white"):
        line = Line(self.top_left, self.top_right)
        self.__win.draw_line(line, fill_color)

    def draw_bottom_wall(self, fill_color="white"):
        line = Line(self.bottom_left, self.bottom_right)
        self.__win.draw_line(line, fill_color)

    def draw_left_wall(self, fill_color="white"):
        line = Line(self.top_left, self.bottom_left)
        self.__win.draw_line(line, fill_color)

    def draw_right_wall(self, fill_color="white"):
        line = Line(self.top_right, self.bottom_right)
        self.__win.draw_line(line, fill_color)

    def draw_move(self, to_cell, undo=False):
        print("Cells to connect", self, to_cell)
        c1_x = (self.__x1 + self.__x2) / 2
        c1_y = (self.__y1 + self.__y2) / 2
        c2_x = (to_cell.__x1 + to_cell.__x2) / 2
        c2_y = (to_cell.__y1 + to_cell.__y2) / 2

        if undo:
            fill_color = "red"
        else:
            fill_color = "white"

        self.__win.draw_line(Line(Point(c1_x, c1_y), Point(c2_x, c2_y)), fill_color)

        # # moving up
        # if self.__y1 > to_cell.__y1:
        #     self.__win.draw_line(
        #         Line(Point(c1_x, c1_y), Point(c1_x, self.__y1)), fill_color
        #     )
        #     to_cell.__win.draw_line(
        #         Line(Point(c2_x, c2_y), Point(c2_x, to_cell.__y2)), fill_color
        #     )
        #
        # # moving down
        # elif self.__y1 < to_cell.__y1:
        #     self.__win.draw_line(
        #         Line(Point(c1_x, c1_y), Point(c1_x, self.__y2)), fill_color
        #     )
        #     to_cell.__win.draw_line(
        #         Line(Point(c2_x, c2_y), Point(c2_x, to_cell.__y1)), fill_color
        #     )
        #
        # # moving right
        # elif self.__x1 < to_cell.__x1:
        #     self.__win.draw_line(
        #         Line(Point(c1_x, c1_y), Point(self.__x2, c1_y)), fill_color
        #     )
        #     to_cell.__win.draw_line(
        #         Line(Point(c2_x, c2_y), Point(to_cell.__x1, c2_y)), fill_color
        #     )
        #
        # # moving left
        # elif self.__x1 > to_cell.__x1:
        #     self.__win.draw_line(
        #         Line(Point(c1_x, c1_y), Point(self.__x1, c1_y)), fill_color
        #     )
        #     to_cell.__win.draw_line(
        #         Line(Point(c2_x, c2_y), Point(to_cell.__x2, c2_y)), fill_color
        #     )

    def __repr__(self):
        return f"{self.__x1} {self.__y1} {self.__x2} {self.__y2} {self.has_top_wall} {self.has_bottom_wall} {self.has_left_wall} {self.has_right_wall}"
