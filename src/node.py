import colors
import pygame


class Node:
    #TODO: total_rows use
    def __init__(self,row,col,width,total_rows,color = colors.WHITE):
        self.row = row 
        self.col = col
        self.x = row * width
        self.y = col * width
        self.total_rows = total_rows
        self.neighbors = []
        self.color = color
        self.width = width

    def get_pos(self):
        return (self.row,self.col)

    '''
    Defining the state-color code for the nodes
    unreached : white
    open : green
    barrier : black
    start : violet
    end : cyan
    path : violet
    '''

    # State getters for the node

    def is_closed(self):
        return self.color == colors.RED

    def is_open(self):
        return self.color == colors.GREEN

    def is_barrier(self):
        return self.color == colors.BLACK

    def is_start(self):
        return self.color == colors.CYAN

    def is_end(self):
        return self.color == colors.DARK_BLUE

    def is_path(self):
        return self.color == colors.PURPLE

    # State setter for the node

    def reset(self):
        self.color = colors.WHITE

    def make_closed(self):
        self.color = colors.RED

    def make_open(self):
        self.color = colors.GREEN

    def make_barrier(self):
        self.color = colors.BLACK

    def make_start(self):
        self.color = colors.CYAN

    def make_end(self):
        self.color = colors.DARK_BLUE

    def make_path(self):
        self.color = colors.PURPLE

    def draw(self,window):
        pygame.draw.rect(window,self.color,(self.x,self.y,self.width,self.width))

    def update_neighbors(self,grid):
        self.neighbors = []
        ## Down 
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        ## Up
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        ## Left 
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col -1])

        ## Right
        if self.col < self.total_rows -1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

    
    # def __lt__(self,other_node):
    #     return False




    

    

    


    
