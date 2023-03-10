#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python class named Point3D defined by x, y, and z. 
#Define a method that returns (x, y ,z). This tells Python to represent this object in the following format: (x, y, z)
#Then create a variable named my_point containing a new instance of Point3D with x=1, y=2, and z=3 and print it.

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def get_coordinates(self):
        return (self.x, self.y, self.z)
# To create an instance of this class with the x, y, and z values of 1, 2, and 3 respectively, we can write:
my_point = Point3D(1, 2, 3)
#And to print the point's coordinates, we can call the get_coordinates() method on my_point:
print(my_point.get_coordinates())


# In[2]:


#Write a Python class named Rectangle constructed by a length and width. 
#Define two methods, area and perimeter, which will compute the area and the perimeter of the rectangle.
#Then create a variable named my_rectangle containing a new instance of Rectangle with width=3 and length = 4 and 
#compute both area and perimeter ( the area is expected to be 3*4=12 and perimeter 2*(3+4)=14).


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
#To create an instance of this class with length=4 and width=3, we can write:
my_rectangle = Rectangle(length=4, width=3)

#To compute the area and perimeter of this rectangle, we can call the area() and perimeter() methods on my_rectangle:
print("Area: ", my_rectangle.area())
print("Perimeter: ", my_rectangle.perimeter())


# In[4]:


#Write a Python  class named Circle constructed by its center O and radius r.
#Define two methods, area and perimeter, which will compute the area and the perimeter of the circle, 
#class Circle:
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
    def isInside(self, point):
        x, y = point
        cx, cy = self.center
        if (x - cx) ** 2 + (y - cy) ** 2 <= self.radius ** 2:
            return True
        else:
            return False

#and is Inside() method which allows you to test whether a point A(x, y) belongs to the circle C(O, r) or not.

#The Circle class takes two arguments, center and radius, in its constructor. The area() method calculates the area of the circle using the formula πr^2, 
#and the perimeter() method calculates the perimeter of the circle using the formula 2πr.
#The isInside() method takes a point (as a tuple of x and y coordinates) and returns True if the point is inside the circle or False if it is not.
#To create an instance of this class with center=(0, 0) and radius=5, we can write:
my_circle = Circle(center=(0, 0), radius=5)

#To compute the area and perimeter of this circle, we can call the area() and perimeter() methods on my_circle:
print("Area: ", my_circle.area())
print("Perimeter: ", my_circle.perimeter())

#To check if a point A(x, y) is inside the circle C(O, r) or not, we can call the isInside() method on my_circle and pass in the point as a tuple:
print(my_circle.isInside((3, 4)))  # Output: True
print(my_circle.isInside((5, 5)))  # Output: False







# In[5]:


#Suppose we want to model a bank account with support for deposit and withdraw operations. 
#Let’s create a Python class named Bank defined by its balance. 
#Define two methods, deposit and withdraw, to compute the new amount of each operation.

class Bank:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return self.balance

#The Bank class takes an argument, balance, in its constructor to set the initial balance of the account.
#The deposit() method takes an amount to be deposited and adds it to the current balance, returning the new balance. 
#The withdraw() method takes an amount to be withdrawn and subtracts it from the current balance, returning the new balance.
#If the requested withdrawal amount is greater than the current balance, it returns a string "Insufficient funds".

#To create an instance of this class with an initial balance of 1000, we can write:
my_bank = Bank(balance=1000)

#To make a deposit of 500 into the account, we can call the deposit() method on my_bank:

print("New balance after deposit: ", my_bank.deposit(500))
#To make a withdrawal of 1200 from the account, we can call the withdraw() method on my_bank:

print("New balance after withdrawal: ", my_bank.withdraw(1200))
#If we try to withdraw an amount greater than the current balance, 
#the withdraw() method returns the string "Insufficient funds"

print(my_bank.withdraw(5000))  # Output: "Insufficient funds"


# In[ ]:




