#Write function subtractTwo that takes in a number, and returns a value that is 2 less than that number
x = 4
def subtractTwo(x):
    x - 2
    return x
y = x - 2
print(y)
#Homework: Write a function isEven that takes in a number and returns True if it’s even and returns False if it’s odd
x = 3
def isEven(x):
    if x % 2 == 0:
        return True
    elif x % 2 != 0:
        return False
y = isEven(x)
print(y)

#Homework: Write a function isNegativeAndEven that takes in a number and returns True if it’s even and a negative number.
# Return False if it is odd or a positive number.
y  = -2
def isNegativeAndEven(y):
    if y % 2 == 0 and y % 2 < 0:
        return True
    elif y % 2 != 0 and y % 2 > 0:
        return False
m  = isNegativeAndEven(y)
print(m)

# Write a function isNegativeAndEven that takes in a number and returns True if it’s even and a negative number.
# Return False if it is odd or a positive number.
x = - 2
def isNegativeAndEven(x):
    if x % 2 == 0 and x % 2 < 0:
        return True
    elif x % 2 != 0 and x % 2 > 0:
        return False
c = isNegativeAndEven(x)
print(c)

# Break this down into 1 function isNegative that returns true
# if a variable is negative and 1 function isEven that returns true if a variable is even.
# Both of these functions will be called in  isNegativeAndEven and will return True if the number is negative and even.


def isNegative(x):
    if x < 0:
        return True
def isEven(o):
    if o % 2 ==0:
        return True

def isNegativeAndEven(t , u):

    t == isNegative(x)
    u == isEven(o)

    print(t , u)

#Write function absoulteValue that takes in a value and returns the absolute value of it

import math

print(math.fabs(-55))

#Write function powerTo that takes in a two numbers and returns the first number to the power to the second number

import math
print(math.pow(5 , 3))


# Write function howMuchToPay that takes in 2 variables totalCost and numPeople
# and tells everyone how much of the bill they must pay (assuming we split the bill evenly).
# Round the amount everyone owes to the nearest dollar
import math
totalCost = 50
numPeople = 5
print(math.ceil(totalCost / numPeople))


# Write a function zodiacAnimal that calculates what animal sign you are in the chinese zodiac based on the year you were born.
# You may use Google to find out what the animals are and what years they correspond to.(think what operator should we use?)
year = 1990

def zodiacAnimal(year):
    if year % 12 == 0:
        print("Monkey")

    elif year % 12 == 1:
        print("Rooster")

    elif year % 12 == 2:
        print("Dog")

    elif year % 12 == 3:
        print("Pig")

    elif year % 12 == 4:
        print("Rat")

    elif year % 12 == 5:
        print("Ox")

    elif year % 12 == 6:
        print("Tiger")

    elif year % 12 == 7:
        print("Rabbit")

    elif year % 12 == 8:
        print("Dragon")

    elif year % 12 == 9:
        print("Snake")

    elif year % 12 == 10:
        print("Horse")

    elif year % 12 == 11:
        print("Sheep")

zodiacAnimal(year)