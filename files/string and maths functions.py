"""
String :- String is a set of characters inclosed in single,double or triple inverted commas.
---------

NOTE :- In string every character have an index value.Which starts withs 0 and last character at index -1.

=> String is Immutable(not changable).

syntax to get indexed character :-
----------------------------------
stringName[IndexNo.]

to get a part of string :-
-----------------------------
stringName[startIndex : endIndex+1 : step+1]
"""

st = "hello world"

# print(type(st))
# print(st[-2])
# print(st[::-1]) => dlrow olleh => It reverse the string.
# print(st[3:]) => lo world
# print(st[:7]) => hello w
# print(st[::]) => hello world



# ================ String Palindrome ===============
# naman => naman 

# s = "malayalam"

# if(s==s[::-1]):
#     print("string is palindrome")
# else:
#     print("Not Palindrome")

"""
============================== String Methods =============================
=> len(stringName) :- Return the length of the string.
=> 
=> 
"""
st2="My name is Ram"

# print(len(st2)) => 15
# print(st2.upper()) => MY NAME IS RAM.
# print(st2.lower()) => my name is ram.
# print(st2.casefold())
# print(st.index("n"))

# print(st2.capitalize()) => My name is ram. 

# print(st2.startswith("My"))
# print(st2.endswith("."))

st3=st2.replace("Ram","Shyam")
# print(st3)

# print(st2.isdigit())
# print("hello world".isalpha())
# print(st2.isspace())

# =============== string formatting =================
# message+variable
# .format(variableName1,variableName2,...)
name="Ram"
age=21
address="Vrindavan"

details = "The Name of user is {0} , Age of user is {1} And address is {2}".format(name,age,address)
# print(details)

# =====================================================

# => .split() :- convert string into list Data type.
# NOTE : default split value is space.

l = st2.split()
# print(type(l))
# print(l) => ['My', 'name', 'is', 'Ram']

# ============================== maths functions ================================
"""
To add some extra functionality in our code, We have to use some libraries.

There are two types of libraries :-
------------------------------------
1. Built-in Libraries :- No Need to install.
=> math,date,time,etc..

2. Not Built-in Libraries :- We have to install them to use.
=> pyqt5,pandas,numpy,qr,etc...
NOTE :- To install any library in python => in cmd or vsCode Terminal => "pip install libraryName"

syntax to access library :-
----------------------------
import libraryName

libraryName.functionName()
"""
import math
# import math as m
# from math import *
# from math import pow,sqrt,factorial


# print(math.pow(2,3))
# print(math.factorial(15))
# print(math.sqrt(81))
# print(math.cbrt(81))
# print(math.ceil(81.1))
# print(math.floor(81.271781))
# print(math.degrees(1))
# print(math.gcd(27,48))
# print(math.radians(360))
# print(math.remainder(21,6))





a="hello"
b="world"
# + => string concatination
# * => string repeatetion
# print(a*4)

def test(x=[]):
    x.append(1)
    print(x)

# test()
# test()

# any() :- return True any value is present in list or tuple,set or dictionary 

# print(any(()))





