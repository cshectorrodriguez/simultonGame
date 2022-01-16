# Hunter is derived from both the Mobile_Simulton and Pulsator classes;
#   each updates like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    dist = 200
    def __init__(self,x,y,width,height,angle,speed):
        Pulsator.__init__(self,x,y,width,height)
        Mobile_Simulton.__init__(self,x,y,width,height,angle,speed)

    def update(self, model):
        eaten = set()
        preys = model.find(isinstance)
        for z in preys:
            if self.contains(z):
                model.remove(z)
                eaten.add(z)
        if len(eaten) == 0:
            self._pcounter += 1
            if self._pcounter == self.counter:
                self._width -= 1
                self._height -= 1
                self._pcounter = 0
        else:
            self._width += len(eaten)
            self._height += len(eaten)
            self._pcounter = 0
        if self._width == 0 and self._height == 0:
            model.remove(self)
        
        ##########################################
        x1 = self.get_location()[0]
        y1 = self.get_location()[1]
        chase = self.dist
        target = None
        for z in preys:
            if self.distance(z.get_location()) <= chase:
                chase = self.distance(z.get_location())
                target = z
        if target != None:
            x2 = target.get_location()[0]
            y2 = target.get_location()[1]
            new_x = x2-x1
            new_y = y2-y1
            self._angle = atan2(new_y,new_x)
        self.move()












        
#     def update(self, model):
#         eaten = set()
#         preys = model.find(isinstance)
#         for z in preys:
#             if self.contains(z):
#                 model.remove(z)
#                 eaten.add(z)
#         if len(eaten) == 0:
#             self._pcounter += 1
#             if self._pcounter == self.counter:
#                 self._width -= 1
#                 self._height -= 1
#                 self._pcounter = 0
#         else:
#             self._width += len(eaten)
#             self._height += len(eaten)
#             self._pcounter = 0
#         if self._width == 0 and self._height == 0:
#             model.remove(self)
#         
#         ##########################################
#         x1 = self.get_location()[0]
#         y1 = self.get_location()[1]
#         closest = 1000
#         #print(self._angle)
#         global dist
#         chase = 200
#         targets = set()
#         for z in preys:
#             x2 = z.get_location()[0]
#             y2 = z.get_location()[1]
#             
# #             if self.distance((x2,y2)) <= self.dist:
# #                 self.dist = self.distance((x2,y2))
# #                 new_x = x2-x1
# #                 new_y = y2-y1
# #                 new_angle = atan2(new_y,new_x)
# #                 self._angle = new_angle
# #                 self.dist = 200
#             if self.distance((x2,y2)) <= self.dist:
#                 targets.add(z)
#         target = None
#         for z in targets:
#             x2 = z.get_location()[0]
#             y2 = z.get_location()[1]
#             if self.distance((x2,y2)) <= chase:
#                 chase = self.distance((x2,y2))
#                 target = z
#         if target != None:
#             x2 = target.get_location()[0]
#             y2 = target.get_location()[1]
#             if self.distance((x2,y2)) <= self.dist:
#                 new_x = x2-x1
#                 new_y = y2-y1
#                 new_angle = atan2(new_y,new_x)
#                 self._angle = new_angle
                
                  
            
            
            
            
            
            
            
            
#             
#             
#         self.move()
#         pass
#     pass
