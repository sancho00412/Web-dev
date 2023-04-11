# importing libraries

import pygame
import time
import random
import os
import math

# initialization

pygame.init()

# setting

height, width = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(pygame.image.load("C:\python2\week8\paint_elements\paint_icon.png"))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()
fps = 60
my_font = pygame.font.SysFont('', 25)
choosed = "NOTHING"
palette = "white"
position = (0, 0)
Check = True

# colors

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 255, 0)
lime = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
green = (0, 128, 0)
gray = (128, 128, 128)
maroon = (128, 0, 0)
olive = (128, 128, 0)
purple = (128, 0, 128)
teal = (0, 128, 128)
navy = (0, 0, 128)
brown = (139, 69, 19)
indigo = (75, 0, 130)
current_color = white
color_of_panel = (176, 224, 230)

# groups of colors

shades_of_red = [red, maroon, purple, magenta]
shades_of_blue = [blue, cyan, navy, indigo]
shades_of_green = [green, lime, teal, olive]
basic_colors = [black, white, gray, brown]
list_of_colors = [basic_colors, shades_of_red,
                  shades_of_green, shades_of_blue,]

# function for circle


def circle(display, color, coordinate, radius):
    pygame.draw.circle(display, color, coordinate, radius)


# function for rectangle

def rectangle(display, color, x, y, width, height):
    pygame.draw.rect(display, color, pygame.Rect(x, y, width, height))


# function for ellipse

def ellipse(display, color, x, y, width, height):
    pygame.draw.ellipse(display, color, pygame.Rect(x, y, width, height))

# function for line


def line(display, color, start_position, end_position):
    pygame.draw.line(display, color, start_position, end_position)

# palette


def panel_of_palette():
    surface = pygame.Surface((80, 80))
    for block in range(4):
        for color in range(4):
            pygame.draw.rect(
                surface, list_of_colors[block][color], pygame.Rect(20 * color, 20 * block, 16, 16))
    screen.blit(surface, (420, 100))
    pygame.display.update()


# setting the display


def control_panel():

    # loading images

    image_of_rectangle = pygame.image.load("C:\\python2\\week8\\paint_elements\\rectangle.png")
    image_of_circle = pygame.image.load("C:\python2\week8\paint_elements\circle.png")
    image_of_ellipse = pygame.image.load("C:\python2\week8\paint_elements\ellipse.png")
    image_of_line = pygame.image.load("C:\python2\week8\paint_elements\line.png")
    image_of_palette = pygame.image.load("C:\python2\week8\paint_elements\palette.png")

    # scaling images

    image_of_rectangle = pygame.transform.scale(image_of_rectangle, (100, 100))
    image_of_circle = pygame.transform.scale(image_of_circle, (100, 100))
    image_of_ellipse = pygame.transform.scale(image_of_ellipse, (100, 100))
    image_of_line = pygame.transform.scale(image_of_line, (100, 100))
    image_of_palette = pygame.transform.scale(image_of_palette, (100, 100))

    # borders
    pygame.draw.rect(screen, white, pygame.Rect(0, 0, 500, 100))
    border = pygame.draw.rect(screen, black, pygame.Rect(0, 99, width, 1))
    for i in range(width):
        if i % 100 == 0:
            pygame.draw.rect(screen, black, pygame.Rect(i, 0, 1, 100))
    pygame.draw.circle(
        screen, current_color, (438, 59), 7)
    # drawing images

    screen.blit(image_of_rectangle, (0, 0))
    screen.blit(image_of_circle, (100, 0))
    screen.blit(image_of_ellipse, (200, 0))
    screen.blit(image_of_line, (300, 0))
    screen.blit(image_of_palette, (400, 0))

    pygame.display.update()

# main loop


screen.fill(white)
exit = True
StartDrawing = False
while exit:

    # main condition

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

        # work with mouse

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            position = pygame.mouse.get_pos()
            StartDrawing = True
            # functions
            if position[1] <= 100:
                StartDrawing = False
                if position[0] >= 0 and position[0] < 100:
                    choosed = "Rectangle"
                if position[0] >= 100 and position[0] < 200:
                    choosed = "Circle"
                if position[0] >= 200 and position[0] < 300:
                    choosed = "Ellipse"
                if position[0] >= 300 and position[0] < 400:
                    choosed = "Line"
                if position[0] >= 400 and position[0] <= 500:
                    choosed = "Palette"
                    check = False

        # Choosing the color
        elif event.type == pygame.MOUSEMOTION:
            if StartDrawing:
                direction = event.pos
                x = direction[0]-position[0]
                y = direction[1]-position[1]
                if (position[0]+x < 101):
                    x = 101
                if (position[1]+y < 101):
                    y = 101
                if choosed == "Rectangle":
                    rectangle(screen, current_color,
                              position[0], position[1], x, y)
                if choosed == "Circle":
                    circle(screen, current_color, position, math.sqrt(
                        math.pow((position[0]-x), 2)+math.pow((position[1]-y), 2)))
                if choosed == "Ellipse":
                    ellipse(screen, current_color,
                            position[0], position[1], x, y)
                if choosed == "Line":
                    line(screen, current_color, position, (x, y))
        if choosed == "Palette":
            # (500,180)
            if not check:
                panel_of_palette()
                for block in range(4):
                    for color in range(4):
                        if 420+(color * 16) <= position[0] and 100+(block*16) <= position[1]:
                            current_color = list_of_colors[block][color]
                            # (438,59) get_pos helps
                            pygame.draw.circle(
                                screen, current_color, (438, 59), 7)
                            pygame.draw.rect(
                                screen, white, pygame.Rect(420, 100, 80, 80))
                            check = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.draw.rect(screen, white, pygame.Rect(0, 100, 500, 400))

    control_panel()
    pygame.display.update()