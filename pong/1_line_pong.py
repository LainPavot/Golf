#!/usr/bin/env python
# -*- coding: utf-8 -*-
# x, y, z = iter vals or params
# p = pause
# o = ?
# n = math
# g = G-setter
# _ = resolution
# b = ?
# y = ?
# _ = resolution
# l = ?
# a = time
# i = pygame
# n = math
# c = pygame.display
# d = player lost
# e = player position
# f = AI position
# h = palette height
# j = ball size
# k = ball position
# m = ball angle
# r = AI lost
# w = window
# 
# I = initialize
# L = play
# M = move
# D = display all
# K = futur k
#def prt(x):
  #print x
while"p"in globals()or(map(globals().__setitem__,"pong_by_lainILhjDK",
[1,0,0,globals().__setitem__,0,0,0,(640,480),0]+map(__import__,["time"
,"pygame","math"])+[lambda:(i.init(),map(g,"cpdefkm",(i.display,1,0,(0
,(_[1]-h)/2),(_[0]-j,(_[1]-h)/2),((_[0]-j)/2,(_[1]-j)/2),n.pi)),g("w",
c.set_mode(_)),D()),lambda:(a.sleep(0.005),[g("p",not p)if x.type==2
and x.key==32 else exit()if x.type==12 else""for x in i.event.get()],d
and I()or p or(w.fill(0),g("e",(e[0],e[1]-(i.key.get_pressed()[273]and
e[1]>0)/2.+(i.key.get_pressed()[274]and e[1]+h<_[1])/2.)),g("k",K()),0
<=K()[1]<=_[1]-j or g("m",m+(n.pi-m)*2),(n.pi/2<m<n.pi*1.5 and[0<k[0]<
j and e[1]<k[1]+j/2<e[1]+h and g("m",n.pi-m-(e[1]+(h-j)/2.-k[1])/h)])
or _[0]-j<k[0]+j<_[0]and f[1]<k[1]+j/2<f[1]+h and g("m",(n.pi-m)%n.pi+
(f[1]+(h-j)/2.-k[1])/h),g("z",(f[0],f[1]+((-0.7 if(f[1]+h/2)>k[1] else
0.7)if k[0]>_[0]/2. else 0))),0<=z[1]<=_[1]-h and g("f",z),g("d",k[0]<
0),g("r",k[0]+j>_[0]),d or r and I(),D())),64,8,lambda:([w.subsurface(
*x).fill((255,)*3)for x in(e+(j,h),f+(j,h),k+(j,j),(_[0]/2-1,0,2,_[1])
)],c.flip()),lambda:(k[0]+n.cos(m),k[1]+n.sin(m))]),I()):L()