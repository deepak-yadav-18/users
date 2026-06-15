"""
=========================== TUPLE ==========================
------------------------------------------------------------
=> It can also store multiple values in a single variable.

-> Data is Ordered
-> ImMutable(Not-Changable)
-> Allow Duplicates 

syntax:-
--------

tupleName = (value1,value2,...)
OR 
tuple(list/set) :- Convert them into tuple.

========== tuple methods ==========
=> .index(value) :- return index value of given index
=> .count(value) :- Return the count of the value.
"""

tpl = (10,39,58,"Hello","Ram",True,84.547,10,10,10,39)
# iterate over a tuple (access each value by using loop)

# for i in tpl:
#     print(i)
# print(tpl)

# print(tpl[0])


# print(tpl.index("Hello"))
# print(tpl.count(10))


s="olevel"
# start = -1 , end = -6 , step=-1(it represents string will we printed in reverse order ) 
# end value should be +1, but in this case we have -ending value so we add -1 with -len(s)-1

for i in range(-1,-len(s)-1,-1):
    print(s[i])