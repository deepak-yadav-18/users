"""
================================== SET Data Type ===================================
=> Unordered :- No index number
=> Not allow Duplicates
=> It is Muatable , NOTE :- we can not change given Values, but we can add or remove values

NOTE :- set does not allow list,set and dictionary as a data Type.

setName = {value1,value2,value3,......}

set(list/tuple) :- convert it into set data type
"""

st = {10,29,"hello",-127,-38,True,10,"hello",3278}

st.add(1011)
st.remove("hello")
# print(st)

for i in st:
    print(i)