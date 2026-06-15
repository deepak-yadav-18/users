# count frequency of characters in a string.
"""
st :- hello world
{'h':1 , 'e':1 ,'l':3 ,'o':2 ,'w':1 ,'r':1 ,'d':1 , ' ':1}
"""
# d={10:20 , 30:50}
# d[40]=60
# print(d) => {10: 20, 30: 50, 40: 60}

"""
st=input("Enter Any string : ")
frequency={}

for i in st:
    if(i  in frequency):
        frequency[i]+=1 # frequency["h"]=1
    else:
        frequency[i]=1

print(frequency)
for i in frequency:
    print(i," : ",frequency[i])

"""

# merge two dictionaries

d1={1:10,2:20,3:30,10:10,5:12}

# d2={"one":1,"two":2}
# d3=d1|d2
# d1.update(d2)
# print(d3)

# find maximum and minimum key and value pairs in the dictionary
# ------------------------------------------------------------------

"""
v=d1.values() # list of all values 
max=max(v) # get maximum value
min=min(v) # get maximum value

for key in d1:
    if(d1[key]==max):
        print(key,":",d1[key])
    if(d1[key]==min):
        print(key,":",d1[key])
"""

# ================== Student Grade Book System ===================
students=[]

ans='y'
while(ans=="y"):
    name=input("Enter Student Name : ")
    age=input("Enter Student Age : ")
    print()
    hindi=int(input("Enter hindi marks : "))
    english=int(input("Enter english marks : "))
    maths=int(input("Enter maths marks : "))
    science=int(input("Enter science marks : "))
    computer=int(input("Enter computer marks : "))
    print()

    total_marks = hindi+english+maths+science+computer
    percentage = (total_marks/500)*100

    std = {"Name":name , "Age":age, "total_marks":str(total_marks),'percentage':str(percentage)}

    students.append(std)

    ans=input("Do you want to insert the record of the Student (y/n) : ")
    print()

print(students)
print()

# here records contains all dictionaries inside the students list.

print()
print("================= Students Records ====================")

index=1
for records in students:

    print(f"""
    Name of Student {index} :\t{records["Name"]} 
    Age  of Student {index} :\t{records["Age"]}
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Total Marks is :\t{records["total_marks"]}
    Percentage  is :\t{records["percentage"]}
..............................................................\n
""")
    
    index+=1

print("=========================================================")



f = open("Students records.txt","a")
f.write("\n")
f.writelines(str(students))
f.close()









