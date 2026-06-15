# 2.Total digits in a number
"""
num=372836
total_digits=0

while(num>0):
    total_digits+=1
    num=num//10

print("Total Digits are :- ",total_digits)
"""

# ========== sum of n natural numbers using recursion
def sumN(n):
    if(n==1):
        return 1
    return n+sumN(n-1)

# print(sumN(10))


# ==================== Armstrong Number =========================

#  1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, and 9474


# 153 => 1**3+5**3+3**3 => 1+125+27 => 153
# 132 => 1**3+3**3+2**3 => 1+27+8 => 36 X
# 1234 => 1**4 + 2**4 + 3**4 + 4**4 => 1+16+81+256 => 344 X

"""
num=1634 #372 , 37 , 3 , 0
power = len(str(num))
temp=num # 372
sum=0 # 0,8,351 , 378
while(num>0):
    last_digit = num%10 #372%10 => 2 , 37%10 => 7 , 3%10 => 3
    sum=sum+last_digit**power # 0+2**3=>8 , 8+7**3=> 351 , 351+3**3 => 378
    num=num//10 # 372//10 => 37 , 37//10 => 3 , 3//10 -> 0


print("Original number is : ",num)
print("Temporary number is : ",temp)
print("Sum is : ",sum)
if(sum==temp):
    print(temp," is a Armstrtong Number")
else:
    print(temp," is not a Armstrtong Number")

# print(336/10)
# print(336//10)

"""
# NOTE : To get last digit of a Number :- num%10
# NOTE : To skip last digit of a Number :- num//10

def armstrong(num):
    temp=num # it holds the copy of the original number
    power = len(str(num))
    sum=0

    while(num>0):
        last_digit = num%10
        sum = sum + last_digit**power
        num = num//10

    if(temp==sum):
        print(temp," is Armstrong")
    

# armstrong(326)
# armstrong(153)
# armstrong(36)
# armstrong(3)
# armstrong(370)
# armstrong(1634)
# armstrong(3262)

# st ="123"
# print(len(st)) => 



for i in range(1,10000+1):
    armstrong(i)









