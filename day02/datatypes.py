
# tuple
# string and tuple are immutable in python and js not in other lang
# list is mutable
# Why these are immutable ?

num1= 26
print(type(num1))
print(id(num1))
num2 = 26
print (id(num2))
print("varible used to refer the value only not to store")

str1 = "hi"
print(type(str1))
print(id(str1))
str2 = 'hi'
print (id(str2))

print('number of different varibles with same values have a same location/id.. if we want to change a particular varible then all the varibles should change so to this bug strings in python are immutable ')


name = "str"
name = "str"
name = "str"
name = "str"
name = "str"
print(name);
print(id(str))
name = "str"
name = "str"
name = "str1"
print(name)
print(id(name))

print('so we cannt change particular index value of the string onl ')
print('--------')

# tuple immutable
tup1 = (1, 'hi',True, [1,"manisha"],"string")
print(type(tup1))
print(tup1[1]) 
# tup1[1]= 'welcome';
# tuple is immutable;
print(tup1[1]) 
print(tup1);
tup1 += (1)
print(tup1)

# difference blt tuple and list... important

# advanatages of tuple
# 1. not to make any chance by user
# it will dublicate the code and always to make change

# range datatype::
# range(0,10)
r1=range(0,10)
print(list(r1))

# slice
print()

# steps to skip
print(r1[2: 10: 2])

# diff b\t list and tuple
# tuple is fast than list;
# tuple is more effencent;
# tuple is immutable  list is immutable
#  sytax is difference






