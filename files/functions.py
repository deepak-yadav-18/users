"""
Function :- Function is a block of code, that runs when we call it. 
-----------

================= Types of functions ==================
1.Pre-defined Functions :- Functions that are defined, we do not have to create them, we just call them.
ex: print(),input(),int(),float(),type(),ord(),chr(),bool(),etc...

2.User-defined Functions :- Functions are defined by the user.

syntax :-
---------
============= here we define a function (function definition) =============

def functionName(parameter1,parameter2,...):
    statements

============ function calling ===============

functionName(argument1,argument2,....)  


NOTE :- parameters are optional value but if we assign a parameter,
        then provide a actual value on function calling
parameter :- Named Placeholder.
argument :- Real value in place of parameter.


NOTE :- Through functions we can perform 'modular programming'.
modular programming :- we can create module.
"""

def sayHello(name,age):
    print(f"Hello {name}\nYour Age is {age}")
    print("--------------------------------------\n")

# sayHello("Ram",32)
# sayHello("Shyam",54)
# sayHello("Raman",65)
# sayHello("Suman",35)

def sum(a,b):
    print(f"The sum of {a} and {b} is : {a+b}")
    print(f"The substraction of {a} and {b} is : {a-b}")
    print(f"The multiplication of {a} and {b} is : {a*b}")
    print(f"The division of {a} and {b} is : {a/b}")
    print(f"The remainder of {a} and {b} is : {a%b}")

# sum(10,3)
def calculator(x,y,opr):
    if(opr=="+"):
        print(f"The sum of {x} and {y} is {x+y}")
    elif(opr=="-"):
        print(f"The substraction of {x} and {y} is {x-y}")
    elif(opr=="*"):
        print(f"The Product of {x} and {y} is : {x*y}")
    elif(opr=="/"):
        print(f"The Division of {x} and {y} is : {x/y}")
    elif(opr=="%"):
        print(f"The Remainder of {x} and {y} is : {x%y}")
    else:
        print("Invalid Operator....")


# calculator(10,3,"*")
# calculator(120,3,"/")
# calculator(32,3,"%")

def printA(r,c,smbl):
    for row in range(1,r+1):
        for col in range(1,c+1):
            if(((col==1 or col==c) and row>1) or ((row==1 or row==r//2) and (col>1 and col<c))):
                print(smbl,end=" ")
            else:
                print(" ",end=" ")
        print()
    print()


# printA(8,8,"*")
# printA(10,10,"#")
# printA(15,20,"X")
# printA(25,20,"$")

def fibo(n):
    n1=0
    n2=1
    for i in range(1,n+1):
        print(n1,end="\t")
        n3=n1+n2
        n1=n2
        n2=n3

# fibo(10)
# fibo(15)



def count_digits(num):
    # num=int(input("Enter any number :- "))
    total_digits=0
    while(num>0):
        total_digits+=1
        num=num//10

    print("Total Digits are : ",total_digits)

# count_digits(3221738921321)
# count_digits(9054389278927593247439825743)
"""
num=218
218//10 =>21.8==> 21

num=21
21//10 => 2.1 => 2

num=2
2//10 => .2 => 0

"""

"""
================= break , continue , pass, return ======================
=> break :- To come out from loop body
=> continue :- To skip a part.
=> pass :- To skip a block. TO run a empty block.To hold a part
=> return :- It is used to come out from function body.
             It is mostly used in recursion.
"""

def output(a,b):
    pass


"""
for i in range(1,100+1):
    if(i%5==0):
        # break
        # continue
        pass
    print(i)
"""

# ========== function with default parameter ===========
def sum(a,b=0):
    return a+b

# print(sum(29))

def showDetails(name,age,country="India"):
    return f"The Name is : {name}\nAge is : {age}\nCountry is : {country}"

#print(showDetails("Yogi",16,"Nepal"))
#print(showDetails("Modi",26))

# =================== Anonymous function(lambda) =========================
# Single line function is created by the lambda keyword.
"""
syntax :-
----------
functionName = lambda p1,p2,... : statement 
"""

# def power(n,p):
#     print(n**p)

power = lambda n,p: print(n**p)
# power(10,4)

# power(3,5)

name="Ram singh"











