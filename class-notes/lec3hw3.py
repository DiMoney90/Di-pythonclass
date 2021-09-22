# Write a function that takes in a string and returns the length of the string
x = "what's up?"

len(x)


# Write a function that takes in a string. If the length is greater than 10, have it print “this is a really long word”.
# Otherwise do nothing.

def longword(x):
    x == "wjwhasdiiasdasdasdsd"
    if len(x) > 10:
        print("this is a really long word")


# Write a function that takes in a string and returns the number of times the letter ‘a’ appears.

string = "apple eats apple"
print(string.count("a"))

# Write a function that takes in a string and prints the output of it when it is splitted after every comma.

string = " I like eat BBQ!"
print(string.split())

# Write a function that takes in a string and returns a new string that replaces every letter ‘a’ with the letter ‘b’ of the old string

string = "banana eat banana"
print(string.replace("a", "b"))

# Write a function that takes in a string representation of an integer (ex. “67” or “1000”).
# Then turn this into type integer and return this. `

string = "1000"
print(int("1000"))

# Write a function that takes in a string and removes the first letter in the string
string = "world"
print(string [1:])

# Write a function that takes in two strings x and y. If x is the reverse of y, then return True. Otherwise print false.
# (same link under “reverse”)
x = "hello"
y = "olleh"

def revers(x, y):
    if reversed(x) == y:
        print("ture")
    else:
        print("false")

# Write a function that takes in 2 strings and concatenates them with the string operator and returns this new string.

print("hello " + "world" )

# Now do this function above ^ again but using the join operator (same link under “join”).

print("w".join("hello"))

#Write a function myFunc that takes in string x. If there are only letters in x are in the alphabet, print “they’re in the alphabet”.
# If there are only numbers in string x , print “there are numbers in the string”.
# If x ends with an exclamation point, print “is an excited comment”.
# If there are any special characters in the string (special characters are # ! & in this example),
# print “there are special characters (#,!,&)in the string”. (same link under “Testing”).
