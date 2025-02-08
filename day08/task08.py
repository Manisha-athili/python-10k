
#Current bill units in between 0 to 100 then 50 rupees per unit
# 101 to 200 - 100 rupees per unit
# More than 200 then - 150 per unit
#Mandatory service charge of 50 rupees for every user.
#Compute total current bill With and without elif statement.

units = input("Number of units: ")
bill=1;
if units<100:
    bill=50*units
    print()
elif units<200:
    bill= 100*units
elif units>200:
    bill= 150*units
else:
    print("Invaild number")