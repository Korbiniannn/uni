import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5
    
    def euclidean_distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    
    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)
    
    def angle_between(self, other):
        vert = other.y - self.y
        horiz = other.x - self.x
        return math.atan2(vert, horiz)
class triangle:
    def __init__(self, p1 = Point, p2 = Point, p3 = Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def side_lengths(self,):
        print("Hi")
    
    def angles(self,):
        pass

    def side_classification(self,):
        pass

    def angle_classification(self,):
        pass

    def is_right(self,):
        pass

    def area(self,):
        pass

    def perimeter():
        pass
