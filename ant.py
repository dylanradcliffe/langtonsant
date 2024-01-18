import pygame

SCREENWIDTH = 1200
SCREENHEIGHT = 768

TILEPIXELSX = 4
TILEPIXELSY = 4

N = 10 # steps per frame

TILEWIDTH = SCREENWIDTH // TILEPIXELSX
TILEHEIGHT = SCREENHEIGHT // TILEPIXELSY

tiles =[False] * TILEWIDTH * TILEHEIGHT


def xy2tile(x, y):
    return (TILEWIDTH * (y % TILEHEIGHT)) + (x % TILEWIDTH)


def drawTile(surface, x,y):
    col = (0,0,0) if tiles[xy2tile(x,y)]  else (255,255,255)
    #print(x,y,col)
    pygame.draw.rect(surface, col, pygame.Rect(x * TILEPIXELSX, y * TILEPIXELSY, TILEPIXELSX, TILEPIXELSY))
    #print((surface, col, pygame.Rect(x * TILEPIXELSX, y * TILEPIXELSY, TILEPIXELSX, TILEPIXELSY)))

def drawTiles(surface):
   for y in range(TILEHEIGHT):
        for x in range (TILEWIDTH):
           drawTile(surface, x, y)



def turn(v, dir):
    dx, dy = v
    return (-dir * dy, dir * dx)

def advanceAnt(p, v):
    x,y = p
    dx,dy = turn(v, 1 if tiles[xy2tile(x,y)] else -1)
    tiles[xy2tile(x,y)]= not tiles[xy2tile(x,y)]
    newPos = x + dx, y + dy
    return newPos, (dx, dy)


#### MAIN

if __name__ == "__main__":

    antPos = (TILEWIDTH // 2,  TILEHEIGHT // 2)
    antV = (1,0)

    pygame.init()
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    pygame.display.set_caption("Langton's Ant")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        surface.fill((255,255,255))
        drawTiles(surface)
        screen.blit(surface,(0,0))
        pygame.display.flip()
        pygame.display.update()

        # move ant N steps per frame
        for i in range(N):
            antPos, antV = advanceAnt(antPos, antV)
        