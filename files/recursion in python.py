"""
recursion :- When a function calls itself inside the function body, called as recursion.

NOTE :- it calls itself, until base condition is not satisfied.
"""

# ============ printing 1-10 numbers using recursion ============= 
def count(n):
    # base condition
    if(n==10):
        return 10
    print(n)
    return count(n+1)

# print(count(1))

# for i in range(10,0,-1):
#     print(i)

# ============== printing 10-1 using recursion ===================

def rev_count(n):
    if(n==0):
        return 0
    print(n)
    return rev_count(n-1)

#rev_count(10)

# ================= sum of n natural natural numbers ===============
# 1-10 :- 1+2+3+4+5...+10 => 55

for i in range(1,10):
    def sumN(i):
        if(i==1):
            return 1
        return i+sumN(i-1) # => i=1 , 1+sum(i-1) => 1+0 => 1 , 2+sum(2-1) => 3 , 3+sum(3-1) => 5 , 5+5-1=> 9 , 9+6-1 => 14 , 14+6=> 20 , 20+7 => 27 , 27+8 => 35 , 35+9 => 44 , 44+10 => 55
    print(i," = ", sumN(i))
# print(sumN(12))

def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)
"""
factorial(5)

return 5*factorial(5-1) => 5*4 => 20
return 20*factorial(4-1) => 20*3 => 60
return 60*factorial(3-1) => 60*2 => 120
return 120*factorial(2-1) => 120*1 => 120
return 120*factorial(1-1) => 120*0 => 120*1 => 120

"""
# print(factorial(5))

# =================== fibonnachi series ====================
# 0 1 1 2 3 5 8 13 21 34 ,....

def fibo(n):
    if(n==1):
        return 0
    if(n==2):    
        return 1
    return fibo(n-1)+fibo(n-2)

# for i in range(1,11):
#     print(fibo(i),end="\t")

# 2**3 => 2*2*2
def power(n,p):
    if(p==0):
        return 1
    return n*power(n,p-1)

# print(power(2,4))


def check_Alpha(ch):
    # ch=input("Enter any character : ")
    if(ch>="A" and ch<="Z"):
        print(f"{ch} is a Upper Case Alphabet")
    elif(ch>="a" and ch<="z"):
        print(f"{ch} is a Lower Case Alphabet")
    elif(ch>="0" and ch<="9"):
        print(f"{ch} is a Number")
    else:
        print(f"{ch} is a special symbol.")
         
# check_Alpha("FGHFHG")
# check_Alpha("cdshjkchsd")
# check_Alpha("38479242")
# check_Alpha("#$")

