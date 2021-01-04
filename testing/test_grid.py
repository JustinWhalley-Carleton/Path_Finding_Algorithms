import sys
import os
sys.path.insert(1, os.path.dirname(os.path.dirname(__file__)))
from node import *

grid = []

for i in range(25):
    grid.append([])
    for j in range(25):
        grid[i].append(Node(i,j,800,25))
