import pygame
import pygame_menu
from astar import *
from BFS import *
from DFS import *
from node import *
from how_to_use import *
from colors import *
from functools import partial

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,WIDTH)) 

#add the grid lines to the display
def draw_grid(win,rows,width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win,GREY,(0,i*gap),(width,i*gap))
        for j in range(rows):
            pygame.draw.line(win,GREY,(j*gap,0),(j*gap,width))
#draw on the window
def draw(win,grid,rows,width):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win,rows,width)
    pygame.display.update()
# make a 2d array of nodes 
def make_grid(rows,width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i,j,gap,rows)
            grid[i].append(node)
    return grid
# get the position of the mouse click
def get_clicked_pos(pos,rows,width):
    gap = width // rows
    y,x = pos
    row = y //gap
    col = x//gap
    return row,col
# main function to run the program
def main(win,width):
    # set caption of the window
    pygame.display.set_caption("Path Finding Algorithm")
    # initialize variables
    ROWS = 25
    grid = make_grid(ROWS,width)
    font = pygame.font.Font('freesansbold.ttf', 20) 
    algorithms = ["AStar", "BFS", "DFS"]
    node_types = ["Start","End","Wall"]
    current_node = 0
    current_algorithm= 0
    start = None
    end = None
    run = True
    started = False
    path_length = 0
    draw(win,grid,ROWS,width)
    # main loop to run program
    while run:
        # add the current node type and algorithm on the bottom of the window
        algorithm_label = font.render(f"Algorithm = {algorithms[current_algorithm]}",1,BLACK)
        node_label = font.render(f"Node = {node_types[current_node]}",1,BLACK)
        win.blit(algorithm_label, (WIDTH - algorithm_label.get_width() - 10,WIDTH-20))
        win.blit(node_label,(10,WIDTH-20))
        pygame.display.update()
        # check events 
        for event in pygame.event.get():
            # quit the program after exiting the window
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN:
                # execute the program
                if event.key == pygame.K_SPACE:
                    if start != None and end != None:
                        started = True
                        for row in grid:
                            for node in row:
                                node.update_neighbors(grid)
                        if current_algorithm == 0:
                            path_length = astar(grid,start,end,lambda: draw(win,grid,ROWS,width))
                        elif current_algorithm == 1:
                            path_length = BFS(lambda: draw(win,grid,ROWS,width),grid,start,end)
                        elif current_algorithm == 2:
                            path_length = DFS(lambda: draw(win,grid,ROWS,width),grid,start,end)
                        
                        start.make_start()
                        end.make_end()
                # change the node type
                if event.key == pygame.K_UP:
                    if current_node == 2:
                        current_node = 0
                    else:
                        current_node+=1
                    draw(win,grid,ROWS,width)
                if event.key == pygame.K_DOWN:
                    if current_node == 0:
                        current_node = 2
                    else:
                        current_node-=1
                    draw(win,grid,ROWS,width)
                # change the algorithm type
                if event.key == pygame.K_LEFT:
                    if current_algorithm == 0:
                        current_algorithm = 2
                    else:
                        current_algorithm-=1
                    draw(win,grid,ROWS,width)
                if event.key == pygame.K_RIGHT:
                    if current_algorithm == 2:
                        current_algorithm = 0
                    else:
                        current_algorithm+=1
                    draw(win,grid,ROWS,width)
                # reset the window
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    started = False
                    grid = make_grid(ROWS,width)
                    current_node = 0
                    draw(win,grid,ROWS,width)
            #if the program is executed display the path length and dont allow changing of grid
            if started:
                path_label = font.render(f"Path Length: {path_length}",1,BLACK)
                WIN.blit(path_label, (WIDTH-path_label.get_width()-10,10))
                pygame.display.update()
                continue
            # react to leeft click
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row,col = get_clicked_pos(pos,ROWS,width)
                node = grid[row][col]
                if node != start and node != end:
                    if current_node ==0:
                        if start == None:
                            start = node
                            node.make_start()
                            current_node +=1
                        else:
                            start.reset()
                            start = node
                            start.make_start()
                    elif current_node == 1:
                        if end == None:
                            end = node
                            node.make_end()
                            current_node+=1
                        else:
                            end.reset()
                            end = node
                            end.make_end()
                    elif current_node ==2:
                        node.make_wall()
                draw(win,grid,ROWS,width)
            # react to right click
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()  
                row,col = get_clicked_pos(pos,ROWS,width)
                node = grid[row][col]
                node.reset()   
                if node == start: 
                    start = None
                elif node == end:
                    end =None
                draw(win,grid,ROWS,width)
    pygame.quit()
    quit()
#display the main menu
def main_menu():
    pygame.init()
    pygame.display.set_caption("Menu")
    surface = pygame.display.set_mode((WIDTH,WIDTH))
    menu = pygame_menu.Menu(300,400,"Welcome",theme=pygame_menu.themes.THEME_BLUE)
    menu.add_button("Enter",partial(main,WIN,WIDTH))
    menu.add_button("How To Use", partial(how_to_use,WIDTH))
    menu.add_button("Quit",pygame_menu.events.EXIT)
    menu.mainloop(surface)

if __name__ == "__main__":
    main_menu()