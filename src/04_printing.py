"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("% 2d" %x)
print("% 2.3f, and % 2d" %(y, x))
print("x is % 2d, y is % 1.2f, z is % s" %(x,y,z))

# Use the 'format' string method to print the same thing
print("{0}".format(x))
print("{0}, and {1}".format(y, x))
print("x is {0}, y is {1:1.2f}, z is {2}".format(x, y, z))

# Finally, print the same thing using an f-string
print(f"{x}")
print(f"{y}, and {x}")
print(f"x is {x}, y is {y}, z is {z}")