import pygame
import sys
pygame.init()
w,h=400,300
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption("My ball")


size=50
radius=25
ball_pos=[200,150]
color_screen=(255,255,255) #white
color_ball=(255,0,0) #red
speed=30


while True:
    screen.fill(color_screen)
    pygame.draw.circle(screen,color_ball,ball_pos,radius)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                ball_pos[1]-=speed
            elif event.key==pygame.K_LEFT:
                ball_pos[0] -= speed
            elif event.key==pygame.K_RIGHT:
                ball_pos[0]+=speed
            elif event.key==pygame.K_DOWN:
                ball_pos[1]+=speed
    if ball_pos[0] < radius:
      ball_pos[0] =radius
    elif ball_pos[0] > w-radius:
     ball_pos[0] = w -radius

    if ball_pos[1] < radius:
      ball_pos[1] = radius
    elif ball_pos[1] > h - radius:
      ball_pos[1] = h - radius        