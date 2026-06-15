"""
1. Find the sum of all values inside the list
[1,2,3,4,5,10,21] => 46

2. Remove all duplicates from the list.

"""
# ========== find the count of even and odd numbers in a list =========
# ========== find the sum of even and odd numbers in a list =========
def Sum_and_count():
    lst=[39,2,32,4,4,65,5,54,43,3,32,43,54,76,98]

    count_even=0
    count_odd=0

    sum_even=0
    sum_odd=0

    sum=0

    for i in lst:
        sum+=i
        if(i%2==0):
            count_even+=1
            sum_even+=i
        else:
            count_odd+=1
            sum_odd+=i

    print(f"""
------------- counting and sum program ----------------
      Total Values inside the list :- {len(lst)}
      Total Sum of all values inside the list :- {sum}
      ==========================================
      Total Even Numbers : {count_even}
      Total Odd Numbers : {count_odd}
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      Total sum of even numbers is : {sum_even}
      Total sum of odd numbers is : {sum_odd}
-------------------------------------------------------

""")

# Sum_and_count()

# def rotate_list(lst, num_rotation, direction='right'):
#     n = len(lst)
#     num_rotation = num_rotation % n  # handle cases where num_rotation > n

#     if direction == 'right':
#         return lst[-num_rotation:] + lst[:-num_rotation]
#     elif direction == 'left':
#         return lst[num_rotation:] + lst[:num_rotation]
#     else:
#         raise ValueError("Direction must be 'right' or 'left'")
# # Sample list
# my_list = [1, 2, 3, 4, 5]

# # Rotate right by 2
# rotated_right = rotate_list(my_list, 3, 'right')
# print("Right Rotation:", rotated_right)  # Output: [4, 5, 1, 2, 3]

# # Rotate left by 2
# rotated_left = rotate_list(my_list, 2, 'left')
# print("Left Rotation:", rotated_left)    # Output: [3, 4, 5, 1, 2]

"""
⚙️ Moderate-Level Python List Programs
================================================================================
1	Reverse a list without using reverse() or slicing.
2	Remove all duplicates from a list while maintaining order.
3	Find the second largest and second smallest element in a list.
4*	Count the frequency of each element in the list.
5	Find all even and odd numbers from a list and separate them.
6	Check if two lists are equal (same elements in the same order).
7	Find common elements in two or more lists (intersection).
8	Replace every element in a list with the product of all other elements.
9	Remove all elements from a list that are greater than a given value.
10*	Create a list of squares or cubes of numbers using list comprehension.
11	Merge two sorted lists into one sorted list (without using sort()).
12	Check if a list is a palindrome (same forward and backward).
13	Find all indices of a given element in the list.
14*	Split a list into two halves.
15*	Check if elements of one list are a subset of another list.
16	Find the sum of all prime numbers in a list.
17	Count the number of positive, negative, and zero values in a list.
18	Multiply all elements in a list.
================================================================================
"""

# ======================= List Comprehension ===================================
# it is sortest way to create a list.

# [variableName for variableName in range(start,end+1) if(condition)] 

# lst=[]
# for i in range(1,11):
#     lst.append(i)

lst=[i**2 for i in range(1,101) if(i%5==0)]
# print(lst)


lst2=[327,43,231,231,10,10,231,30,24,30,10,10]

frequency={} # here we create an empty dictionary
lst3=[]
for i in lst2:
    # frequency.update({i:lst2.count(i)})
    lst3.append((i,lst2.count(i)))
    # count=1
    # if(i in frequency):
    #     frequency[i]+=1
    # else:
    #     frequency[i]=1

# print(list(set(lst3)))
# print(frequency)


# u1=["Ram",35,45,"Mathura"]

# dictionary :- It stores data in key and value pairs
"""
=> dictionary is Unordered
=> Value accessed by key Name.
dictionaryName = {key:value, key:velue ,....}

NOTE :- Not allow duplicate keys

dictionaryName[key]
"""

u1={"Name":"Ram",35:"Id","Age":45,"Address":"mathura"}

# add a new key and value pair
u1["password"]=73282

# add a new key and value pair using .update(dictionary) function
u1.update({"Class":12})


# print(u1["Name"])
# print(u1[35])
# print(u1["password"])

# print(u1)





lst4=[327,43,231,231,10,10,231,30,24,30,10,10,67,89]

part1=[]
part2=[]


length = len(lst4)
half = length/2

for i in range(0,length):
    if(i<half):
        part1.append(lst4[i])
    else:
        part2.append(lst4[i])

lst5=[part1,part2]

# print(lst5)

# ================ checking subset of lists ==================
lst6=[10,43,231,67]
ans="Yes"
for i in lst6:
    if(i not in lst4):
        ans="No"
        break

# print(ans)

# ============= replace value with product of another values =============
l=[1,2,3,4,5]
# [120,60,20,5]
l2=[]
f=1
for i in range(len(l)-1,0,-1):
    if(i>0):
        # a=l[i+1]*[l+2]*l[i*3]*l[i*4]
        f=f*l[i]
    
    l2.append(f)
    # print(i)

print(l2)

# ========================= *args and **args ================================
"""
*args :- It can accept multiple arguments when we call the function.But in the form of TUPLE.
**args :- It can accept multiple arguments when we call the function.But in the form of DICTIONARY.
"""

def sum(a,b):
    print(a+b)

# sum(10,20,30)

def names(*name):
    print(name)
    for i in name:
        print(i)

def sm(*nums):
    for i in nums:
        sum=nums[0]+nums[1]
    print(sum)

sm(10,30)
# names('Ram',"shyam","karan","suman","Teena","geeta")

def users(**user):
    for i in user:
        print(i,user[i])
        # print(j)
    print(user)

# users(name1="Ram",name2="Shyam")

