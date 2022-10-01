import random
import globals as gv
import pygame

def randomBoolean(probability):
    return random.random() < probability

def draw_rectangle(x, y, screen, block_size, color):
    pygame.draw.rect(screen, color, (x * block_size, y * block_size, block_size, block_size))