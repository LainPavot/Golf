#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Input(object):

  def __init__(self, *data):
    self.data = iter(data)

  def __call__(self):
    data = next(self.data)
    print(data)
    return data


def p(r,t,b,x=1):
 m=map;o=[' ']*max(m(len,(t,r)));p=o[:];t,n=list(t),1
 for s in b.split(", "):
  e,b,*_=m(int,(s+":"+s).split(":"));s=slice(-e-1,-b or 99);d=e-b+1;p[s]=e>b and"/%s\\"%("-"*(d-2))or"^";o[-e-1]=str(n);n+=1
  if x:t+=r[s]
  else:t[s],r=r[:d],r[d:]
 return[''.join(x).rstrip()for x in(o,p,t)]
i=input
f,g=i().split(" ")
o,s,r=p(g,"",i().split(": ",1)[1])
t,*_,u=i().split(" ")
print('\n'.join([f,o,s,g,"","="+r,"",t]+p(r,u,i().split(": ",1)[1],0)))


for input in (
  Input(*"""From: 010011010
Bits: 1:0, 6:4, 8
To:   000000000
Bits: 7:2""".split("\n")
  ), Input(*"""From: saint
Bits: 4, 0, 3:1
To:   _____
Bits: 4, 2, 3, 1:0""".split("\n")
  ), Input(*"""From: 0011010010101100100101
Bits: 0, 2, 5, 9:8, 11, 13, 16, 19:18
To:   000000000000
Bits: 11, 8:0""".split("\n")
  ), Input(*"""From: 100100010000100000
Bits: 5:0, 10:6, 14:11, 17:15
To:   000000000000000000
Bits: 17:15, 14:11, 10:6, 5:0""".split("\n")
  ), Input(*"""From: 0000011111
Bits: 9, 0, 8, 1, 7, 2, 6, 3, 5:4
To:   11111111110000000000
Bits: 14:5""".split("\n")
  )
):
  i=input
  f,g=i().split(" ")
  o,s,r=p(g,"",i().split(": ",1)[1])
  t,*_,u=i().split(" ")
  print('\n'.join([f,o,s,g,"","="+r,"",t]+p(r,u,i().split(": ",1)[1],0)))