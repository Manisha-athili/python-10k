#  Function s ;;;;   

# print("start1");
# print("start2");
# print(4/5 * 3.14 *10 *10* 10);
# print("end1");
# print("end2");


# print("start1");
# print("start2");
# print(4/5 * 3.14 *20 *20* 20);
# print("end1");
# print("end2");


# print("start1");
# print("start2");
# print(4/5 * 3.14 *30 *30* 30);
# print("end1");
# print("end2");

#this all are repitative tasks... to decrease it we use functions... 

def myName(r):         # parameters
    print("start1");
    print("start2");
    print(4/5 * 3.14 *r * r *r);
    print("end1");
    print("end2");

myName(10);  # arguments
myName(20);

# diff b/t  loop and func :  flexibility
 
# position arguments
def myName(pie,r):         # parameters
    print("start1");
    print("start2");
    print(4/5 * pie *r * r *r);
    print(pie)
    print(r)
    print("end1");
    print("end2");

myName(3.14,10)  # position arguments
myName(2.14,20)
# mapping depends on positions..


# keyword arguments::
def myName(pie,r):         # parameters
    print("start1");
    print("start2");
    print(4/5 * pie *r * r *r);
    print(pie)
    print(r)
    print("end1");
    print("end2");

myName(r=10,pie=3.14)  # keyword  arguments
myName(pie=2.14,r=20)

# default ::  values are given in parameters...in declaration
def myName(pie,r):         # parameters
    print("start1");
    print("start2");
    print(4/5 * pie *r * r *r);
    print(pie)
    print(r)
    print("end1");
    print("end2");

myName(10,23)  # default arguments
myName(2.9,r=20)

# examples ::: 
def calc(a,b=1):
   print(a+b)
   print(a-b)
   print(a*b)
   print(a**b)

calc(2,5)
calc(9,11)  # normal function
print("normal function")
print(calc(9,11))

def calc(a,b=1):
#    print(a+b)
#    print(a-b)
#    print(a*b)
#    print(a**b)
   return a+b

calc(2,5)
calc(9,11)
print(calc(1,2))
print(calc)  #<function calc at 0x000001375B4C3E20>
print(id(calc))    # not equal


def calculate(a,b=1):
   return a+b, a*b, a-b, a/b

calculate(3,8)

# list functions::

def print_even_place(input_list):
    for k in range(0,len(input_list)):
        if k%2==0:
            print(input_list[k])

list = [2,4,5,7,9,5]
print_even_place(list)


