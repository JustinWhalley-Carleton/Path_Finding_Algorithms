from node import *
import pygame
from queue import PriorityQueue


#display path on the window and count path length
def reconstruct_path(came_from,current,draw, start):    
    path = []   
    path_length = 0    
    while current in reversed(came_from):
        current = came_from[current]
        path.append(current)
    for current in reversed(path):
        if current == start:
            continue
        path_length+= 1
        current.make_path()
        if draw != None: # dontdraw for testing
            draw()
    return path_length 
# main algorithm function
def astar(grid,start,end,draw):
    # initialize variables
    count = 0
    open_set = PriorityQueue()
    open_set.put((0,count,start))
    came_from = {}
    g_score = {node:float("inf") for row in grid for node in row}    
    g_score[start] = 0
    f_score = {node:float("inf") for row in grid for node in row}      
    f_score[start] = h(start.get_pos(),end.get_pos())
    open_set_hash = {start}
    path_length = 0
    #main loop to find path
    while not open_set.empty():
        current = open_set.get()[2]
        open_set_hash.remove(current)
        # check if found the end
        if current == end:
            start.make_start()
            end.make_end()
            return reconstruct_path(came_from,current,draw,start)
        # check neighbors to see which is the best path
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1 
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor]=temp_g_score
                f_score[neighbor]=temp_g_score+h(neighbor.get_pos(),end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor],count,neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        #draw the checked nodes on the window if not testing
        if draw != None:
            draw()
        #close the node if neighbors were checked
        if current != start:
            current.make_closed()
    return None
#calculate manhatten distance between node1 and node2
def h(node1,node2):
    x1,y1 = node1
    x2,y2 = node2
    return abs(x1-x2)+abs(y1-y2)