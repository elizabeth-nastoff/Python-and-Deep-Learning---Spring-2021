# Steps
# take two numbers from user input
# perform arithmetic operators

# input is declared as floats, otherwise they'd be strings
X = float(input("Enter first number:"))
Y = float(input("Enter second number:"))

# operations for + - / * are done in the print statements
print(X, "+", Y, "=", X+Y)
print(X, "-", Y, "=", X-Y)
print(X, "/", Y, "=", X/Y)
print(X, "*", Y, "=", X*Y)

# works with decimals and negative numbers
# no implementation to round the results