class Point:
    k = 2  #class variable
    def __init__(self,x,y):
        self.x = x #instance variable
        self.y = y
    def move(self):
        print('move')
    def draw(self):
        print('draw')
point = Point(2,3)
print(point.x)
point.draw()

class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f'hi, i am {self.name} ')
obj = Person('srikrishna')
obj.talk()

class Mammel:
    def walk(self):
        print('walk')
class Dog(Mammel):
    pass
class Cat(Mammel):
    def be_annoying(self):
        print('annoying')
cat1 = Cat()
cat1.walk()
cat1.be_annoying()

# multilevel inheritance:
# multiple inheritance = child derived from 2 parents
class Prey:
    def flee(self):
        print('this animal flees')
class Predator:
    def hunt(self):
        print('this animal is hunting')
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()
rabbit.flee()
hawk.hunt()
# fish.flee()
# fish.hunt()

class Overriding:
    def eat(self):
        print('this animal is eating')
class Rabbit:
    def eat(self):
        print('this rabbit eatin a carrot')

class Method_chaining:
    def turn_on(self):
        print('you start the engine')
        return self
    def drive(self):
        print('you drive the car')
        return self
    def brake(self):
        print('you stop on the brakes')
        return self
    def turn_off(self):
        print('you turn on the engine')
        return self
car = Method_chaining()
car.turn_on().drive().brake().turn_off()

#super() = returns a temporary object of parent class
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.width
class Cube(Rectangle):
    def __init__(self, length, width,height):
        super().__init__(length, width)
        self.height = height
    def volume(self):
        return self.length*self.width*self.height
square = Square(3,3)
cube = Cube(3,3,3)
print(square.area())
print(cube.volume())

# abstract prevents creating object and compels a user to override abstract methods
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
class Car(Vehicle):
    def go(self):
        print('drive the car')
class Motorcycle(Vehicle):
    def go():
        print('let ride the motorcycle')
# veh = Vehicle()
car = Car()
motorcycle = Motorcycle()
# veh.go()
car.go()
motorcycle.go()

# object as parameter
class Car:
    color = None
class Motorcycle:
    color = None
def change_color(vehicle,color):
    vehicle.color = color
car1 = Car()
car2 = Car()
bike1 = Motorcycle()
change_color(car1,'red')
change_color(car2,'green')
change_color(bike1,'blue')
print(car1.color)
print(car2.color)
print(bike1.color)

# Duck typing = object given less importance than methods , if walk and quakes like duck then duck
class Duck:
    def walk(self):
        print('this duck is walking')
    def talk(self):
        print('this duck is qwuacking')
class Chicken:
    def walk(self):
        print('this chicken is walking')
    def talk(self):
        print('this chicken is clucking')
class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()
duck = Duck()
chicken = Chicken()
person = Person()
person.catch(duck)
person.catch(chicken)

# walrus operator := 
foods = list()
while True:
    food = input('what food do u like?:')
    if food == 'quit':
        break
    foods.append(food)

foods = list()
while food := input('what food do u like?:') != "quit":
    foods.append(food)