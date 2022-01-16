# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    radius = 5
    def __init__(self,x,y,width,height,angle,speed,color):
        Prey.__init__(self,x,y,width,height,angle,speed)
        self._color = color
        
    def update(self,model):
        if model.cycle_count % 7 == 0:
            new_speed = 10
            while 7 < self._speed + new_speed or self._speed + new_speed < 3:
                if random() < 0.5:
                    new_speed = random() * (-0.5)
                else:
                    new_speed = random() * (0.5)
            self._angle += new_speed
            self._speed += new_speed
        self.move()
        #self.wall_bounce()
         
    def display(self,canvas):
       canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill=self._color)