# conditional statements:: 
# if - else
# if-elif


# print("i can vote")
# print("i cannot vote")
# 2 conditions will work...in real one can be ture so to impli  here controls statements comes..

# if age is greater than 18 i can vote or else I cannot vote.
age =18
if age > 18:
    print("i can vote")
    print("i can vote1")
    print("i can vote2")
print("responsible citizen")
#   print(" citizen") error : indentation error
print("responsible citizen")

# if condition should start with atleast 1 space.....


if age >= 18:
    print("i can vote")
    print("i can vote1")
    print("i can vote2")
else:
    print("ifelse")
#    print("ifelse") error indentation error
    print("")
print("responsible citizen")
#   print(" citizen") error : indentation error
print("responsible citizen")

# t or F

if True:
    print("i can vote")
    print("i can vote1")
    print("i can vote2")
else:
    print("ifelse")

if False:
    print("i can vote")
    print("i can vote1")
    print("i can vote2")
else:
    print("ifelse")

# if the num is positive print positive or else print negative
num = int(input("enter a num"));
if num>0:
    print(num," is positive")
else:
    print(num, " is negative")

# --------

num = int(input("enter a num"));
if num>0:
    print(num," is positive")
else:
    if num==0:
        print(num, " zero")
    print(num, " is negative") # zero and  negative also prints so... follows
