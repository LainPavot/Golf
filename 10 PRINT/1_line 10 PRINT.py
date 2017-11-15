#!/usr/bin/env python
# -*- coding: utf-8 -*-

while"p"in globals()or(map(globals().__setitem__,"baltox",map(__import__,["pygame",
"random"])+[globals().__setitem__,lambda:(b.init(),map(l,"d_j",(b.display,(800,)*2,
range)),l("w",d.set_mode(_))),lambda:(l("u",b.key.get_pressed()),u[32]and(l("z",20)
,[(l("v",a.random()>0.5),b.draw.line(w,(255,)*3,(f,y+v*z),(f+z,y+z*(not v))))for f
in j(0,_[0],z)for y in j(0,_[1],z)],d.flip())or u[113]and x(),[e.type==12 and x()
for e in b.event.get()]),exit]),t()):o()

exit()
import pygame

import random

# set our screen's width and height
screenWidth, screenHeight = (800, 800)

pygame.init()

pygame.display.set_caption("10 PRINT in Pygame")
screen = pygame.display.set_mode((screenWidth, screenHeight))

running = True

white = (255, 255, 255)
black = (0, 0, 0)

# size of square, in pixels
square = 20

def drawScreen():
    screen.fill(black)
    # Python version of 10 PRINT happens here
    for x in range(0, screenWidth, square):
        for y in range(0, screenHeight, square):
            if random.random() > 0.5:
                pygame.draw.line(screen, white, (x, y), (x + square, y + square))
            else:
                pygame.draw.line(screen, white, (x, y + square), (x + square, y))

while running:
    key = pygame.key.get_pressed()
    # only draw if user presses spacebar
    if key[pygame.K_SPACE]:
        drawScreen()
    # quit if user presses q
    if key[pygame.K_q]:
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # this updates the display
    pygame.display.flip()
