import queue
from node import *
import pygame

# show path on window and count the path length
def reconstruct_path(path,grid,start,end,draw):
    x,y = start.get_pos()
    path_length = 0
    for move in path:
        if(move == "L"):
            x-=1
        if(move == "R"):
            x+=1
        if(move == "U"):
            y-=1
        if(move == "D"):
            y+=1
        path_length+=1
        grid[x][y].make_path()
        draw()
    end.make_end()
    start.make_start()
    draw()
    return path_length
# check if node reached a dead end
def hasMove(path,start,grid):
    x,y = start.get_pos()
    flag1 = True
    flag2 = True
    flag3 = True
    flag4 = True
    for move in path:
        if(move == "L"):
            x-=1
        if(move == "R"):
            x+=1
        if(move == "U"):
            y-=1
        if(move == "D"):
            y+=1
    if x+1 <24:
        if(grid[x+1][y].is_closed() or grid[x+1][y].is_start() or grid[x+1][y].is_end()):
            flag1 = False
    else:
        flag1 = False
    if x-1 >0:
        if(grid[x-1][y].is_closed() or grid[x-1][y].is_start() or grid[x-1][y].is_end()):
            flag2 = False
    else:
        flag2 = False
    if y+1 <24:
        if(grid[x][y+1].is_closed() or grid[x][y+1].is_start() or grid[x][y+1].is_end()):
            flag3 = False
    else:
        flag3 = False
    if y-1 >0:
        if(grid[x][y-1].is_closed() or grid[x][y-1].is_start() or grid[x][y-1].is_end()):
            flag4 = False
    else:
        flag4 = False
    return (flag1 or flag2 or flag3 or flag4)
# check if the move is valid
def moveValid(path, grid, start):
    x,y = start.get_pos()
    for move in path:
        if(move == "L"):
            x-=1
        if(move == "R"):
            x+=1
        if(move == "U"):
            y-=1
        if(move == "D"):
            y+=1
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return False
    elif(grid[x][y].is_wall() or grid[x][y].is_closed() or grid[x][y].is_start()):
        return False
    grid[x][y].make_closed()
    return True
# check if the node has a move
def hasMove(path,start,grid):
    x,y = start.get_pos()
    flag1 = True
    flag2 = True
    flag3 = True
    flag4 = True
    for move in path:
        if(move == "L"):
            x-=1
        if(move == "R"):
            x+=1
        if(move == "U"):
            y-=1
        if(move == "D"):
            y+=1
    if x+1 <24:
        if(grid[x+1][y].is_closed() or grid[x+1][y].is_start() or grid[x+1][y].is_end()):
            flag1 = False
    else:
        flag1 = False
    if x-1 >0:
        if(grid[x-1][y].is_closed() or grid[x-1][y].is_start() or grid[x-1][y].is_end()):
            flag2 = False
    else:
        flag2 = False
    if y+1 <24:
        if(grid[x][y+1].is_closed() or grid[x][y+1].is_start() or grid[x][y+1].is_end()):
            flag3 = False
    else:
        flag3 = False
    if y-1 >0:
        if(grid[x][y-1].is_closed() or grid[x][y-1].is_start() or grid[x][y-1].is_end()):
            flag4 = False
    else:
        flag4 = False
    return (flag1 or flag2 or flag3 or flag4)
# check if the path leads to the end node
def isEnd(path,start,end):
    x,y = start.get_pos()
    endX, endY = end.get_pos()
    for move in path:
        if(move == "L"):
            x-=1
        if(move == "R"):
            x+=1
        if(move == "U"):
            y-=1
        if(move == "D"):
            y+=1
    if((x,y) == (endX,endY)):
        return True
    return False
# main algorithm function
def BFS(draw,grid,start,end):
    paths = queue.Queue()
    paths.put("")
    add = ""
    # main loop to run the algorithm
    while not isEnd(add,start,end):
        add = paths.get()
        path_arr = []
        #check all directions
        for direction in ["L","R","U","D"]:
            put = add + direction
            if moveValid(put,grid,start):
                paths.put(put)
                draw()
        dead_end = False
        # check if if all nodes lead to a deadend and stop execution if all nodes lead to a dead end
        for i in range(paths.qsize()):
            temp = paths.get()
            paths.put(temp)
            path_arr.append(hasMove(temp,start,grid))
        for val in path_arr:
            if(val):
                dead_end = dead_end or val
        if(not dead_end):
            return
    return reconstruct_path(add,grid,start,end,draw)