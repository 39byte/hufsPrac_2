import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def dist(self, other):
        return (self-q).length()
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    @property
    def X(self):
        return self.x
    
    @property
    def Y(self):
        return self.y
    
    @X.setter
    def X(self, x):
        self.x = x
    
    @Y.setter
    def Y(self, y):
        self.y = y
    


p = Point(1, 2)
q = Point(2, 3)

r = p + q
print(r)

r = p - q
print(r)

print(p.length())
print(p.dist(q))

print(p.dot(q))

p.move(1, 1)
print(p)
print()
print(p.X, p.Y)