# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    counter = 30
    def __init__(self,x,y,width,height):
        Black_Hole.__init__(self,x,y,width,height)
        self._pcounter = 0
    
    def update(self, model):
        #print(self.__dict__['_width'])
        eaten = set()
        #print(len(eaten))
        for z in model.find(isinstance):
            if self.contains(z):
                model.remove(z)
                eaten.add(z)
        if len(eaten) == 0:
            self._pcounter += 1
            if self._pcounter == self.counter:
                #print(self.width)
                self._width -= 1
                self._height -= 1
                self._pcounter = 0
        else:
            self._width += len(eaten)
            self._height += len(eaten)
            self._pcounter = 0
        if self._width == 0 and self._height == 0:
            model.remove(self)
        return eaten
            