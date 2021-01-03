from colors import *
import pygame


class Node:
    def __init__(self, row, col, width, total_rows):   
        self.row = row                           
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = WHITE
        self.neighbors = []                     
        self.width = width
        self.total_rows = total_rows
    #get position of the node
    def get_pos(self):                                  
        return self.row,self.col
    # return true if node is closed
    def is_closed(self):                                
        return self.color == RED
    # return true if node is open
    def is_open(self):                                  
        return self.color == GREEN
    # returns true is node is a wall
    def is_wall(self):                                                    
        return self.color == BLACK
    # returns true if its a starting point
    def is_start(self):                                 
        return self.color == ORANGE
    # returns true if node is the end point
    def is_end(self):                                   
        return self.color == TURQUOISE
    # reset the node back to empty
    def reset(self):                                    
        self.color = WHITE
    # make the node a start point    
    def make_start(self):                               
        self.color = ORANGE
    # make the node a closed node
    def make_closed(self):                              
        self.color = RED
    # make the node an open node
    def make_open(self):                             
        self.color = GREEN
    # make the node a wall point
    def make_wall(self):                                
        self.color = BLACK
    # make the node an end point
    def make_end(self):                                 
        self.color = TURQUOISE
    # make the node a path point
    def make_path(self):                                
        self.color = PURPLE
    # draw the node on the window
    def draw(self,win):                                 
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))
    # update the neighbors of the node as long as it is valid and is not a wall point
    def update_neighbors(self,grid):                     
        self.neighbors = []
        if self.col>0 and not grid[self.row][self.col-1].is_wall():                        
            self.neighbors.append(grid[self.row][self.col-1])
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall():   
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_wall():   
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.row >0 and not grid[self.row - 1][self.col].is_wall():                     
            self.neighbors.append(grid[self.row - 1][self.col])
        
        