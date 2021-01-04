import unittest
import sys
import os
sys.path.insert(1, os.path.dirname(os.path.dirname(__file__)))
from node import *
from test_grid import *
from colors import *

class Node_test(unittest.TestCase):
    
    def test_make_closed(self):
        grid[1][1].make_closed()
        self.assertTrue(grid[1][1].is_closed())

    def test_make_open(self):
        grid[1][1].make_open()
        self.assertTrue(grid[1][1].is_open())

    def test_make_wall(self):
        grid[1][1].make_wall()
        self.assertTrue(grid[1][1].is_wall())

    def test_make_start(self):
        grid[1][1].make_start()
        self.assertTrue(grid[1][1].is_start())

    def test_make_end(self):
        grid[1][1].make_end()
        self.assertTrue(grid[1][1].is_end())

    def test_make_path(self):
        grid[1][1].make_path()
        self.assertTrue(grid[1][1].color == PURPLE) 

    def test_reset(self):
        grid[1][1].reset()
        self.assertTrue(grid[1][1].color == WHITE)

    def test_neighbors(self):
        grid[3][0].update_neighbors(grid)
        self.assertTrue(len(grid[3][0].neighbors) == 3 and grid[2][0] in grid[3][0].neighbors and grid[4][0] in grid[3][0].neighbors and grid[3][1] in grid[3][0].neighbors)

    def test_get_pos(self):
        self.assertTrue(grid[9][3].get_pos() == (9,3))

    def tearDown(self):
        for row in grid:
            for node in row:
                node.reset()
'''
if __name__=="__main__":
    unittest.main()
'''