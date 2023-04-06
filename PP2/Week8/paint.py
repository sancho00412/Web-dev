import pygame

pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

colors = [RED, GREEN, BLUE]

# draw functions
def drawCircle( screen, x, y, color):
    pygame.draw.circle( screen, color, ( x ,y), 40)

def freeDraw( screen, x, y, color):
    pygame.draw.circle( screen, color, (x, y), 2)

def drawRect( screen, x, y, color):
    pygame.draw.rect(screen, color, (x, y, 50, 80))

screen.fill(WHITE)

i = 0 # color's index

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # choose color
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            i += 1
            i = i % 3

        # circle
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            (x, y) =  pygame.mouse.get_pos()
            drawCircle( screen, x, y, colors[i])
        
        # free drawing
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            (x, y) =  pygame.mouse.get_pos()
            freeDraw(screen, x, y, colors[i])

        # rectabgle
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            (x, y) = pygame.mouse.get_pos()
            drawRect( screen, x, y, colors[i])

        # eraser
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill(WHITE)

    pygame.display.update()
    clock.tick(60)