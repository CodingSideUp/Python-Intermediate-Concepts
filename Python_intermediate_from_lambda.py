#lambda
#syntax: lambda argument:function
#the lambda fns are used typically when you need to run expressions only once in the code

add_10 = lambda x: x+10
print(add_10(6))

#expressing the above lambda stmt in the form of a regular func

def add_10(x):
    return x + 10
print(add_10(4))

#lambda fn for 2 args

multn = lambda x,y: x*y
print(multn(4, 5))

#ideally sometimes the lambda fns are used with sorted, map and filter fns
#sorted

points2D = [(1,2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D) #sorts in ascending order of x axis coordinates
print(points2D)
print(points2D_sorted) 

#representing the same code by giving another condition
points2D = [(1,2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key= lambda x:x[1]) #sorts in ascending order of y axis coordinates
print(points2D)
print(points2D_sorted)

#representing the above code in terms of a different code using fn

points2D = [(1,2), (15, 1), (5, -1), (10, 4)]

def sort_by_y(x):
    return x[1]

points2D_sorted = sorted(points2D, key=sort_by_y)
print(points2D)
print(points2D_sorted)  #if you see o/p then you can understand that the fn is written if you have the possibilty of 
#executiong the same thing later in the code.
#if in case you would do it only once, then you will use lambda

#same code giving a different expresion

points2D = [(1,2), (15, 1), (5, -1), (10, 4)]

points2D_sorted = sorted(points2D, key= lambda x: x[0] + x[1])
print(points2D_sorted)

#doing above one using function

points2D = [(1,2), (15, 1), (5, -1), (10, 4)]

def add_points2D(x):
    return x[0] + x[1]

sortd_add_points2D = sorted(points2D, key= add_points2D)
print(sortd_add_points2D) 

#map fn transforms each element with a function
#syntax: map(func, sequence/list/iterable)

a = [1, 2, 3, 4, 5]
b = map(lambda i: i*2, a)
print(list(b))

#list comprehension is similar to the map function
#below code will give you the same output using list comprehension

c = [x * 2 for x in a]
print(list(c))

#filter fn
#syntax: filter(funct, iterable/object on which the op/func should work)
#this literally filters a list based on an expression

z = [0,1,2,3,4,5,6]
y = filter(lambda x: x%2 == 0, z)
print(list(y))

#executing the above with list comprehension

s = [x %2 == 0 for x in z]
print(list(s))  #if u see, o/p is in logical nature, not sure why

#modifying the expression for the actual list
s = [x for x in z if x % 2 == 0]
print(list(s))

#reduce(func, seq)
#repeatedly applies fn to the seq and gives u one single o/p

from functools import reduce
a = [1, 2, 3, 4]
prod_a = reduce(lambda x,y: x*y, a)
print(prod_a)

#errors and exceptions

#raising an exception

# x = -5

# if x < 0:
#     raise Exception("x should be positive")

#if the same code is written with x = 5 then no exception will be raised

#catching errors with try and except block
 #this will give u a zero division error

try:
    a = 5/0
except:
    print("you have a zero division error")

#if u wanna know the type of error to be printed w/o interrupting the flow of the program
    
try:
    a = 5/0
except Exception as e:
    print(e)

#another example
#here we're just trying to get the name of the error w/o interrupting the execution of the program
#the program will continue getting executed 
    
try:
    b = 5 + '10'  #we're tryna add an in with a string, this is unsupported op type error
except Exception as e:
    print(e)

#tryna execute more than two try and except
    
try:
    a = 5/0
    b = 5 + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

#same code with syntax correct hence no errors will be printed so we will use else stmt

try:
    a = 5/1
    b = 5 + 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Alles gut")

#logging
    
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    datefmt='%m/%d/%Y %H:%M:%S')
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

#logging from another file named main_logger
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    datefmt='%m/%d/%Y %H:%M:%S')
import Python_intermediate_from_lambda

#json
#serialisation
#encoding

import json
person = {"name": "Gurudarshan", "age":30, "city":"New york", "hasChildren":False, "titles":["programmer", "engineer",]}
personJSON = json.dumps(person)
print(personJSON)

#setting indent
#just a method of formatting and making the data look more better

personJSON = json.dumps(person, indent=4)
print(personJSON)

