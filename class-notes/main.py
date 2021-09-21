# Homework!!!!!!! Turn these into functions
# .1. Function isLessThan that returns whether the first value is less than the second value
x = 5
y = 6
def isLessThan(x , y):
    if x < y:
        return(x , y)
isLessThan(x , y)
print("x < y")

#   2. Function isGreaterThan that returns  whether the first value is greater than the second value
x = 5
y = 4
def isgeaterThan(x , y):
    if x > y:
        return(x , y)
isgeaterThan(x , y)
print("x > y")

#   3. Function isLessThanOrEqualTo that returns whether the first value is less than or equal to the second value
x = -1
y = 1
def isLessThanOrEqual(x , y):
    if x <= y:
        return(x , y)
isLessThanOrEqual(x , y)
print("x <= y")

#   4. Function isGreaterThanOrEqualTo that returns whether the first value is greater than or equal to the second value
x = 1
y = -1
def isGreaterThanOrEqualTo(x , y):
    if x >= y:
        return(x , y)
isGreaterThanOrEqualTo(x , y)
print("x >= y")

#   5. Function isEqual that returns  whether the first value is equal to the second value
x = 1
y = 1

def isEqual(x , y):
    if x == y:
        return(x, y)
print("x == y ")

# Homework!!!!!!! Write the output of each expression + no cheating USE UR BRAINSICLES ***
# Hint: if there are no parenthesis, expressions are read left to right
# 1.not(not False) is false
# 2.(not False) or True  is  ture
# 3.False and False and True  is false
# 4.True and True and False is false
# 5.(3 >= 2) or (-1 is not 1) and (“zero” is “zero”) is true
# 6.(“hello” > “hello friends”)  is false

# Practice/hm
#If 100 is greater than or equal to 3, print out “foo”. Otherwise print out “bar”
x = 100
def function(x):
    if x > 3:
        print("foo")
    else:
        print("bar")
function(x)

#   If “hello” equals “hello”, print out “hello is equal to hello”. Otherwise print out “nah”

hello = "hello"
def function(hello):
    if hello == "hello":
        print("hello is equal to hello")
    else:
        print("nah")
function(hello)

#   Write a function that takes in variable y. If y is equal to 3, print out “this value is three”. Otherwise print out
#   “this value is not three”
y = 5
def function(y):
    if y == 5:
        print("this value is three")
    else:
        print("this value is not three")

#   Write a function that takes in variable x and y. If x is equal to True or y is equal to True print out
#   “There is a value equal to true”.
#   Otherwise print out “they both are not true”

x = "ture"
y = "false"

def function(x,y):
    if x == "ture" or y == "ture":
        print("There is a value equal to ture")
    else:
        print("they both are not ture")
function(x,y)

#   Homework!!!!!!!  Write out these functions
#   1.Write a function isBigAndPositive that takes in 2 values, first and second.
#   If first is equal to second and first is greater than 0, print out “The first number is a positive number greater than 0”.
#   Otherwise print out “The first number must be negative or smaller than the second value”
first = 2
second = 1
def isBigAndPositive(first , second):
    if first == second and first > 0:
        print("The first number is a positive number greater than 0")
    else:
        print("The first number must be negative or smaller than the second value")

isBigAndPositive(first , second)


#   Write a function isSmallorNegative that takes in 2 values first and second.
#   If first is less than second and first is less than -1, print out “The first number is smaller than the second or is negative”.
#   Otherwise print “The first number is larger than the second or is not negative”

def isSmallorNegative(first , second):
    if first < second and first < -1:
        print("The first number is smaller than the second or is negative")
    else:
        print("The first number is larger than the second or is not negative")
isSmallorNegative(first , second)


#  Homework: Create these functions.
#  1.isIntegerOrString (takes in 1 variable, if it’s a string it will print “this is a string”.
#  If it’s an integer, it will print “this is an integer”)
u = 1
def isIntegerOrString(u):
    if (type(u)) == str:
        print("this is a string")
    elif (type(u)) == int:
        print("this is a integer")
isIntegerOrString(u)


#   isDivisibleByFive (takes in 1 variable, if it’s divisible by 5 it will print “this is divisible by 5”.
#   if it’s not divisible by 5, it will print “this is not divisible by 5”)

o = 6

def isDivisibleByFive(o):
    if o % 5 == 0:
        print("this is divisible by 5")
    else:
        print("this is not divisible by 5")
isDivisibleByFive(o)


#   This one only needs to be done with if/else. gradingScale takes in variable grade.
#   If grade is greater than or equal to 90 print “Grade: A”. If grade is greater than or equal to 80 print “Grade: B”.
#   If grade is greater than or equal to 70 print “Grade: C”. Otherwise, print “you have failed the class”
g = 65
def grade(g):

    if g >= 70 and g < 80:
        print("Grade: C")
    if g >= 80 and g < 90:
        print("Grade: B")
    if g >= 90:
        print("Grade: A")
    if g < 70:
        print("you have failed the class")

grade(g)