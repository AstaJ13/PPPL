#Write a Python program that uses object-oriented principles to calculate
#  the area of a Circle, Triangle, or Square based on user input.
#Abstraction             (abstraction, inheritance, and polymorphism )

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def Area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius= radius

    def Area(self):
        return math.pi * self.radius **2
    
class Triangle(Shape):
    def __init__(self,base,height):
        self.base= base
        self.height= height

    def Area(self):
        return 0.5* self.base * self.height

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def Area(self):
        return  self.side* self.side
    

def select():
    type= int(input("Select 1.Circle, 2.Traingle, 3.Square: " ))
    if type ==1:
        return Circle(float(input("Enter radius: ")))
    elif type ==2:
        return Triangle(float(input("Enter base: ")), float(input("enter height: ")))
    elif type == 3:
        return Square(float(input("Enter side:")))
    else:
        print("Invalid")
        return select()

if __name__ =="__main__":
    shape= select()
    print(f"Area: {shape.Area()} ")