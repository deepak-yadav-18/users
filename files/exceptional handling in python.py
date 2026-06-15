"""
exception (Error) Handling :- Handling errors in python code.
-----------------------------
=> using exceptional handling, we can return a meaningfull message to user.
=> We can run code after the error line.

syntax :-
---------
try:
    write your code...
except(errorName):
    statement
else:
    This statement runs when there is no error in our code.
finally:
    This block is always runs, either there is any error or No error.

Common error names :
--------------------
1. syntaxError
2. zeroDevisionError
3. indexError
4. valueError

"""

try:
    name="Ram"
    l=[1,2,3,34,4,5]
    print(29/9)
    print(name)
    print(l[1])
except(ZeroDivisionError):
    print("Any number can not be divisible by Zero.")
except(NameError):
    print("Name is Not Defined")
except(IndexError):
    print("Out of index Range")
else:
    for i in range(1,11):
        for j in range(i):
            print("*",end=" ")
        print()
    print("Finally there is no more Error....")

finally:
    print("\n------------------------------------------------------")
    print("This is our Finally Block and It runs always...\n")

    print("hello world")