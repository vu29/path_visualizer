from numpy.f2py.crackfortran import true_intent_list
import pygame

from node import Node,colors
from utils import *




WIDTH = 900
ROWS = 60

WINDOW = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Path Visualizer")


def main(window,side_length,rows):

    assert(int(side_length/rows) == side_length/rows)

    grid = make_grid(rows,side_length)

    start,end = None,None

    run = True
    algo_started = False

    while run:
        draw(window,grid,rows,side_length)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            ## if algo is started disable any update event from user
            if algo_started:
                continue
            
            ## left key
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row,col = get_clicked_position(pos,rows,side_length)
                node = grid[row][col]
                if not start:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()

                elif node != start and node != end:
                    node.make_barrier()

            ## right key
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row,col = get_clicked_position(pos,rows,side_length)
                node = grid[row][col]

                node.reset()

                if node == start:
                    start = None

                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not algo_started:
                    pass


                

    
    pygame.quit()

if __name__ == '__main__':
    main(WINDOW,WIDTH,ROWS)

    

