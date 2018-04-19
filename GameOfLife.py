#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import time
import random


res = (640, 480)
size = 8
X, Y = res[0]//size,res[1]//size
rule = {1:{2,3}, 0:{3}}
pygame.display.init()
f = pygame.display.set_mode(res)


def set_alive(pos):
  x,y=pos[0]//size,pos[1]//size
  grid[y][x] = not grid[y][x]

def set_random():
  global grid
  grid = [[
      random.randint(0,1)
      for x in range(X)
    ] for y in range(Y)
  ]


def neighboors(x, y):
  return sum(
   1 for c in (x+1, x, x-1) for l in (y+1, y, y-1)
   if X>c>=0 and Y>l>=0 and grid[l][c] and (c,l)!=(x,y)
  )


def next_gen():
  global grid
  grid = [[
      neighboors(x,y) in rule[grid[y][x]]
      for x in range(X)
    ] for y in range(Y)
  ]


def display():
  f.fill(0)
  for y, r in enumerate(grid):
    for x, a in enumerate(r):
      a and f.blit(w, (x*size,y*size))
  else:
    pygame.display.flip()


pause = 1
grid = [[0]*X]*Y
w = pygame.Surface((size,)*2)
w.fill((255,)*3)
while 1:
  time.sleep(0.01)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        set_alive(event.pos)
      elif event.button == 3:
        set_random()
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      pause = not pause
  grid and (pause or next_gen(), display())
  
  