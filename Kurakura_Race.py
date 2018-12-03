# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:35:40 2018

@author: Posma
"""

#!/bin/python3
from turtle import Turtle
from random import randint


iren = Turtle()
iren.color('red')
iren.shape('turtle')
iren.penup()
iren.goto(-160,100)
iren.pendown()

kanaya = Turtle()
kanaya.color('yellow')
kanaya.shape('turtle')
kanaya.penup()
kanaya.goto(-160,70)
kanaya.pendown()

seli = Turtle()
seli.color('pink')
seli.shape('turtle')
seli.penup()
seli.goto(-160,40)
seli.pendown()

posma = Turtle()
posma.color('blue')
posma.shape('turtle')
posma.penup()
posma.goto(-160,10)
posma.pendown()



for turn in range(100):
  iren.forward(randint(1,4))
  kanaya.forward (randint(1,4))
  seli.forward (randint(1,4))
  posma.forward (randint(1,4))
  
input("Press Enter to close")

  
  
  



  
  
  


