from queue import PriorityQueue
from utils import heuristic
import math
import pygame


def reconstruct(draw,came_from,current):
    while current in came_from:
        current.make_path()
        current = came_from[current]
        print(current)
        draw()


def a_star(draw,grid,start,end):
    '''
    -> F(s) = H(s) + G(s)
            H(s) : heuristic distance (manhattan distance in this case)
            G(s) : shortest distance from start node to current node

    -> open_set is the set of nodes currently in traversal sorted according to f-score
    -> count is used as a tie-breaker for those nodes having same f-score, to precedes another
    -> came_for dictionary is used for back-tracking
    
    '''
    count = 0
    open_set = PriorityQueue()
    open_set.put((0,count,start))
    came_from = {}
    g_score = {node : float('inf') for row in grid for node in row}
    g_score[start] = 0
    f_score = {node : float('inf') for row in grid for node in row}
    f_score[0] = heuristic(start.get_pos(),end.get_pos())

    open_set_hash = set([start])

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            ##TODO : make path
            end.make_end()
            reconstruct(draw,came_from,came_from[current])
            return True
        
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor.get_pos(),end.get_pos())

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor],count,neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

