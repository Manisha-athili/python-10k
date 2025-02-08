# for loop::

# for num1 in range(0,26):
#     print(num1)

#     if(num1 % 2==0):
#         print("Evev")
#     else:
#         print("odd")


#  fizz buzz fizzbuss

for i in range(1,102):
    if i%15 == 0:       # if 3 is given auto 15 will not work in multiplies of  
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i % 3== 0:
        print("Fizz") 
    else :
        print(i)


for cls in range(1,11):
    print("Class", cls, "roll nos: ")
    for roll in range(1,31):
        print("class : " ,cls, "roll no. : ", roll)


for cls in range(1,11):
    print("Class", cls, "roll nos: ")
    for roll in range(1,31):
        if cls != 5:                      # it will not print 5 class but 5 class loop will run....
            print("class : " ,cls, "roll no. : ", roll)


for cls in range(1,11):      
    print("Class", cls, "roll nos: ")
    if cls != 5:                     # efficiency tn up one code.... unwanted loop will not run....
        for roll in range(1,31):               
            print("class : " ,cls, "roll no. : ", roll)

for cls in range(1,11):
    print("Class", cls, "roll nos: ")
    if cls not in [5]:                     # is same tn up code
        for roll in range(1,31):               
            print("class : " ,cls, "roll no. : ", roll)

# if cls not in [1,5]

for cls in range(1,11):
    print("Class", cls, "roll nos: ")
    if cls  in []:                     # here noting will print as list is empty to print 
        for roll in range(1,31):               
            print("class : " ,cls, "roll no. : ", roll)



# /////While loop: runs the code till condition is false....

print("----while loop ::::")
# num1 = 5
# while num1 < 10:
#     print("whatever")
#     print("something")    infinate loop

# 1-25  whole number
num = 1
while num<26:
    print(num)
    num+=1

#  print 3 muliples

num =1
while num<26:
    if num%3 == 0:
        print(num , "is 3 multiples")
    else:
        print(num,"not multiple")
    num+=1;

# while loop is based on conditions  ....
# foe loop is based on valuses...





