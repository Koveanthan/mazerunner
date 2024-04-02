from cell import Cell
from graphics import Line, Point, Window
from maze import Maze

window = Window(800, 600)

# line1 = Line(Point(0, 10), Point(100, 10))
# window.draw_line(line1, "white")
# line2 = Line(Point(0, 50), Point(150, 50))
# window.draw_line(line2, "red")
#
# cell1 = Cell(10, 10, 20, 20, window, True, True, True, True)
# cell1.draw("red")
# cell2 = Cell(300, 300, 500, 500, window, has_top_wall=False, has_bottom_wall=False)
# cell2.draw()
# cell3 = Cell(700, 500, 800, 600, window, has_right_wall=False, has_left_wall=False)
# cell3.draw("red")
#
# cell2.draw_move(cell3)
#
# cell1.draw_move(cell2, True)

m = Maze(80, 60, 8, 8, 80, 60, window)

window.wait_for_close()
