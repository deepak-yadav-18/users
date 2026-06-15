"""
Operators are some special symbols used for specific task.
---------------------------------------------------------------------------
1. Arithematic Operators :- + , - , * , / , %(Modulas[find remainder]) , **(exponential) , // (floor division)

2. Assignment Operators :- = , += , -= , *= , /= , %= , **= , //=

3. Relational or Comparision operators :- > , < , ==(isEqual to) , >=(greater than or equal to) , <= , != (not equal to)

NOTE : These operators are used to 'compare two values' and return boolean value(True/False).And create a condition

4. Logical Operators :- and(logical and) , or (logical or) , not (logical not)

NOTE :- These operators are used to 'compare two conditions' and return boolean value(True/False).

syntax :- (condition1)logicalOpearator(condition2)

and :- return True if both conditions are true, it return false if either one condition is false.
or  :- return True if either one condition is true, it return false if both condition are false.
not :- It reverse the conditions.(True--->False , False--->True)

5. Bitwise Operators :- &(biwise and) , |(bitwise or) , ^(bitwise XOR) , >>(bitwise right shift) , << (bitwise left shift)

NOTE :- These are used to perform bitwise operation between two bits.

6. ternary operator :-(true statement) if(condition) else (false statement)
It works as single line if-else statement
"""

"""
x=83
y=3
print(x%y) # 2

print(2**3) # 8

print(35//4) # 8 (Remove floating points.)
"""


# =============== celcius to fehrenhite ===================
"""
F = (C * 9/5) + 32. 
"""
# temp=int(input("Enter Tempreture in Celcius :- "))

# f_to_c = (temp*9/5)+32

# print("Tempreture in Celcius : ",temp)
# print("Tempreture in Fehrenhite : ",f_to_c)

# ================== area of circle =======================
"""
area = 3.14*r**2
"""
# r = int(input("Enter Radius : "))
# area = 3.14*r**2
# print("Area of circle is : ",area)


# =====================================================================
a=19
b=2
sm=a+b
sb=a-b
ml=a*b
dv=a/b
md=a%b
exp=a**b
flr=a//b

"""
print("Sum is : ",sm)
print("Sub is : ",sb)
print("multiplication is : ",ml)
print("division is : ",dv)
print("Modulas is : ",md)
print("exponential is : ",exp)
print("floor division is : ",flr)

"""

# x=20
# # x=x+10
# x+=10 # x= x+10
# # print(x)

# y=4
# y**=2 # y = y**2 => y= 4**2 => y=16
# print(y)



"""
======================== Relational operators =============================
n1=20
n2=20

print(n1>n2) # => False
print(n1<n2) # => False
print(n1>=n2) # => True
print(n1<=n2) # => True
print(n1==n2) # => True
print(n1!=n2) # => False
"""



n1=10
n2=20
n3=30

# output = (n1<n2)and(n1<n3) => True
# output = (n1>n2)or(n1>n3) => False
# output = not(n1>n2)  => True

# print("Output is : ",output)



# print(46&135)
# print(46|135)
# print(46^135)
# print(46>>2)
# print(~46)
# print(46<<2)
# print(bin(46))
# print(bin(135))



# ====================== voting eligibility =======================
# age=int(input("Enter your age :- "))
# output = "You can Vote" if(age>=18) else "You can not Vote"
# print(output)

# =================== even or odd =================================
# num = int(input("Enter number :- "))
# check = "Even Number" if(num%2==0) else "Odd number"
# print(check)

# ============================== membership operator===================================

"""
st = "I live in Vrindavan ( Mathura )"
print("Vrindavan" in st)
print("Mathura" not in st)

"""

a=10
b=10
print(type(a))
print(a is b)
