import random
import time

from cell import Cell


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__seed = seed
        if self.__seed is not None:
            random.seed(self.__seed)
        else:
            random.seed()
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited()
        self._solve()

    def _create_cells(self):
        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                col_cells.append(
                    Cell(
                        self.__x1 + (self.__cell_size_x * i),
                        self.__y1 + (self.__cell_size_y * j),
                        self.__x1 + (self.__cell_size_x * (i + 1)),
                        self.__y1 + (self.__cell_size_y * (j + 1)),
                        self.__win,
                    )
                )
            self._cells.append(col_cells)

        # used for test_cases where _win will be None
        if self.__win is not None:
            self._draw_cells()

    def _draw_cells(self):
        for list in self._cells:
            for cell in list:
                cell.draw("blue")
            self.__animate()

    def _draw_cell(self, i, j):
        self._cells[i][j].draw("blue")
        self.__animate()

    def __animate(self):
        if self.__win is not None:
            self.__win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        self._cells[-1][-1].has_bottom_wall = False
        self._cells[-1][-1].draw()
        # self.__animate()

    def _break_walls_r(self, i, j):
        while True:
            can_visit = []
            self._cells[i][j].visited = True
            can_visit.extend(self.can_visit_rows(i, j))
            can_visit.extend(self.can_visit_columns(i, j))

            if can_visit:
                i, j = self.pick_next_cell(i, j, can_visit)
                self._break_walls_r(i, j)
            else:
                return

    def can_visit_rows(self, i, j):
        can_visit = []

        if j + 1 < self.__num_rows and not self._cells[i][j+1].visited:
            can_visit.append((i, j+1, "down"))
        if j - 1 >= 0 and not self._cells[i][j-1].visited:
            can_visit.append((i, j-1, "up"))

        return can_visit

    def can_visit_columns(self, i, j):
        can_visit = []

        if i + 1 < self.__num_cols and not self._cells[i+1][j].visited:
            can_visit.append((i + 1, j, "right"))
        if i - 1 >= 0 and not self._cells[i-1][j].visited:
            can_visit.append((i - 1, j, "left"))

        return can_visit

    def pick_next_cell(self, cur_col, cur_row, can_visit):

        pick = random.randrange(len(can_visit))
        next_cell_tuple = can_visit.pop(pick)
        next_cell_column = next_cell_tuple[0]
        next_cell_row = next_cell_tuple[1]
        next_cell_direction = next_cell_tuple[2]
        cell = self._cells[cur_col][cur_row]
        next_cell = self._cells[next_cell_column][next_cell_row]

        match next_cell_direction:
            case "up":
                cell.has_top_wall = False
                next_cell.has_bottom_wall = False
                self._draw_cell(cur_col, cur_row)
            case "down":
                cell.has_bottom_wall = False
                next_cell.has_top_wall = False
                self._draw_cell(cur_col, cur_row)
            case "left":
                cell.has_left_wall = False
                next_cell.has_right_wall = False
                self._draw_cell(cur_col, cur_row)
            case "right":
                cell.has_right_wall = False
                next_cell.has_left_wall = False
                self._draw_cell(cur_col, cur_row)

        return next_cell_column, next_cell_row

    def _reset_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._cells[i][j].visited = False

    def _solve(self):
        if self.__solve_r(0, 0):
            return True
        return False

    def __solve_r(self, cur_col, cur_row):
        while True:
            if cur_col == self.__num_cols - 1 and cur_row == self.__num_rows - 1:
                return True

            self._cells[cur_col][cur_row].visited = True
            directions = self.__get_possible_directions(cur_col, cur_row)
            print("Directions", directions)
            if not directions:
                return False

            pick = random.randrange(len(directions))
            next_col, next_row = directions.pop(pick)

            self._move(cur_col, cur_row, next_col, next_row)

            if not self.__solve_r(next_col, next_row):
                self._undo_move(cur_col, cur_row, next_col, next_row)
            else:
                self._cells[next_col][next_row].visited = True
                return True

    def __get_possible_directions(self, cur_col, cur_row):
        directions = []
        cell = self._cells[cur_col][cur_row]

        if not cell.has_top_wall and not (cur_col == 0 and cur_row == 0):
            if self._cells[cur_col][cur_row - 1].visited is False:
                directions.append((cur_col, cur_row - 1))

        if not cell.has_bottom_wall:
            if self._cells[cur_col][cur_row + 1].visited is False:
                directions.append((cur_col, cur_row + 1))

        if not cell.has_right_wall:
            if self._cells[cur_col + 1][cur_row].visited is False:
                directions.append((cur_col + 1, cur_row))

        if not cell.has_left_wall and not (cur_col == self.__num_cols - 1 and cur_row == self.__num_rows - 1):
            if self._cells[cur_col - 1][cur_row].visited is False:
                directions.append((cur_col - 1, cur_row))

        return directions

    def _move(self, cur_col, cur_row, next_col, next_row):
        print("draw_move", cur_col, cur_row, next_col, next_row)
        self._cells[cur_col][cur_row].draw_move(
            self._cells[next_col][next_row])
        self.__animate()

    def _undo_move(self, cur_col, cur_row, next_col, next_row):
        print("undo_move", cur_col, cur_row, next_col, next_row)
        self._cells[next_col][next_row].draw_move(
            self._cells[cur_col][cur_row], True)
        self.__animate()
