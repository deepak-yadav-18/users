# class collage:
#     def __init__(self, c_name, c_address, id):
#         self.collage_name = c_name
#         self.collage_address = c_address
#         self.id = id  # instance variable

#     def sport_department(self):
#         print(f"""
#         ============= {self.collage_name} Collage ===============
#         """)
#         print("\t\tWelcome to sport Team")

#     def music_department(self):
#         print(f"""
#         ============= {self.collage_name} Collage ===============
#         """)
#         print("\t\tWelcome to music Group")


# class student(collage):
#     def __init__(self, id, c_name, c_address, collage_id):
#         super().__init__(c_name, c_address, collage_id)  # Call parent constructor
#         self.student_id = id
#         if self.student_id == self.id:
#             self.sport_department()
#         else:
#             print("Invalid Id")


# # Input section
# collage_id = int(input("Enter College Id to register: "))
# student_id = int(input("Enter Student Id: "))

# # Object creation
# s1 = student(student_id, "ABC", "Mathura", collage_id)

#* =======================================================================================================
# class parent:
#     def parent_data(self):
#         print("Parent class")

# class child(parent):
#     def child_data(self):
#         print("Child class")

    
# c1=child()
# c1.child_data()
# c1.parent_data()



"""
Module system in python :
=============================
Module :- It is a file, which contains some properties(variables) and methods(functions).
---------
We can use these methods and properties in another file using 'import' keyword.

syntax :-
==========
import fileName

fileName.propertyName
fileName.functionName()
-----------------------------------------------------------------------------------------------

In python there are two types of modules :-
--------------------------------------------
1. built-in Modules :- we do not have to install them seperately.
2. not built-in modules :- We have to install them before use.

in cmd or vs code terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~
for install a Module(library) :- pip install moduleName
"""

"""
^ >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Numpy (Numerical Python) :- It is used to working with arrays data type in python.
---------------------------
It is created by 'travis oliphant' in 2005

NOTE :- Because numpy is faster than list data type. And provides many functions for mathematical or statical work.
^ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
"""
import numpy as np

# from numpy import *   # for all functions from numpy
# from numpy import array,sum,mean,zeros,identity

arr = np.array([1,2,3,4,5,6,7,8,9,10])

# print(arr.size)

try:
    arr2 = arr.reshape((5,2))
    # print(arr2)
except(ValueError):
    print("Size is not valid")


zero_array = np.zeros((4,10),dtype=int)
# print(zero_array.dtype)
# print(zero_array)

ar1 = np.array([10,20,40])
ar2 = np.array([1,2,4])
# 10*1+20*2+40*4 => 210
add = np.add(ar1,ar2)
dot_product = np.dot(ar1,ar2)
# print(dot_product)

# print(np.sum(ar1)) #70

ar3 = np.array([10,20,30,20,30])
# print(np.unique(ar3)) # [10 20 30]
#* =======================================================================================================
# Simulated temperature data for 7 days (Morning, Afternoon, Evening)
data = np.array([
    [22, 28, 24],
    [21, 30, 25],
    [19, 29, 24],
    [20, 31, 26],
    [18, 28, 22],
    [23, 32, 27],
    [21, 30, 25]
])

average_per_day = data.mean(axis=1)
hottest_day = np.argmax(average_per_day)

# print("Daily Averages:", average_per_day)
# print("Hottest Day (0-indexed):", hottest_day)


# =============================================================================================================

# import pdb

# def calculate_discount(price, discount):
#     pdb.set_trace()  # Debugger starts here
#     discounted_price = price - (price * discount / 100)
#     return discounted_price

# item_price = 200
# discount_percent = 15

# final_price = calculate_discount(item_price, discount_percent)
# print(f"Final Price: {final_price}")
