"""
=> In python we have some data types, that stores values in the form of collection.

-> list :- Ordered(value have index number) , Mutable(Changable) , Allow Duplicates , Hetrogenious  => [value1,value2,...]
-> tuple :- Ordered , Immutable(Not Changable), Allow Duplicates => (value1,value2,...)
-> set :- Unordered , Mutable , Not Allow Duplicates => {value1,value2,.....}
-> dictionary :-(Store data in key and value pairs), Unordered , Mutable , Not allow duplicates keys. => {key:value,key:value,..}

"""

# ========================= List Data Type ==========================
"""
=> it stores multiple values in a single variable with comma seperation, Inside square brackets.

=> Data inside the list is Ordered.(every value have index number,which starts from 0)
=> Data is mutable(Changable)
=> Allow Duplicates values
=> hetrogenious :- Allow different types of data types values.

syntax :- 
-----------
listName = [value1,value2,......]

"""
user1=["Ram",35,"Mathura",True,90.34,101,35,True]
# print(type(user1)) => <class 'list'>

# We can access values inside the list using index number.
# NOTE : last value have -1 index number.
# syntax :- listName[index] => return value at that index number.

# print(user1[-1])

# ============= Iterate over a list =================
# Looping through the list.

# for i in user1:
#     print(i)

# =========== change values inside the list ===========
# listName[index] = value

user1[0]="Shyam"
# print(user1)

# ======================== List Functions or Methods ============================
"""
=> len(listName) :- Return the length of the list.

========================== Add values inside the list ==========================

=> .append(value) :- It add a new value inside the list,At last
=> .insert(index,value) :- Add value at specific index number.
=> .extend(list2) :- To combine two lists.

========================= Remove values from the list ===========================

=> .pop() :- Remove a value from last of the list.
OR
   .pop(index) :- Remove particular index value.

=> .remove(value) :- Remove particular value from the list.   
=> .clear() :- Remove all values from the list and return the empty list.
=> del :- It deletes the list.
OR 
   del listName[startIndex:endIndex+1] :- Remove values in a range.

======================== list extra methods ==========================================
=> max(list) :- Return the maximum value from list
=> min(list) :- Return the minimum value from list
=> .sort() :- It arrange the list in 'accending order' (Sort the original list and also reflection show in original list)
=> .copy() :- It is used to generate the copy of the list.
=> .sum() :- Add all values from the list.
=> sorted(list) :- It arrange data in accending order (create a another sorted list)
=> .count(value) :- It return the count of a value inside the list.
=> .index(value) :- Return the index number of given value.
=> .reverse() :- It reversed the list.
======================================================================================
"""
# print(len(user1))

user1.append("Geeta")

user1.insert(1,"first")

# print(user1)

l1=[10,20,30,40,50]
l2=[1.1,2.2,3.3,4.4]

# l1.extend(l2)
l3=l1+l2
l4=l1*2

print(l1)
# l1.pop()
# l1.pop(3)

# l1.remove(20)

# l1.clear()

# del l1

# del l1[1:4] => [10, 50]
# del l1[::] => []
# print(l1)


lst1=[3,54,1,-27,-10,48,547,578,89,1,2,3,4,4,3,3,3,3,32,3]
# lst2=[]

# for i in lst1:
#     if(i not in lst2):
#         lst2.append(i)
# print(lst2)

print(max(lst1))


# lst1.sort() #=> arrange data in accending Order.
lst1.sort(reverse=True) #=> arrange data in decending order.

print(lst1)
l7=lst1.copy()

# l7.reverse()
# print(l7[::-1])

print(l7.count(3))
# print(l7.index(-27))
