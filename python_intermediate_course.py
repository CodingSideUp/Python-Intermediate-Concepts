#lists: [] ordered, mutable, allows duplicates
mylist = ["ban", "cherry", "apple"]
print(mylist)

#
mylist2 = [5, True, "apple", "apple"]
print(mylist2)

#indexing
item = mylist[0]
print(item)

#reverse indexing
print(mylist[-2])

#
if "banana" in mylist:
    print("Yes")
else:
    print("No")

#length
print(len(mylist))

#appending
mylist.append("lemon")
print(mylist) #appends at last index of row

#appending at a certain position
mylist.insert(1, "blueberry")
print(mylist)

#to remove
item = mylist.pop() #removes last lement of the list
print(mylist)

#remove a specific element
#item = mylist.remove("name_of_element")

#can remove contents of a list with .clear() fn
#item = mylist.clear()

#can reverse the list
#item = mylist.reverse()

#sorting
#sorts in descending
mylist = [3, 4, 7, 1, 2]
item = mylist.sort()
print(mylist)

#creating a new list and sorting another list to it
newlist = sorted(mylist)
print(mylist)
print(newlist)

#new list with five zeros
mylist = [0] * 5
print(mylist)

#can add 2 lists
new_list = mylist + mylist2
print(new_list)

#slicing
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]
print(a)

#no start index
a = mylist[:5]
print(a)

#no stop index
a = mylist[1:]
print(a)

#step index
#syntax:[start index:stop index:step index ]
a = mylist[::1]
print(a)    

#reverse list
a = mylist[::-1]
print(a)

#copying
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org
print(list_cpy)
print(list_org)

#if u modify the copy, this also modifies the original list
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org
list_cpy.append("lemon")
print(list_org)
print(list_cpy)

#try debugging this code
#mylist = [1,2,3,4,5,6]
#b = [i*i for i in my list]
#print(mylist)
#print(b)

#Tuples(): ordered, immutable, dups allowed
#can be defined without () as well

mytuple = ("Max", 28, "Boston")
print(mytuple)

#using built in tuple fn
mytuple = tuple(["Max", 28,"Boston"])
print(mytuple)

#indexing
item = mytuple[2]
print(item)
#try negative indexing with the same

#if u try changing elements, you get an error as it's immutable
#mytuple[0] = "Tim"

#iteration
for i in mytuple:
    print(i)

#can check for len of a tuple with:
#print(len(tuple_name))
    
#count no of elements in tuple
my_tuple = ('a', 'p', 'p', 'l', 'e')   
print(my_tuple.count('p'))

#index of an element
print(my_tuple.index('p'))

#convert tuple to a list
my_list = list(my_tuple)
print(my_list)
#converting it back into a tuple
my_tuple2 = tuple(my_list)
print(my_tuple2)

#slicing
#note that it doesn't print out the last index
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b)
#all the slicing we did in lists is valid for tuples as well

#unpacking
#the no of elements defined inside the tuple must be equal to the no of objects we define
my_tuple = "max", 28, "Boston"
name, age, city = my_tuple
print(name)
print(age)
print(city)

#unpacking in a different way
#converted into a list

my_tuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple
print(i1)
print(i2)
print(i3) 

#tuples occupy lesser space as compared to the lists
#so whenever u r working with large data, it might be beneficial to work with tuples
#ideally the o/p should show a different size but here it shows the same, you can debug this later

import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = [0, 1, 2, "hello", True]
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

#dictionary{}
#key:value, unordered, mutable
#querying in dict for values of keys must be done in [] ie., the key must be inside the []
#within ""

mydict = {"name": "Max", "age":28, "city":"new york"}

#using dict{} fn to create a dictionary
mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

#to print a particulare value of a key:
#this will give you the age 
value = mydict["age"]
print(value)

#to add a new key:value pair at the end
mydict["email"] = "max@xyz.com"
print(mydict)

#delete items

del mydict["name"]
print(mydict)

#can use mydict.pop("age")
#can use mydict.popitem(): This removes the last item

#to check for a particular element is there in the dict
mydict = {"name": "Max", "age":28, "city":"new york"}
if "name" in  mydict:
    print(mydict["name"])

#using try/ecept statement
    
try:
    print(mydict["name"])
except:
    print("error")

#looping
for key in mydict:
    print(key)

#for only the keys
for key in mydict.keys():
    print(key)

#for only the values
for value in mydict.values():
    print(value)

#if in case you want both keys and values, then
for key, value in mydict.items():
    print(key, value)

#copy a dictionary 
mydict_cpy = mydict
print(mydict_cpy)
#if you modify the copy, then it modifies the original one as well
#you can use mydict_cpy = mydict.copy() fn as well
#can also use dict function as: mydict_cpy = dict(mydict)

#updating one list with a new one
my_dict = {"name":"Max", "age": 28, "email":"max@xyz.com"}
print(my_dict)
my_dict_2 = dict(name="Mary", age=27, city="Boston")
my_dict.update(my_dict_2)
print(my_dict)

#sets: unordered, mutable, no duplicates {}, but no key:value pairs inside curly braces
#it doesn't allow duplicates
myset = {1, 2, 3, 1, 2}
print(myset)

#set can also be defined using the set() func
myset = set([12, 34])
print(myset)

#another method
myset = set("Hello") #u can see only one 'l' in the o/p
print(myset)

#can add into set with add() funct
#and also remove with remove() func'n

myset = {1, 2, 3, 4, 5}
myset.add(4)
myset.remove(3)

#discard method
#myset.discard(3)

#clear method to clear the set
#myset.clear()

#remove any numbver from the set arbitrarily
#print(myset.pop())

#iteration is the same

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

#union is being done, it will be done without duplication

