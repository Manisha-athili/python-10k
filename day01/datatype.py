# print("Day 1")

#Datatypes
# 1.Numeric data types
# 2.Sequence Data types :: list , 
# 3.Set
# 4.Dictionary

#Numeric Data types
#1.Int data type
#2.Float data type 
#3.Complex number data type : a + jb : ex 2+3j + 4 + 5j = 6+8j;
#4.Boolean data type: Ture and false;


# # int
# num1 = 21
# num2 = 4
# print(type(num1))
# # oprations
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 % num2)
# print(num1 ** num2)

# # float
# num1= 21.0
# num2=4.0
# print(type(num1))
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 % num2)
# print(num1 ** num2)

# # boolean # boolean : capital T,F only 
# bool= True
# print(type(bool))
# # boolen : capital T,F only 
my = 123
you = 4

# int class
print(type(my))


#boolean class
print(type(my==you)) 


# true condition
print(my==you) 


# false condition
print(my!=you)


my = "hi"
you = "hello"
# type boolen class
print(type(my))

# boolean class
print(type(my==you)) 

# boolean conditions
print(my==you) 
print(type(len(my)==len(you)))
print(my==you) 

print("---")

# complex number
img1 = 2+3j;
img2 = 5+1j;
# type
print(type(img1))

# operations
print(img1+img2)
print(img1-img2)
print(img1**img2)
print(img1*img2)
print(img1/img2)
# print(img1//img2); this will not work
# In result1 we are performing floor division between two integers, 10 and 3. The result of dividing 10 by 3 is 3.333...., but floor division returns the largest integer less than or equal to the result. Therefore, the result is 3.

# print(img1%img2); this will not work

print("--------")

print("Sequences - string, list, tuple, and range")
# Sequences - 
# string, 
# list, 
# tuple, and 
# range

# strings: sequence of characters
str1="10k coders"
str2="hello"

# print string
print(str1);
print(str2)

# length
print(len(str1))
print(len(str2))
name = "Sai teja Sir"
print(name)
print(len(name))

# string indexing : (0 to length-1) or  (-n to -1)
print(str1[0])
print(str2[0])
print(name[2])


# negative indexing
print(str1[-10])
print(str2[-5])
# print("--")
print(name[-10])

# slicing (or) Substring
print(str1[4:11])
# print(str1[4:11:-1]) empty string reads from left to rigth
print(name[0:8]) # slicing wil not print upperbond indexing value

# right to left
# print("-")
print(str1[-4:-1])
print(name[-4])
# print(str1[-4:-1:-1]) empty string not work  string reads from left to rigth
# print(str1[-1:-4]) empty string not work string reads from left to rigth


# index steping ;; leave str1[-4:-1:n] skips n-1 nums and prints...
print(str1[-4:-1:2]) 
print(name[-4:-1:2])

#String : adding element  list have appened
str1 += " welcome"
print(str1)

name += " is smart"
print(name)


# why string immutable : 
print("when different varible refer a value .it is difficult to change particualar referance so to avoid it, strings are made immutable")
str1 = "str"
str2 = "str"
str3 = "str"
print(id(str1))
print(id(str2))
print(id(str3))

# immutable object can’t be changed after it is created. int, float, bool, string, Unicode and tuple.
# mutable :: can change tuble and list value can be changed but particular 

# list : collection of sequenced items and it is mutable datatype 
# print("list can store hetrogenous items and size can flexable ;; datatype and size have no restrictions"

list1 = [1, 2.2 , "str1", 2+3j,True, ['hi','im here']];
print(list1)

# type
print(type(list1))

# to add item
list1.append("im extra")
print(list1)
print("--------")

# index
print(list1[2])

# slice
print(list1[3:])
print(list1[:4]) # upperbound not inclued

# accessing list of list
print(list1[5][1])

list2 = ['hi','im here',1, (2,6),{8,"6"},]
print(list2)
# print(list2[4])


# string is immutable in python and js not in other lang
print('for loop')
for i in list1:
    print(i);


# tuple
# string and tuple are immutable in python and js not in other lang
