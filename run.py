import numpy as np
import pygame
from constants import *
from pygame.locals import *

l = []
s = reversed(SIZE)
for x in s:
    l.append(x)

s = l

del l

# print(s)

grid = np.zeros(s, dtype=np.int8)

won = 0

finish = False

player = 1

RS = (SIZE[0]*X+2*STEP, SIZE[1]*Y+2*STEP)


def init():
    pygame.init()
    screen = pygame.display.set_mode(RS)
    return screen


def drawLines(screen: pygame.Surface, grid: np.ndarray):
    screen.fill((255, 255, 255))
    for x in range(SIZE[0]+1):
        pygame.draw.line(screen, (0, 0, 0), (STEP+x*X, STEP),
                         (STEP+x*X, RS[1]-STEP))
    for x in range(SIZE[1]+1):
        pygame.draw.line(screen, (0, 0, 0), (STEP,  STEP+x*Y),
                         (RS[0]-STEP,  STEP+x*Y))


def drawGrid(screen: pygame.Surface, grid: np.ndarray, radius: float):
    # for x in range(len(grid)
    for y in range(SIZE[1]):
        for x in range(SIZE[0]):
            g = grid[y, x]
            if g != 0:
                pygame.draw.circle(screen, COLOURPLAYER1 if g == 1 else COLOURPLAYER2,
                                   (STEP+x*X+STEP*0.5, STEP+y*Y+STEP*0.5), radius)


def draw(screen: pygame.Surface, grid, pos, player):
    RADIUS = STEP*0.8/2
    "+-+-+-+-+-+-+-+"
    "| | | | | | | |"
    "+-+-+-+-+-+-+-+"
    "| | | | | | | |"
    "+-+-+-+-+-+-+-+"
    "| | | | | | | |"
    "+-+-+-+-+-+-+-+"
    "| | | | | | | |"
    "+-+-+-+-+-+-+-+"
    "| | | | | | | |"
    "+-+-+-+-+-+-+-+"
    "| | | | | | | |"
    "+-+-+-+-+-+-+-+"
    drawLines(screen, grid)

    if pos != -1:
        realPos = (STEP+pos*X+STEP/2, 50)
        # print(player)
        pygame.draw.circle(screen, COLOURPLAYER1 if player ==
                           1 else COLOURPLAYER2, realPos, RADIUS)
    else:
        pass

    drawGrid(screen, grid, RADIUS)

    pygame.display.update()


def dropToken(colomn, player):
    # c = copy.deepcopy(colomn)

    for x in range(len(colomn)):
        y = colomn[len(colomn)-x-1]
        if y == 0:
            colomn[len(colomn)-x-1] = player
            return True

    else:
        return False


def gridFull(grid):
    # full = True
    for x in grid:
        for y in x:
            if y == 0:
                return False
    return True

def playerWon(grid):
    ...

screen = init()

pos = -1

while not finish:

    turnFinished = False

    # pos = -1

    # print(grid)

    while not turnFinished:

        draw(screen, grid, pos, player)

        if gridFull(grid):
            turnFinished = True
            player = 1
            grid = np.zeros(s, dtype=np.int8)


        events = pygame.event.get()

        # print(events, end="\r")

        for x in events:
            if x.type == pygame.QUIT:
                exit()

            # print(x.type)

            if x.type == MOUSEMOTION:
                # print(x)

                p = x.pos[0]

                # print(p)

                p2: int = (p-STEP)//X

                r = 0

                if p2 < 0:
                    r = -1

                elif p2 < SIZE[0]:
                    r = p2
                else:
                    r = -1

                # print(r)
                pos = r

            if x.type == KEYDOWN:
                print(x)
                if x.key == pygame.K_r:
                    grid = np.zeros(s, dtype=np.int8)
                    player = 1

            if x.type == pygame.MOUSEBUTTONDOWN:
                # print(x)
                p = x.pos[0]

                # print(p)

                p2: int = (p-STEP)//X

                r = 0

                if p2 < 0:
                    r = -1

                elif p2 < SIZE[0]:
                    r = p2
                else:
                    r = -1

                pos = r

                if pos != -1:
                    tmp = grid[:, pos]

                    if dropToken(tmp, player) == True:
                        turnFinished = True
                    else:
                        pass

                # print(r)

        # print(str(pos)+" ", end="\r")

    player = 3-player
