"""
Python is an object oriented and interpreter based programming language.
---------------------------------------------------------------------------
variable :- Variable are container for storing diffferent kinds of data.
-----------
================================ Data Types ===============================
1. In-Built Data types
2. User defined data type => oops(object oriented programming)

=========================== In-built data types ===========================

1. string :- Data stored in single,bouble or triple inverted commas(multi-line string).
2. integer :- a whole number value ex: 21,-3267
3. float :- Used to store fractional value. ex: 29.43674 , -.48349
4. complex :- Add an imaginary value with number. ex: 34+5j
5. boolean :- There is only two values in boolean data type.(True or False)
6. list :-  it stores multiple values with comma seperation inside [](square bracket), ex: user=["Ram",32,"Mathura"]
7. tuple :- it stores multiple values with comma seperation inside ()(square bracket), ex: user=("Ram",32,"Mathura")
8. set :- it stores multiple values with comma seperation inside {}(square bracket), ex: user={"Ram",32,"Mathura"}
9. frozenset: it stores multiple values with comma seperation inside frozenset()(square bracket), ex: user=frozenset(["Ram",32,"Mathura"])
10. dictionary :- it stores multiple values in key-value pair with comma seperation inside {}(square bracket), ex: user4={"Name":"Ram" , "Age":32 , "Address":"Mathura"}
11. range
12. None

NOTE :- type(variableName/value) :- return data type.
"""

a="""
----------------------------------
Name        Age         Address
----------------------------------
Raman       32          Mathura
----------------------------------
Kanha       35          Vrindavan
----------------------------------
"""


age=36
perc=10/2
cmp =35-46j
ans=True
user=["Ram",32,"Mathura"]
user2=("Ram",32,"Mathura")
user3={"Ram",32,"Mathura"}
user4={"Name":"Ram" , "Age":32 , "Address":"Mathura"}
frSet = frozenset([1,2,3,4,5,6])

r = range(1,20)

n = None
 
print(type(n))

# NOTE : id(variableName) is used to get memory location of the variable. In integer form.
# To get in hexadecimal form :- hex(id(variable))
print(hex(id(r)))

