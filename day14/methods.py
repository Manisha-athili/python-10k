arr = [123,43]
#print(arr[-3])#list index out of range

print(len(arr))

#methods in python
# append() :: add single element at end 
# extend :: adds multiple element at end 
# insert(index wr to add, value) :: adds ele in required position. 
#search():
# count():
# clear():
# sort():
# reverse():

#append and extend
list = [1,4,"str",[2,34,5],True]
list.append("hi")
print(list)

#list in list
list.append([2,34])
print(list)

# extend 
list.extend([2,3,6,86])
print(list)

list1 = []
for i in range(0,100):
    if i % 3 ==0:
        list1.append(i)
        list1.extend([i])
print(list1)

# 99 ..... 45, 0,3,4,......42
list2 = []
for i in range(0,100):
    if i and i<45:
        list2.append(i)
    elif i%3==0:
        list2.insert(0,i)
print(list2)



