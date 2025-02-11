#  lambda  real useage :: 
# map, filter, reduce : 
# functions are passed as arguments ...
# MAPS : 
#  

from functools import reduce        # 
def double(x):
    return x*2

map_example = map(double, [1,2,3,4,5])  
print(map_example )         # returns defination
print(list(map_example ))   # returns [2,4,6,8,10]


# lambda why??
map_example = map(lambda x : x*2, [1,2,3,4,5])  
print(map_example )         # returns defination
print(list(map_example )) 

# filter::
def even_filter(num):
    if num%2==0:
        return True
    return False
filter_example = filter(even_filter, [1,2,3,4,5])  
print(filter_example)         # returns defination
print(list(filter_example ))   # returns [2,4,6,8,10]


# lambda using filter::

filter_example = filter(lambda a:a%2==0, [1,2,3,4,5])  
print(list(filter_example ))  # lambda helps to add 

# reduse 

# reduce :: 
reduce_example = reduce(lambda x,y : x+y,[1,2,3,4,5,6])
print(reduce_example)

# local scope to globle:::
num1 = 10

def ex_function():
    # global num1  ==> to change local to globel scope
    num1 = 25
    print(num1)
ex_function()
print(num1)

#  both num1 local scope and globle scope and 1 want
def ex_function():
    num1 = 25;
    globals()[num1]=45 #helps to convert local to glbal
    print(num1)

ex_function()
print(num1)


# String inbuilt functions ::
str1 = "i love python";
print(str1.replace("python","code"))
print(str1)

# strings in py are immutable str1 will remain same but only changes here str1.replace("python","code")  