import pygame

CLOSED_COLOR = (55, 0, 200)
OPEN_COLOR = (0, 255, 0)
YELLOW = (255, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)
BARRIER_COLOR = (255, 255, 255)
PATH_COLOR = (128, 0, 128)
START_COLOR = (255, 165, 0)
GREY = (128, 128, 128)
END_COLOR = (64, 224, 208)
SCREEN_WIDTH = 400
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
pygame.display.set_caption(" Path Finder Using A* Search Algo ")


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

    def __lt__(self, other):
        return False

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

    # SAVE ALL FOUR NEIGHBOURS IF THEY ARE NOT BARRIERS TO THE START NODE
    def update_neighbors(self, grid):
        self.neighbors = []
        # NEIGHBOUR ABOVE
        if self.row > 0 and not grid[self.row - 1][self.column].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.column])
        # NEIGHBOUR LEFT
        if self.column > 0 and not grid[self.row][self.column - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.column - 1])
        # NEIGHBOUR BELOW
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.column].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.column])
        # NEIGHBOUR RIGHT
        if self.column < self.total_rows - 1 and not grid[self.row][self.column + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.column + 1])


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for x in range(rows):
        grid.append([])
        for y in range(rows):
            node = Locate(x, y, gap, rows)
            grid[x].append(node)

    return grid


def draw_grid(window, rows, width):
    space = width // rows
    for n in range(rows):
        pygame.draw.line(window, GREY, (0, n * space), (width, n * space))
        for s in range(rows):
            pygame.draw.line(window, GREY, (s * space, 0), (s * space, width))


def draw(window, grid, rows, width):
    #  window.fill(BACKGROUND_COLOR)
    for row in grid:
        for node in row:
            node.draw(window)
            draw_grid(window, rows, width)
            pygame.display.update()


def main(window, width):
    ROWS = 50
    grid = make_grid(ROWS, width)
    draw(window, grid, ROWS, width)


main(WINDOW, SCREEN_WIDTH)
