from turtle import Turtle


name = int(input("Name: "))
#print(f"XXX {here}) allows us to instern anthing from the program into the {}
print(f"Hello, {name}")

n = intput("Number: ")

if n>0:
    print("n is positive")
elif n<0:
    print("n is neg")
else:
    print("n is zero")

# list []- list of mutable values
# we can use .append to add a value to the end of the list
# we can use .sort to sort the names. most often alphabetically



# tuple- sequence of immutable values


# set- collectioin of unique values
s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)

s.remove(2)

print(f"The set has {len(s)} elements")

#This is a simple list that that says to go through the list one at a time
#Then call that item i and print it 
for i in [0,1,2,3,4,5]:
    print(i)

for i in range(6):
    print(i)

names= [Harry, Ron, Jermey]

for i in names:
    print(i)

# dict {} - collection of key-value pairs 

# Here we have our keys on the left seperated with : and seperate them from values with a , comma
houses = {"harry":"Gryffindor","Syltheran":"Draco"}

print(houses["Harry"])

#Functions

def square(x):
    return x*x

for i in range(10):
    print(f"The square of {i} is {square(i)}")

#classes 
#You can think of a class as a template for an object

class Point():
# __init__ is a magic method that is automatically called everytime I create a new point
# object that operate on themselves, with an x & y value storing values within itself 
    def __init__(self, x, y):
        self.x = x
        self.y = y
#    def __init__(self, input1, input2):
#        self.x = input1
#        self.y = input2
p = Point(2,8)
# So were saying to go into the point and print the value within that point
print(p.x)
print(p.y)

class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        #if there arent any more open seats
        if not self.open_seats():
            return False
        # here we store the object into itself
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["harry", "Ron", "hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person)
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No avalible seats for {person}")

# Decorators
# Is a function that take a funtion as input and them modifys that function

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function")
    return wrapper

#This wraps the hello function in announce, runs the function, then prints last message
@announce
def hello():
    print("Hello, world")

hello()

# Go back over lambda