personJSON = json.dumps(person, indent=4, separators=('; ', '= ')) #semicolon and space will be printed after end of each line while '= ' is after each variable such as name, age etc
print(personJSON)

personJSON = json.dumps(person, indent=4, sort_keys=True) #sortkeys= makes the keys arrange in alphabetical order
print(personJSON)

#covert it into a file
#observe a new file gets created with the name 'person.json' and the person dict is writen there

with open('person.json', 'w') as file:  #opening file in write mode
    json.dump(person, file)   #.dump is used here instead of .dumps which is for a string

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)  #the data would be reflecting in 4 different lines in the file


#converting json data to python object
#deserialization or decoding
    #the data looks like dict and key:value pairs now

person = json.loads(personJSON)
print(person)

#convert from json file using load function instead of convert from json string using loads funcvtion

with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)

#if you write this code you will get an erro, try to understand the code
#this part will give you an error
#in order to understand why, consider the next code snippet
#TypeError: Object of type User is not JSON serializable
    
# import json

# class User:

#     def __init__(self, name, age):

#         self.name = name
#         self.age = age

# user = User('Max', 27)

# userJSON = json.dumps(user)

#writing a custom encoding function
    
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

#using an encoding function

def encode_user(o):
    if isinstance(o, User):
        return {'name':o.name, 'age':o.age, o.__class__.__name__:True}  #observe the o/p to understand
    else:
        TypeError('Object of type User is not JSON serializable')

userJSON = json.dumps(user, default = encode_user)
print(userJSON)

#random numbers

#importing random numbers in the range of 0 to 1

import random

rand = random.random()
print(a)

b = random.uniform(1, 10)
print(b)

c = random.randint(1, 7)
print(c)

d = random.randrange(1, 8) #it will never print 8
print(d)

#statistics

f = random.normalvariate(0, 1) #syntax: normalvariate(mu, sigma)
print(f)

mylist = list("ABCDEFGH")
print(mylist)

x = random.choice(mylist)  #prints randomly by picking a string from a to h
print(x)

a = random.sample(mylist, 3)  #randomly picks 3 strings from the list
print(a)

#alternately
b = random.sample(mylist, k = 3)
print(b)

random.shuffle(mylist)
print(mylist)

#seed function
random.seed(1)
print(random.random()) #prints randomly between 1 to 10
print(random.randint(1, 10))

#secret module
#passwords, security related, authentication etc

import secrets
a = secrets.randbelow(10)
print(a)
b = secrets.randbits(3) #this generates decimal equivalent of binary from 0 to 8 as 2^n = 8
print(b)

#
import numpy as np
a = np.random.rand(3) #generates randomly 3 numbers
print(a)

b = np.random.rand(3, 3)
print(b)

#array with single dimension
a = np.random.randint(0, 10, 3)
print(a)

#array with multiple dimensions
c = np.random.randint(0, 9, (3, 4)) #3x4 array
print(c)

#creating a custome array manually and shuffling them using the shuffle fn

d = np.random.randint(1, 5, (3,3))
np.random.shuffle(d)
print(d)

#decorators
#what r function and class decorators?
#func dec:
#functions can be defined seperately, as part of another function and even returned as part of another function
#a decorator is a function which takes another decorator as an argument and extends it's functionality without explicitly modifying it

def start_end_decorator(func):
    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper

@start_end_decorator
def print_name():
    print('Guru')

#initially exec this stmt and then comment out this stmt and execute @startendwrapper
#print_name = start_end_decorator(print_name) 

print_name()

#for the same code above, if you give arguments to the func in the @startdecorator, u will get an error
#in order to solve this issues, u need to uniformly declare arguments right from the start

def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@start_end_decorator

def add5(x):
    return x + 5

result = add5(10)
print(result)

#printing what the name of the module is in the end

print(add5.__name__) 
#as we can see the name of the function is being shown as 'wrapper'
#this is not right as the correct name of our function is 'add5'
#in order to solve this, we will use functool.wraps() function from functools library
#we will also define another decorator

import functools
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@my_decorator 
def add5(x):
    return x + 5
result = add5(10)
print(result)
print(add5.__name__) 
#it will now show that the func add5 is a func by name add5



























