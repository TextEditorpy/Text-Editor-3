class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
def area(self):
    return self.lenth * self.width
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

def area(self):
    return 3.14 * self.radius * self.radius
rectangle = Rectangle(4,5)
circle = Circle(3)

print("Rectangle Area:", rectangle.area())
print("Circle Area:",circle.area()) 
