# Special is special type of Prey that can't be 'eaten'; 
#   it updates by moving erratically across the canvas.
#
# Initially displays as black circle with a radius
#   of 15 (width/height 30) and a speed of 100 that changes colors.
#
# Automatically dies 100 cycles after it is placed
#
# It spits out different colored ball objects every 5 cycles (20 balls
#  total during the life of the Special).


from prey import Prey
import random


class Special(Prey):
    radius = 10
    life = 100
    def __init__(self,x,y,width,height,angle,speed,color):
        Prey.__init__(self,x,y,width,height,angle,speed)
        self._color = color
        self._life = 0
        
    def update(self,model):
        if self.life == self._life:
            model.remove(self)
        colors = ['orange', 'yellow', 'green', 'purple', 'pink', 'brown', 'blue']
#         self.randomize_angle()
        if 0 < model.cycle_count % 7 <= 5:
            self._color = random.choices(colors)[0]
        else:
            self._color = random.choices(colors)[0]
        self.randomize_angle()
        if model.cycle_count % 5 == 0:
            #self.randomize_angle()
            model.add(model.Ball(self._x,self._y,10,10,self._angle,5,random.choices(colors)[0]))
#         self.randomize_angle()
#         model.add(model.Ball(self._x,self._y,10,10,self._angle,5,random.choices(colors)[0]))



#         for i in range(10):
#             self.randomize_angle()
#             model.add(model.Ball(self._x,self._y,10,10,self._angle,5,random.choices(colors)[0]))

    
        self._life += 1
        self.move()
        
         
    def display(self,canvas):
       canvas.create_oval(self._x-Special.radius      , self._y-Special.radius,
                                self._x+Special.radius, self._y+Special.radius,
                                fill=self._color)
