from turtle import *

#settings
bgcolor("white")
pencolor("black")
pensize(1)
#hideturtle()
speed(13)

#einheiten
unit_länge = 25 
def forward_units(units):
  forward(units * unit_länge)
def backward_units(units):
  backward(units * unit_länge)

länge_achse = 10
max_länge_in_px = länge_achse*20


### koordinatensystem ###

penup()
right(90)
forward_units(0.25)
left(90)
pendown()


#gitter
penup()
right(180)
forward_units(länge_achse)
right(90)
forward_units(0.25 + länge_achse )
right(90)
pendown()

pencolor(0.9,0.9,0.9)
for e in range(2*länge_achse):
  pendown()
  forward_units(2*länge_achse)
  penup()
  right(90)
  forward_units(0.5)
  right(90)
  pendown()
  forward_units(2*länge_achse)
  penup()
  left(90)
  forward_units(0.5)
  left(90)
  pendown()

forward_units(2*länge_achse)
left(90)

for i in range(2*länge_achse):
  pendown()
  forward_units(2*länge_achse)
  penup()
  left(90)
  forward_units(0.5)
  left(90)
  pendown()
  forward_units(2*länge_achse)
  penup()
  right(90)
  forward_units(0.5)
  right(90)
  pendown()
forward_units(2*länge_achse)

penup()
right(90)
forward_units(länge_achse)
right(90)
forward_units(länge_achse)
left(90)
pendown()
pencolor(0,0,0)

#Achsen
for n in range(2):
  right(90)
  forward_units(länge_achse + 0.5)
  penup()
  backward_units( 2*länge_achse + 1 + 0.559 )
  forward_units(0.559)
  pendown()

  right(90)
  forward_units(0.25)
  right(120)
  forward_units(0.5)
  right(120)
  forward_units(0.5)
  right(120)
  forward_units(0.25)
  left(90) #pfeil

  forward_units( länge_achse + 0.5)

penup()
forward_units(länge_achse)
left(90)
forward_units(0.25)
right(90)
pendown()

#Einteilung
for y in range(4):
  penup()
  right(90)
  forward_units(0.25)
  right(90)
  forward_units(länge_achse)
  forward_units(0.25)
  right(90)
  for x in range(länge_achse):

      forward_units(0.5)
      right(90)
      forward_units(0.125)
      pendown()
      forward_units(0.25)
      penup()
      forward_units(0.125)
      backward_units(0.5)
      left(90)

      forward_units(0.5)
      right(90)
      pendown()
      forward_units(0.5)
      penup()
      backward_units(0.5)
      left(90)

goto(0,0)
left(180)
forward_units(länge_achse+1)
right(90)
forward_units(0.5)
#shape_x
pendown()
right(45)
forward_units(0.707)
left(135)
penup()
forward_units(0.5)
pendown()
left(135)
forward_units(0.707)
penup()
right(45)
forward_units(länge_achse+1+0.5)
left(90)
forward_units(länge_achse-0.25)
left(180)
pendown()
#shape_y
pendown()
right(45)
forward_units(0.3535)
penup()
forward_units(0.3535)
left(135)
penup()
forward_units(0.5)
pendown()
left(135)
forward_units(0.7)

penup()
forward_units(3)
### funktionen ###

#linear
"""
penup()
goto(-max_länge_in_px, -(max_länge_in_px+100))
pencolor(0.2, 0.4, 0.0)
pendown()

for x in range(-max_länge_in_px, max_länge_in_px):
    y = x*2+(unit_länge*2)
    goto(x, y)
position()
"""



#quadratisch

faktor = 0.5
penup()
goto(-max_länge_in_px, -(max_länge_in_px+100))
pencolor(0.2, 0.4, 0.0)
pendown()

for x in range(-max_länge_in_px, max_länge_in_px):
    y = x*x*(faktor*5)
    goto(x, y)
position()

#turtle.exitonclick()
input()