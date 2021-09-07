import pygame
import math
from queue import PriorityQueue

from node import Node,colors
from utils import *




WIDTH = 900

window = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Path Visualizer")


def main(window,side_length,rows):
    grid = make_grid(rows,side_length)

    start,end = None,None

    run = True
    algo_started = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            ## if algo is started disable any update event from user
            if algo_started:
                continue
            
            ## left key
            if pygame.mouse.get_pressed()[0]:
                pass

            ## right key
            elif pygame.mouse.get_pressed()[2]:
                pass
    
    pygame.quit()

    

