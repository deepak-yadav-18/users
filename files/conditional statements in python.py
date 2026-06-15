"""
There are three blocks of code that is used to run code , after satisfy a certain condition.

indentation => 1 tab space => 4 spaces  
if(condition1):
    statements
elif(condition2):
    statements
elif(condition3):
    statements
...
else:
    statement
"""


# ======================== voting program =======================
"""
age=int(input("Enter Your Age :- "))
if((age>=18) and (age<=100)):
    print("You can vote")
elif(age>=1 and age<=17):
    print("You can not Vote")
else:
    print("Invalid Age Input!!! ")

"""

# ===================== Grading system ============================
"""
90-100 => A+
80-89 => A
70-79 => B
50-69 => C
33- 49 => D
<33 => Fail
"""

hindi = int(input("Enter Hindi Marks : "))
english = int(input("Enter English Marks : "))
maths = int(input("Enter Maths Marks : "))
science = int(input("Enter science Marks : "))
sst = int(input("Enter sst Marks : "))


total_marks = hindi+english+maths+science+sst

perc = (total_marks/500)*100

print("=======================================")
print("Total Marks : ",total_marks)
print("Percentage is : ",perc)
print("=======================================")
if(perc>=90 and perc<=100):
    print("A+ Grade")
elif(perc>=80 and perc<=89):
    print("A Grade")
elif(perc>=70 and perc<=79):
    print("B Grade")
elif(perc>=50 and perc<=69):
    print("C Grade")
elif(perc>=33 and perc<=49):
    print("D Grade")
elif(perc<33):
    print("Fail")
else:
    print("Invalid Marks input...")

print("=======================================")


