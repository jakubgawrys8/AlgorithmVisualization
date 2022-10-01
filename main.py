import pygame
import logging
import sys
import asyncio
import globals as gv
import helpers as h
import map as m
import calculate as c
import multiprocessing
import threading
from queue import Queue
import time
import pygame.freetype


m.generate_terrain()
# print("terrain len", len(gv.terrainList))

# gv.terrainList = [gv.Node(3, 1), gv.Node(3, 2), gv.Node(4, 2), gv.Node(5, 2), gv.Node(6, 2), gv.Node(7, 2)]
# starting_node = gv.Node(7, 4)
# starting_node.g = 0
# starting_node.f = 0
# ending_node = gv.Node(4, 1)

m.generate_walkable_list()
print("walkable len", len(gv.walkableList))

starting_node = gv.walkableList[0]
starting_node.g = 0
starting_node.f = 0

ending_node = c.choose_ending_node(starting_node)

print("starting node", starting_node.x, starting_node.y)
print("ending node", ending_node.x, ending_node.y)

gv.openList.append(starting_node)


def draw(starting_node, ending_node):

    draw_nodes_event = pygame.USEREVENT + 1
    pygame.time.set_timer(draw_nodes_event, 35)

    while True:

        gv.CLOCK.tick(30)
        if gv.game_end:
            m.draw_final_list()
            # m.draw_distance_values(True)
        
        m.draw_starting_node(starting_node)
        m.draw_ending_node(ending_node)
        m.draw_terrain()
        m.draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == draw_nodes_event:
                if not gv.game_end:
                    c.process_open_list(ending_node)
                    m.draw_closed_list(starting_node, ending_node)
                    m.draw_open_list(starting_node, ending_node)
                    # m.draw_distance_values()
                    m.draw_grid()

        # print(pygame.time.get_ticks())
        pygame.display.update()


if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption('A* Search Algorithm')

    draw(starting_node, ending_node)
