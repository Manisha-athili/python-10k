# Conditional statements -- Conditional , loop, jump statements.....

# conditional statements ::: 
# indendation if else elif intro....

username = "manisha"
password = "password"

username_input = input("Enter username")
password_input = input("enter password")

if username==username_input and password==password_input:
    print("Successfull")

else:
    print("incorrect")

# if(username==username_input):
#   print("successfull")
# else:
#     
#   if( password!=password_input):
#         print("password wrong")
#   if(username!=username_input):
#         print("username incorrect")
#   print("invalid credincials")
#         

if username==username_input and password==password_input:
    print("login successfull");
elif username!=username_input:
    print("invailded  username")
elif password!=password_input:
    print("password invaild")
else:
    print("invalid credincials")

# loops --- for , while :::

# why loops :: file size, time management, efficiency, code maintainnability.... {if one line changes whole code will change}

# For loop in python ::
for y in range(0,20):  # ub ex
    print(y) #
    print("yevvadiki uppayogam") #static

# even numbers:::
for i in range(0,50):
    if i%2==0:
        print(i , " is even number")

for i in range(0,50):
    if i%2!=0:
        print(i , " is odd number")
        
for i in range(0,50):  # conditon is different
    if i%2==1:
        print(i , " is odd number")

for i in range(0,50):
    if i%2==0:
        print(i , " is even number")
    else:
        print(" is odd number")

for i in range(0,50,2):  # conditon is different ---- steping
        print(i , " is even number")

for i in range(0,50,1):  # conditon is different  ---- steping
        print(i , " is odd number")


#  interview que:::::
# diff b/t version 2 and 3 in py ???
#  backward compatablilty :::: if old 2 version code is supported in new version 3... if it runs it is backword compability...
# code of py2 can be writen in py3   but py3 not support py3...

# py 3 is not  backward compatablilty...

# assignment??  day 
# current bill 0 to 100 : 50 rs pre unit 
#             101 to 200 ==> 100 rs per Unit 
# more than 200 then 150 per unit
# with and 


        
        
