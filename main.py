# Imports
from tkinter import *
from time import sleep
from random import randint

# Screen setup
tk = Tk()
s = Canvas(tk, width = 600, height = 400, background = "powder blue")
s.pack()





#######################
# AIRPLANE #
#######################

# Creating airplane function
def create_airplane(x,y):

  # back circle
  s.create_oval(100+x,200+y, 275+x,250+y, fill = "white", outline = "white", width = 2)

  # main body
  s.create_rectangle(155+x,200+y, 450+x,250+y, fill = "white", outline = "")


  # FRONT #

  # front bottom circle
  s.create_oval(400+x,215+y, 500+x,250+y, fill = "white", outline = "")
  
  # shading in front circle
  s.create_arc(400+x,215+y, 500+x,250+y, start = 90, extent = -180, fill = "grey97", outline = "")
  
  # front top circle for cockpit
  s.create_oval(430+x,200+y, 475+x,250+y, fill = "white", outline = "")

  # cockpit
  s.create_polygon(450+x,205+y, 465+x,205+y, 470+x,217+y, 450+x,217+y, fill = "grey30", outline = "") 


  # ENGINE #
  
  # main body of engine 
  s.create_oval(300+x,250+y, 330+x,280+y, fill = "white", outline = "")
  
  # inside of engine
  s.create_oval(310+x,250+y, 330+x,280+y, fill = "honeydew4", outline = "dodger blue")

  # engine fans
  start = 0

  for l in range(12): 
    s.create_arc(310+x,250+y, 330+x,280+y, start = start, extent = 2, fill = "grey30")
    start += 30

  # engine center (fan holder)
  s.create_oval(315+x,260+y, 325+x,270+y, fill = "grey30", outline = "")


  # ACCESSORIES #
  
  # large blue line
  s.create_line(123+x,240+y, 497+x,240+y, fill = "dodger blue", width = 2)
  
  # entry door left
  s.create_rectangle(165+x,210+y, 185+x,237+y, fill = "", outline = "honeydew4", width = 2)

  # entry door right
  s.create_rectangle(427+x,210+y, 445+x,237+y, fill = "", outline = "honeydew4", width = 2)


  # WINGS #

  # top wing
  s.create_polygon(205+x,200+y, 175+x,145+y, 155+x,145+y, 155+x,200+y, fill = "dodger blue", outline = "honeydew4") 

  # top wing blue line
  s.create_line(155+x,195+y, 202+x,195+y, fill = "turquoise", width = 2)
  
  # bottom side wing
  s.create_polygon(250+x,250+y, 225+x,275+y, 275+x,275+y, 350+x,250+y, fill = "dodger blue", outline = "honeydew4")

  # back side wing
  s.create_polygon(125+x,225+y, 105+x,250+y, 130+x,250+y, 150+x,225+y, fill = "dodger blue", outline = "honeydew4")


  # WINDOWS #
  xw = 200

  for w in range(9):
    s.create_oval(xw+x,210+y, xw+x+17,230+y, fill = "honeydew4")
    xw += 25

# Create the airplane
create_airplane(0,0)






#######################
# FLYING ANIMATION #
#######################

# Movement values for clouds and bird wing
xval = 400
birdw = 0

# Animation
while xval + 500 >= 325:

  #######################
  # CLOUDS #
  #######################

  # cloud 1 (on airplane)
  cloud1 = s.create_polygon(xval,250, xval+200,250, xval+200,225, xval+150,200, xval+100,200, xval+50,225, fill = "alice blue", outline = "", smooth = True)

  # cloud 2 (top cloud)
  cloud2 = s.create_polygon(xval+350,150, xval+550,150, xval+550,125, xval+500,100, xval+450,100, xval+400,125, fill = "alice blue", outline = "", smooth = True)

  # cloud 3 (bottom cloud)
  cloud3 = s.create_polygon(xval+450,350, xval+650,350, xval+650,325, xval+600,300, xval+550,300, xval+500,325, fill = "alice blue", outline = "", smooth = True)



  #######################
  # BIRD #
  #######################

  # Body
  body = s.create_oval(xval+505,258, xval+520,277, fill = "goldenrod4", outline = "")

  # Head
  head = s.create_oval(xval+500,255, xval+510,265, fill = "saddle brown", outline = "")

  beak = s.create_polygon(xval+500,257, xval+495,260, xval+500,263, fill = "yellow", outline = "")

  eye = s.create_oval(xval+503,257, xval+507,260, fill = "white", outline = "")

  # wing
  wing = s.create_polygon(xval+513,265, xval+528,255+birdw, xval+528,275+birdw, xval+513,270, fill = "gold", outline = "saddlebrown")



  # Decrements
  xval -= 5

  # Flapping motion on wings
  if birdw == 0: birdw = -5
  else: birdw = 0


  # Update, sleep, delete
  s.update()
  sleep(0.03)
  s.delete(cloud1, cloud2, cloud3, body, head, beak, eye, wing) 








