import unittest

from maze import Maze


class TestMaze(unittest.TestCase):
    def test_rows_and_colunms(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 2, 2)
        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)

    def test_zero_rows_and_colunms(self):
        num_cols = 0
        num_rows = 0
        maze = Maze(0, 0, num_rows, num_cols, 2, 2)
        self.assertEqual(len(maze._cells), 0)
        with self.assertRaises(IndexError):
            maze._cells[0]
