#!/usr/bin/env python
# -*- coding: utf-8 -*-

# l=resolution
# i=pause
# _=snake size
# s=blobals().__setitem__
# n=tuple
# k=random(the module)
# a=pygame(the module)
# e=time(the module)
# y=pygame.display
# x=lost
# b=body
# d=sens (direction)
# o=head position
# w=window
# f=food position
# P=Play
# I=Initialize
# F=new Food
# C=Colorize
# K=handle Keydown
"""
Not to have a class, we use globals as context.
If fact, having "self.*" (or "s.*" for short) is still a lot of code.
So we removed the context class and use globals instead.
It also allow not to give some parameters to functions.

While 1:
  if _ not in globals:
    set l i _ s n a k and e variables in globals.
    set P I F C and K functions in globals.
    Calls I
  Calls P(lay)

Play:
  if x(dead):
    Calls I(nitialize)
  else:
    if not i(pause):
      remove tail, add head to body
      erase tail
      make head move
      set x = lost (head in body or out of window)
      if not x:
        color head in green
    for event in pygame.event.get():
      if event.type = exit:
        exit
      if event.type = keydown:
        Calls K(eydown handeling) (event.key)
      if food is eaten:
        extends body
        Calls F(create new food)
      sleep(0.05)
Initialize:
  set y = pygame.display
  initialise pygame
  set w = window(resolution)
  set i,x,b,d,o = 
    True, False, [], (0,0), center of window
  # pause|lost | body|sens| head
  color head in green
  Calls F(create new food)
  update window

F(new Food):
  set f = random x ; random y
  color food in red

Colorize:
  if rectangle is x, y:
    set rectange = x, y, size, size
  colorize rectangle in color
  update rectangle

K(handle keydown):
  if key is up:
    sens = 0, -1
  elif key is down:
    sens = 0, 1
  elif key is right:
    sens = 1, 0
  elif key is left:
    sens = -1, 0
  pause = key is space
"""

while "_" in globals() or (map(globals().__setitem__,
  "lain_snake", [
    (640,480), 1, 1, 1, 10, globals().__setitem__, tuple
  ] + map(__import__,("pygame", "random", "time")))+[
    s("P", lambda:
      x and
        I()
      or (
        i or (
          s("b", b[1:]+[o]),
          C(b[0], 0),
          s("o", n(o[j]+d[j]*_ for j in[0, 1])),
          (s("x", o in b or any(not 0<=o[j]<=l[j]-_ for j in[0, 1])))
          or x
          or C(o)
        ), [
          g.type==12 and exit()or g.type==2 and K(g.key)
          for g in a.event.get()
        ],
        o==f and (
          b.append(f),
          F()
        ),
        e.sleep(0.05)
      )
    ),
    s("I", lambda:(
      s("y", a.display),
      a.init(),
      s("w", y.set_mode(l)),
      map(s, "ixbdo", (1, 0, [], (0, 0), n(x/2-x/2%_ for x in l))),
      C(o),
      F(),
      y.flip())),
    s("F", lambda:(
      s("f", n(k.randrange(0, x-1, _)for x in l)),
      C(f, 255<<16))
    ), 
    s("C", lambda r, c=0xff00, h=1:
      h and
        C(r+(_, )*2, c, 0)
      or(
        w.subsurface(r).fill(c),
        y.update(r)
      )
    ),
    s("K", lambda k:
      0<k-272<5 and [
        (lambda v:
          (v[0]+d[0]or v[1]+d[1]) and (
            s("d", v),
            s("i", 0)
        ))(((0, -1), (0, 1), (1, 0), (-1, 0))[k-273])
      ] or
        s("i", k==32)
    ),
    I()
  ]):P()
