import pygame
# import math

SCREEN_WIDTH = 400
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
pygame.display.set_caption(" Path Finder Using A* Search Algo ")

CLOSED_COLOR = (55, 0, 200)
OPEN_COLOR = (0, 255, 0)
YELLOW = (255, 255, 0)
BACKGROUND_COLOR = (255, 255, 255)
BARRIER_COLOR = (0, 0, 0)
PATH_COLOR = (128, 0, 128)
START_COLOR = (255, 165, 0)
GREY = (128, 128, 128)
END_COLOR = (64, 224, 208)


class Locate:
    def __init__(self, row, column, width, total_rows):
        self.row = row
        self.column = column
        self.x = row * width
        self.y = column * width
        self.color = BACKGROUND_COLOR
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_position(self):
        return self.row, self.column

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def make_start(self):
        self.color = START_COLOR

    def make_closed(self):
        self.color = CLOSED_COLOR

    def make_open(self):
        self.color = OPEN_COLOR

    def make_barrier(self):
        self.color = BARRIER_COLOR

    def make_end(self):
        self.color = END_COLOR

    def make_path(self):
        self.color = PATH_COLOR

    def is_closed(self):
        return self.color == CLOSED_COLOR

    def is_open(self):
        return self.color == OPEN_COLOR

    def is_barrier(self):
        return self.color == BARRIER_COLOR

    def is_start(self):
        return self.color == START_COLOR

    def is_end(self):
        return self.color == END_COLOR

    def reset(self):
        self.color = BACKGROUND_COLOR