u = odds.union(evens)
print(u)

#intersection

i = odds.intersection(primes)
print(i)

#difference of 2 sets
setA = {1, 2, 3, 4, 5,6, 7,8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)

#symmetric difference method

sym_diff = setA.symmetric_difference(setA)
print(diff)

#updating the sets
setA.update(setB)
print(setA)

#
print(setA.issubset(setB))

#superset
setC = (setA.issuperset(setB))

#frozenset
#cant be changed/modified after creation

a = frozenset([1, 2, 3, 4])
print(a)

#strings: ordered, immutable, text rep
#"" or ''

my_string = 'Hello world'
print(my_string)

#if there's a single quote inside the single quote, it will give an error
#so you can use a backslash
#or a single quote inside a double quote

my_string = 'I\'m a programmer'
print(my_string)

#triple quotes for multi line strings and documentation

my_string = """ Hello \
world"""
print(my_string)

#indexing
print(my_string[1])


#slicing
substring = my_string[1:5]
print(substring)

#concatenation of strings
name = "Tom"
sentence = name + "" + my_string
print(sentence)

#iterate
for i in sentence:
    print(i)

#useful methods
#observe white space before and after and how it will be removed
    
my_string="   Hello World   "
print(my_string) #observe o/p here
my_string = my_string.strip()
print(my_string) #observe o/p here

#splitting
print(my_string.split())

#formatting string
#this method is called a placeholder

var = "Tom"
my_string = "the variable is %s" %var
print(my_string)

#if in case there's a number then use %d as it stands for decimal and 
# %s means strings
# %f is for float values

#using the format function
var = 3.1412
my_string = "the variable is {}".format(var)
print(my_string)

#if you want only a specific # of digits then use {:.2f}
#if there is two variable and in one of then you only want to include a particular
#number of digits

var2 = 4.856
my_string = "the variable is {:.2f} and {}".format(var, var2)
print(my_string)

#using f-strings
#this is the latest and better method in python
#only after python 3.6

my_string = f"the variables are {var} and {var2}"
print(my_string)

#can also customise with a mathematical op
my_string = f"the variables are {2*var} and {var2}"
print(my_string)

#collections: Counter, namedtuple, OrderedDict, defaultdict, deque

#Counter stores elements as dictionary keys and counts as dict values
#just counts objects in string

from collections import Counter
a = "aaabbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))
print(my_counter.most_common(1)[0])
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))

#namedtuple
#easy to create a lightweight tuple
#similar to a struct

from collections import namedtuple
Point = namedtuple('Point', 'x,y') #it will create a class called Point with the fields x and y
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

#OrderedDict
#it removes order im whioch items where created

from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1  #if you interchange the order in which you created the elements when you print it, it will print it in the same order in ehich they were crreated
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)  

# d = defaultdict(int)
# d['a'] = 1
# d['b'] = 2
# print(d['a'])

#deque
#it is a double ended queue
#can add or remove element from both the ends

from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d)

d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()

d.extend([4, 5, 6]) #you can do d.extendleft also
print(d)

d.clear()
print(d)

d.append(1)
d.append(2)
d.append(3)
d.append(4)
print(d)

d.rotate(1) #rotate right
print(d)

d.rotate(-1)
print(d)

#itertools
#datatypes which can be used in a for loop
#product, permutations, combinations, accumulate, groupby and infinite iterators

from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))

c = [4, 5]
d = [6]
prod = product(c, d, repeat = 2)
print(list(prod))

#permutations is as name suggests
from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

perm = permutations(a, 2) #checking for permutations with length 2, optional to use length
print(list(perm))

#combinations
from itertools import combinations
a = [1, 2, 3, 4]
comb = combinations(a, 2) #length is mandatory
print(list(comb))

#combinations with replacement

from itertools import combinations_with_replacement
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

#accumulate
#basically one elemtn from list is added to next element in list hence it is an acumulative function
from itertools import accumulate
a = [1, 2, 3, 4]
acc = accumulate(a)
print(list(acc))

#instead of adding, we can multiply in the 
from itertools import accumulate
import operator
acc_mul = accumulate(a, func=operator.mul)
print(list(acc_mul))
a = [1, 2, 5, 3, 4]
acc_max = accumulate(a, func=max)
print(list(acc_max))

#groupby func is an iterator 

from itertools import groupby

def greater_than_3(i):
    return i > 3

a = [1, 2, 3, 4, 5]
obj_groupby = groupby(a, key = greater_than_3)
for key, value in obj_groupby:
    print(key, list(value))

#doing the same aboveexample with lambda function
    
def lesser_than_3(x):
    return x < 3

grpby_lesser = groupby(a, key=lambda x: x<3)  #the syntax for lambda fn: lambda arguments:expression
for key,value in grpby_lesser:
    print(key, list(value))

#another example for a dictionary
    
persons = [{'name':'Guru', 'age':30}, {'name':'Rekha', 'age':28},
           {'name':'Rakshith', 'age':45}, {'name': 'Nagaraju', 'age':45}]

obj_groupby = groupby(persons, key=lambda x:x['age'])
for key, value in obj_groupby:
    print(key, list(value))

#count,cycle and repeat functions

# from itertools import count, cycle, repeat
# a = [1, 2, 3]
# for i in count(10):  #10 is the starting point so it ideally keeps counting ultil infinity
#     print(i)
#     if i == 15:
#         break

# #cycle
# a = [1, 2, 3]
# for i in cycle(a):
#     if i == 6:
#         break
# print(i)

# #repeat
# for i in repeat(1):
#     if i == 7:
#         break

# for i in repeat(1, 4):
#     print(i)

#lambda
#syntax: lambda args:expression
    
adding_10 = lambda x: x + 10
print(adding_10(6))
    










