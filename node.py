import colors
import pygame


class Node:
    #TODO: total_rows use
    def __init__(self,row,col,width,total_rows,color = colors.WHITE):
        self.row = row 
        self.col = col
        self.x = row * width
        self.y = col * width
        self.total_row = total_rows
        self.color = color

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
        return self.color == colors.YELLOW

    def is_path(self):
        return self.color == colors.VIOLET

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
        self.color = colors.YELLOW

    def make_path(self):
        self.color = colors.VIOLET

    def draw(self,window):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))

    def update_neighbours(self,grid):
        pass
    
    def __lt__(self,other_node):
        return False




    

    

    


    
