"""Python for Visual Effects.

Assignment #1 - Data Types and Variables

Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32
print(64+32)
# 2.- Do the same as the question one but this time use variables instead of 
# numbers.
number1= 64
number2= 32
number3 = number1+number2
print(number3)

# 3.- Make a program that prints a sentence that includes at least 3 variables.
a ="country is india"
b ="state is westbengal"
c = "city is kolkata"
d =a+b+c
print(d)

# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."
y = "This is my first Python program."
print(len(y))

# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"

x = 1920 * .10
y = 1080 * .10

print(
" The 10% overscan of 1920 is " + str(x) + ", and the 1080 is " + str(y))