from node import Node
import colors
import pygame


def heuristic(pos1, pos2):
    x1,y1 = pos1
    x2,y2 = pos2

    return abs(x1-x2) + abs(y1-y2)

def make_grid(rows,side_length):
    grid = list()
    block_side = side_length // rows

    for row in range(rows):
        grid.append([])
        for col in range(rows):
            node = Node(row,col,block_side,rows)
            grid[row].append(node)

    return grid

def draw_grid(window,rows,side_length):
    gap = side_length // rows
    
    # Draw horizontal line 
    for row in range(rows):
        pygame.draw.line(window,colors.GRAY,(0,row*gap),(side_length,row*gap))

    # Draw vertical line 
    for col in range(rows):
        pygame.draw.line(window,colors.GRAY,(col*gap,0),(col*gap,side_length))

def draw(window,grid,rows,side_length):
    window.fill(colors.WHITE)
    
    for row in grid:
        for spot in row:
            spot.draw(window)

    draw_grid(window,rows,side_length)
    pygame.display.update()


def get_clicked_position(pos,rows,side_length):
    gap = side_length//rows
    y,x = pos
    
    row = y // gap
    col = x // gap

    return row,col
    

