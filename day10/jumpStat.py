# Jump Statements:::  

# Break
# Continue
# Pass

# Break -- Stops or terminates the loop. anthardanga stop avtundi...

for i in range(0,11):
    if i == 5:               # 5 will not print
        break
    print(i)


for i in range(0,11):
    print(i)
    if i == 5:               # 5 will  print
        break


for i in range(0,11):
    print(i)
    if i == 5:               # all nums upto 4   will  print two times .. but 5 one time
        break
    print(i)


for i in range(0,100):         # loop itarates one time... and breaks
    break

# Continue :: Skips the current itration  of the loop...

for i in range(0,11):
    print(i)                        #  prints all i values 
    if i in [5,6,7]:               
        break                       # breaks at 5 , 6,7 and skips loop and continues to next itration...
    print(i)                          #   prints all i values except 5,6,7 

for i in range(0,10):
    continue                        # itrates for 10 times as it shows effect on block of code only but not on itration

for i in range(0,10):
    continue  
    break                             # break will not hit(work) as continue skips it.... break will not excutes ...


# Examples


for cls in range(1,11):
    
    if cls==5:
        break                     # here upto 4 the loop runs and prints class and roll nos,nxt will stops

    print("Class", cls, "roll nos: ")
    for roll in range(1,31):               
        print("class : " ,cls, "roll no. : ", roll)


for cls in range(1,11):
    print("class", cls , "Roll nos")
    for roll in range(1,31):
        if cls==5 and roll >15:         # here all class prints but in cls 5 after 15 nothing will print
            continue
        print(cls, roll)   # here 

for cls in range(1,11):
    print("class", cls , "Roll nos")
    for roll in range(1,31):
        if cls==5 or roll >15:        # here all class prints but in all cls after 15 and cls 5willvot print
            continue
        print(cls, roll)   # here 



for cls in range(1,11):
    print("class", cls , "Roll nos")
    for roll in range(1,31):
        if cls==5:         # here all class prints but inner for loop will break so 5 cls rollwill not wrk
            break
        print(cls, roll)   
print("break")


for cls in range(1,11):
    print("class", cls , "Roll nos")
    if cls==5:        # here upto 4 cls only prints and breaks at 5...
            break
    for roll in range(1,31):
        print(cls, roll)  


# pass in python ::: why not in other::
#  in other lang we have { flower brakects } to show it is empty or ..
# but in py  we use pass







