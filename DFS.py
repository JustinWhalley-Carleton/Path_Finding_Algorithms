from node import *
import pygame
from queue import LifoQueue
import sys

sys.setrecursionlimit(2500)
# show path on window and count the path length
def reconstruct_path(stack,grid,start,draw):
    path_length = 0
    while not stack.empty():
        node = stack.get()
        node.make_path()
        path_length+=1
        if draw != None: # dont draw when testing
            draw()
    start.make_start()
    if draw != None:  # dont draw when testing
        draw()
    return path_length

def DFS(draw,grid,start,end):
    stack = LifoQueue(25*25)
    stack.put(start)
    run = True
    while run:
        found_node = False
        current = stack.get()
        for neighbor in current.neighbors:
            if neighbor == end and run:
                stack.put(current)
                run = False
            if not neighbor.is_closed() and run:
                neighbor.make_closed()
                stack.put(current)
                stack.put(neighbor)
                found_node = True
                if draw != None: #dont draw when testing
                    draw()
                break
        if stack.empty():
            return

    return reconstruct_path(stack,grid,start,draw)