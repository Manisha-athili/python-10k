
# tuple
print("------date ::: 28-01-2024------------")
tuple1 = (1,2,3,4,5)
tuple2 = (7,8,9)

tuple1 = tuple1+tuple2
print(tuple1)
# tuple is immutable but here tuple is re Assigned....

# Assigment operators ::  +, += ,-=, *=, /=, %=, **=

num1 = 5
num2 = 2
num1+3
print(num1)
# op :5 only compiler doesnot understand we didnt assigned like num1= num1+3;;


num1 = 5
num2 = 2
num1=num1+3
print(num1)  # developers are lazy 
num1 += 3
print(num1)

num1 -= 3
print(num1)

num1 *= 3
print(num1)

num1 **= 3
print(num1)

num1 /= 3
print(num1)

num1 %= 3
print(num1)

num1 //=num2
print(num1)

# logical Operators :: && and , || or,  ! not
# py is diff from js


# and -- if false
print(True and True)
print(True and False)
print(True and (True and False))
print(True and (True and (True and False)))
print(False and (True and False))
print(False and False)  # false
#if first is true it will check 2nd value  and returns false
# if first is false it directly returns false 

#compitation
print(3 and 2) #2
print(2 and 3) #3
print(0 and 2) #0
print(3 and 0) #0
print("" and 0) #""
print(3 and []) #[]
print(3 and ()) #()
print(() and []) #()
print(3 and ' ' and 7) # 7 
print({} and 2)#{}
#if first is true it will check 2nd value  and returns value
# if first is false it directly returns false vave

print("----or : any one can be true it will check 1st and 2nd ----")
print(3  or 2) #3
print(2  or 3) #2
print(0  or 2) #2
print(3  or 0) #3
print("" or  0) #0
print(3  or []) #3
print(3  or ()) #3
print(() or []) #[]
print(3  or ' ' and 7) #3
print({} or 0)#0

#not 
print("---Not ---")
print(not True);
print(not False)
print(not 2) #False
print(not 0) #True
print(not ()) #True
print(not []) #True


# Bitwise Operators:: & ,|, ^ , ~ , >> , << ,
# performs operations on every  bit ,... works on bits only
print("Bitwise Operators")
print(2&5)
# 010 $ 101 => 000 = 0
# 6 & 9 => 0110 & 1001 = 0
# 2 & 3 => 10 & 11 = 2
print(2|3) #3
print(2|5)
# 010 | 101 => 111 => 7
print(9|11) #11
print(bin(9))
print(bin(11))

# 1001 | 1011 = 1

# print(">> << work ??")