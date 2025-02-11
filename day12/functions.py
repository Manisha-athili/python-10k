# def sum(a,b):
#     return a+ b;

# def sum(a,b,c):
#     return a+ b+c;

# def sum(a,b,c,d):
#     return a+ b+c+d;

# sum(2,4) #method overloading .... is not supported in python

# method overloading  is a function with same name but diff definations with same name... id not supported so we use orbitary arguments

# orbitary arguments :  dont no how many elements are there but it will accept all elements   

# using *

def sum(a,*b):
    add =a
    for i in b:
        add += i
    return add

print(sum(2,4,3,4,5,6,7))


def sum(a,**b):   # dicnationary values...
    add =a
    for i,j in b.items:
        add += j
    return add

print(sum(2,num1=4,num2=3,num3=4,num4=5,num5=6,num6=7))


def sum(*a,**b):
    add =a
    # for i in b:      here for is not excuting as all elements are moving to a only
    #     add += i
    return add

print(sum(2,4,3,4,5,6,7,98,))


# Scope :: global and local


num1 = 35               # global scope
def exm():
    num1 = 20           # local scope
    print(num1, "local scpoe") 
print(num1,"globle scope") 


num1 = 35               # global scope
def exm():
    global num1          # keyword to change local to globals
    num1 = 20           # local scope
    print(num1, "local scpoe") 
print(num1,"globle scope") 


num1 = 35               # global scope
def exm():
    global num1          # keyword to change local to globals
    num1 = 20           # local scope

    globals()['num1']=60  # other way to change local to globals using global functions
    print(num1, "local scpoe") 
print(num1,"globle scope") 


# Lambda functions :::  single line code without () and return statement with 

# keyword == lambda
lambda x : x*x 

lam = lambda x : x * 5
print(lam(2))

lam = 10 # as it is reassigned and function is earsed here...

lam3 = lambda x,y:x+y
print(lam3(2,3))

def square():
    return x*x

map(square, [1,2,3,4,5])
map(lambda x: x*x*x, [1,2,3,4,5]) #we use lambda function tp avoid repitition use of the function
