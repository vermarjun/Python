#QUESTION 1
class Line:
    def __init__(self,point1,point2):
        self.point1 = point1
        self.point2 = point2
        self.x1 = self.point1[0]
        self.y1 = self.point1[1]
        self.x2 = self.point2[0]
        self.y2 = self.point2[1]
    def distance(self):
        distance = ((self.x2-self.x1)**2 + (self.y2-self.y1)**2)**0.5
        print(distance) 
    def slope(self):
        slope = (self.y2 - self.y1)/(self.x2 - self.x1)
        print(slope) 
#Check Point
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()
li.slope()

#QUESTION2 
class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        self.pi = 3.14
    def volume(self):
        volume = (self.pi*((self.radius)**2)*(self.height))
        print(volume)
    def surface_area(self):
        area = 2*self.pi*self.radius*(self.radius+self.height)
        print(area)
#Check Point
c = Cylinder(2,3)
c.volume()
c.surface_area()