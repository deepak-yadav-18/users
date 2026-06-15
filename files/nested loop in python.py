"""
Nested loop :- A loop inside the loop.
"""

# outer loop
# for i in range(1,11):
#     # inner loop
#     for j in range(1,6):
#         print(i,end=" ")
#     print()


# Rectangle pattern 
# for i in range(1,11):
#     for j in range(1,21):
#         print("*",end=" ")
#     print()

# ======== Triangle Pattern ==============
"""
*
* *
* * *
* * * *
* * * * *
for i in range(1,16):
    for j in range(i):
        print("*",end=" ")
    print()
"""


"""
=============== decreasing triangle ===============
* * * * *
* * * * 
* * * 
* * 
* 
count=5
for row in range(1,6):
    for col in range(count):
        print("*",end=" ")
    print()
    count=count-1
"""
# n = int(input("Enter Row numbers : "))
# count=n-1
# for row in range(1,n+1):
#     for col1 in range(count):
#         print(" ",end=" ")
#     for col2 in range(row):
#         print("  #",end=" ")
#     print()
#     count-=1 # count=count-1

# =================== Hill pattern =======================
"""
     *
    * *
   * * * 
  * * * *
 * * * * *
 n = int(input("Enter Row numbers : "))
count=n-1
for row in range(1,n+1):
    for col1 in range(count):
        print(" ",end=" ")
    for col2 in range(row):
        print("  #",end=" ")
    print()
    count-=1 # count=count-1
"""
# ================= hollow square pattern ==================
"""

for row in range(1,6):
    for col in range(1,6):
        if((row==1 or row==5) or (col==1 or col==5)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""

# ============ A pattern ==============================
"""
for row in range(1,7):
    for col in range(1,6):
        if((col==1 or col==5) and (row!=1)):
            print("*",end=" ")
        elif(((row==1) and (col>1 and col<5)) or (row==4)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    """


# ======================== B pattern ============================
"""
for row in range(1,8):
    for col in range(1,5):
        if(col==1 or (col==4 and row!=1 and row!=4 and row!=7)):
            print("#",end=" ")
        elif((row==1 or row==4 or row==7) and (col!=4)):
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()

"""

# ==================== X pattern ========================
# count=15
# for row in range(1,16):
#     for col in range(1,16):
#         if(row==col ):
#             print("#",end=" ")
#         elif(col==count):
#             print("#",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     count-=1
#===============K pattern===============================
rows = 9
count = 6

for row in range(1,9+1):
    for col in range(1,6+1):
        if col == 1:
            print("#", end=" ")
        elif (col == count and row<=4):
            print("*", end=" ")
        elif (col == row-3):
            print("$", end=" ")
        else:
            print(" ", end=" ")
    print()
    count-=1