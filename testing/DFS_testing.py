import unittest
import sys
import os
sys.path.insert(1, os.path.dirname(os.path.dirname(__file__)))
from DFS import *
from test_grid import *

class DFS_test(unittest.TestCase):
     
    def test_path_found_no_wall(self):
        start = grid[0][0]
        end = grid[16][20]
        for row in grid:
            for node in row:
                node.update_neighbors(grid)
        self.assertTrue(DFS(None, grid, start, end) != 0)

    def test_path_not_found(self):
        start = grid[0][0]
        end = grid[5][5]
        grid[3][0].make_wall()
        grid[3][1].make_wall()
        grid[3][2].make_wall()
        grid[3][3].make_wall()
        grid[2][3].make_wall()
        grid[1][3].make_wall()
        grid[0][3].make_wall()
        for row in grid:
            for node in row:
                node.update_neighbors(grid)
        self.assertFalse(DFS(None, grid, start, end))

    def test_path_length_no_wall(self):
        start = grid[0][0]
        end = grid[5][5]
        for row in grid:
            for node in row:
                node.update_neighbors(grid)
        self.assertEqual(DFS(None, grid, start, end), 500)

    def test_path_length_with_wall_1(self):
        start = grid[0][0]
        end = grid[5][5]
        grid[3][1].make_wall()
        grid[3][2].make_wall()
        grid[3][3].make_wall()
        grid[2][3].make_wall()
        grid[1][3].make_wall()
        for row in grid:
            for node in row:
                node.update_neighbors(grid)
        self.assertEqual(DFS(None, grid, start, end), 500)
    
    def test_path_length_with_wall_2(self):
        start = grid[0][0]
        end = grid[4][4]
        grid[3][0].make_wall()
        grid[3][1].make_wall()
        grid[3][2].make_wall()
        grid[3][3].make_wall()
        grid[2][3].make_wall()
        grid[1][3].make_wall()
        for row in grid:
            for node in row:
                node.update_neighbors(grid)
        self.assertEqual(DFS(None, grid, start, end), 14)

    def test_path_reconstructed(self):
        start = grid[0][0]
        end = grid[4][4]
        grid[3][0].make_wall()
        grid[3][1].make_wall()
        grid[3][2].make_wall()
        grid[3][3].make_wall()
        grid[2][3].make_wall()
        grid[1][3].make_wall()
        for row in grid:
            for node in row:
                node.update_neighbors(grid)
        DFS(None, grid, start, end)
        flag = True
        flag = flag and grid[1][0].color == PURPLE
        flag = flag and grid[2][0].color == PURPLE
        flag = flag and grid[0][1].color == PURPLE
        flag = flag and grid[1][1].color == PURPLE
        flag = flag and grid[2][1].color == PURPLE
        flag = flag and grid[0][2].color == PURPLE
        flag = flag and grid[1][2].color == PURPLE
        flag = flag and grid[2][2].color == PURPLE
        flag = flag and grid[0][3].color == PURPLE
        flag = flag and grid[0][4].color == PURPLE
        flag = flag and grid[1][4].color == PURPLE
        flag = flag and grid[2][4].color == PURPLE
        flag = flag and grid[3][4].color == PURPLE
        self.assertTrue(flag)

    def tearDown(self):
        for row in grid:
            for node in row:
                node.reset()
'''
if __name__ == "__main__":
    unittest.main()
'''