###################################
# ANIMATION TO SET ENGINE ON FIRE #
###################################

# for moving the fire
f = 0

while xval + 700 > 0: 

  #######################
  # FIRE ON ENGINE #
  #######################
  
  orange = s.create_polygon(310-f,275, 310-f,245-f, 315-f,260, 320,245-f, 325+f,260, 330+f,245-f, 335+f,275, fill = "orange", smooth = True)

  yellow = s.create_polygon(312-f,275, 312-f,250-f, 320-f,265, 320,250-f, 325+f,265, 330+f,250-f, 330+f,275, fill = "yellow", smooth = True)



  #######################
  # CLOUDS #
  #######################

  cloud1 = s.create_polygon(xval,250, xval+200,250, xval+200,225, xval+150,200, xval+100,200, xval+50,225, fill = "alice blue", outline = "", smooth = True)

  cloud2 = s.create_polygon(xval+350,150, xval+550,150, xval+550,125, xval+500,100, xval+450,100, xval+400,125, fill = "alice blue", outline = "", smooth = True)

  cloud3 = s.create_polygon(xval+450,350, xval+650,350, xval+650,325, xval+600,300, xval+550,300, xval+500,325, fill = "alice blue", outline = "", smooth = True)



  # Increments/ Decrements
  xval -= 5

  if f > 10: f = 0
  else: f += 0.3


  # Update, sleep, delete
  s.update()
  sleep(0.03)
  s.delete(cloud1, cloud2, cloud3, body, head, beak, eye, wing, orange, yellow) 








############################
# ANIMATION TO CRASH PLANE #
############################

# for airplane- position and speed of falling
x = 0
y = 0
rate = 1

# Making the airplane fall
for falling in range(150):

  # Airplane
  create_airplane(x,y)

  # FIRE
  orange = s.create_polygon(310-f+x,275+y, 310-f+x,245-f+y, 315-f+x,260+y, 320+x,245-f+y, 325+f+x,260+y, 330+f+x,245-f+y, 335+f+x,275+y, fill = "orange", smooth = True)

  yellow = s.create_polygon(312-f+x,275+y, 312-f+x,250-f+y, 320-f+x,265+y, 320+x,250-f+y, 325+f+x,265+y, 330+f+x,250-f+y, 330+f+x,275+y, fill = "yellow", smooth = True)



  # Increments
  y += 5*rate
  x += 1*rate

  if f > 30: f = 0
  else: f += 0.5


  # Increasing the speed of falling and changing position in 50 frame increments (when airplane goes out of screen)
  if falling == 50:
    x = -100
    y = -300
    rate = 3
    
  if falling == 100:
    x = -50
    y = -250
    rate = 3



  # Update, sleep, delete
  s.update()
  sleep(0.03)
  s.delete("all")







############################
# EXPLOSION ANIMATION #
############################

xval = 0
yval = 0

while 200-yval > -100:

  # Smoke ovals
  s.create_oval(0-xval,250-yval, 300+xval,500-yval, fill = "grey", outline = "grey40")
  s.create_oval(400-xval,250-yval, 650+xval,500-yval, fill = "grey", outline = "grey40")
  s.create_oval(150-xval,150-yval, 500+xval,500-yval, fill = "grey", outline = "grey40")

  # Increments
  xval += 0.5
  yval += 1.5

  # Update, sleep, no delete for smoky effect
  s.update()
  sleep(0.05)


########
# END #
########
s.create_text(300,200, text = "The End", font = "Times 30 italic", fill = "white")