# Edit this function to make it print out upper case HELLO WORLD

def gethello():
    return "hello"

def getWorld():
    return "world"

def helloWorld():
    x = gethello()
    y = getWorld()
    return (x + y)

message = helloWorld()
print(message.upper())

# write a function turnUpperCase that takes in a variable. If the variable is already all uppercase, return it.
# If there is any lowercase, turn it all into upper case and return this new uppercase string.

x = "Hello World"
def turnUpperCase(x):
    if x.isupper():
        return x

    else:
       print(x.upper())
       return x.upper()
x1 = turnUpperCase(x)
print(x1)