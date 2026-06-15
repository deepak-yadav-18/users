import functions
"""
================================ Loop =================================
Loop is used to run a block of code number of times.

1. for loop :- When terminating(ending) condition is known.
2. while loop :- when terminating condition is unKnown.


==================== FOR loop in python ===============================
syntax :-
---------
python follow indentation(1tab space = 4 spaces) for defing a block(if-else,loop,functions)

for variableName in range(start,end-1,step-1): 
    statements...
"""

# for i in range(1,10+1):
#     print(i)
#     print("hello world")
#     print("--------------")
#     print("I line in Mathura")


# for i in range(1,11,3):
#     print(i)


"""
1. print 1-10 numbers 
2. print 1-100 all even numbers
3. print 1-100 all odd numbers
4. print a multiplication table of user defined number.
5. sum of n natural numbers
6. find factorial of a number
7. find the sum of all even and odd numbers in user defined range.
8. print fibonnachi series of upto n number of terms.
"""

# for i in range(1,101):
#     if(i%2!=0):
#         print(i)

"""
5*1 => 5
5*2 => 10
5*3 => 15
5*4 => 20
....
"""

# num = int(input("Enter table number : "))
# for i in range(1,11):
#     print(num*i)

# ===================== sum of n natural numbers =========================
# 1-10 => 1+2+3+4+5+6+7+8+9+10 => 55
"""
start=int(input("Enter Start number : "))
end=int(input("Enter End number : "))
sum=0 # 1,3,6,10,15,21,28,36,45,55
for i in range(start,end+1):
    sum=sum+i # 0+1=>1 , 1+2=>3 , 3+3=>6 , 6+4=>10 , 10+5=>15 , 15+6=>21 , 21+7=>28, 28+8=>36, 36+9 => 45 , 45+10 => 55
    # sum+=i
    # print("i is ",i," and sum is ",sum)
    print(f"i is {i} and sum is {sum}") # this is format string. 

"""


# ========================= swaping two numbers using third or without third variable ====================
# a=10
# b=20
# # c=a

# # a=b
# # b=c
# a,b=b,a
# print("A : ",a)
# print("B : ",b)
# ========================= Fibonnachi series ==============================
# 0,1 , 1,2,3,5,8,13,21,34,55,89,144,...................
# NOTE : there are two fixed numbers 0 and 1 , The new number will be the sum of previous two numbers.


"""
n1=0 #1,1,2,3,5,8,13,21,34,55
n2=1 #1,2,3,5,8,13,21,34,55,89
for i in range(1,11):
    print(n1 ,end="\t") # 0,1,1,2,3,5,8,13,21,34
    n3=n1+n2  # 0+1=>1 , 1+1=>2 ,1+2=>3 ,2+3=>5, 3+5=>8, 5+8=>13, 8+13=>21, 13+21=>34, 21+34=>55, 34+55=>89

    n1=n2 # 1,1,2,3,5,8,13,21,34,55
    n2=n3 # 1,2,3,5,8,13,21,34,55,89

"""


# a=10
# b=20

# print(a,end="\n")
# print(b)

"""
escape sequence characters : Some characters are not valid in a statement,To make them valid we use escape seq. characters.
----------------------------  
syntax :- \character

\n => new line 
\t => tab space
\" => "
\' => '
\b => backspace character
\r => carriage return => beginning of the line.

NOTE :- These are writtern inside the string.
"""

msg="I \blive in \"Mathura\"."
# print(msg)

# functions.printA(10,10,"@")
# functions.calculator(10,39,"*")
