# Black_Hole is derived from only Simulton: each updates by finding and removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    def __init__(self,x,y,width,height):#,color):
        Simulton.__init__(self,x,y,width,height)
        #self._color = color
        
    def update(self, model):
        eaten = set()
        for z in model.find(isinstance):
            if self.contains(z):
                model.remove(z)
                eaten.add(z)
        return eaten
        
    def display(self, canvas):
        #print(self._x)
        wi = self.get_dimension()[0]
        he = self.get_dimension()[1]
        #print(self.get_dimension())
        canvas.create_oval(self._x-wi/2     , self._y-he/2,
                                self._x+wi/2, self._y+he/2,
                                fill= 'black')
    def contains(self,sphere):
        return self._x - self._width/2  <= sphere.__dict__['_x'] <= self._x + self._width/2 and\
               self._y - self._height/2 <= sphere.__dict__['_y'] <= self._y + self._height/2

