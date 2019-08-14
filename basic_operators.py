import math

def add(a,b):
    return a + b

print("3 plus 9 is: ", add(3,9))


def subtract(a,b):
    return a - b

print("9 minus 3 is: ", subtract(9,3))

def multiplication(a,b):
    return a*b

print("3 times 9 is: ", multiplication(3,9))

def division(a,b):
    return a/b

print("9 divided by 3 is: ", int(division(9,3)))

def exponent(a,b):
    return math.pow(a, b)

print("3 to the power of 9 is: ", exponent(3,9))

def modulus(a,b):
    return a % b
print("Remainder of 10 divided by 3 is: ", modulus(10,3))

def anotherAdd(a,b):
    a += b
    return a
print("4 plus 8 is: ", anotherAdd(4,8))

def anotherSubtract(a,b):
    a -= b
    return a
print("8 minus 4 is: ", anotherSubtract(8,4))

def anotherMultiplication(a,b):
    a *= b
    return a
print("4 times is 8: ", anotherMultiplication(4,8))

def anotherDivision(a,b):
    a /= b
    return a
print("8 divided by 4: ", anotherDivision(8,4))