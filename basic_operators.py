import math

def addition(addI,addII):
    return addI + addII

addI = 3
addII = 9
print(addI,'plus',addII,'is:',addition(addI,addII))


def subtraction(subtractI,subtractII):
    return subtractI - subtractII

subtractI = 9
subtractII = 3
print(subtractI,'minus',subtractII,'is:',subtraction(subtractI,subtractII))

def multiplication(multiplyI,multiplyII):
    return multiplyI * multiplyII

multiplyI = 3
multiplyII = 9
print(multiplyI,'times',multiplyII,'is:', multiplication(multiplyI,multiplyII))

def division(divideI,divideII):
    return divideI/divideII

divideI = 9
divideII = 3
print(divideI,'divided by',divideII,'is:', division(divideI,divideII))

def exponent(expI,expII):
    return math.pow(expI,expII)

expI = 3
expII = 9
print(expI,' to the power of ',expII,' is: ', exponent(expI,expII))


def modulus(modulusI,modulusII):
    return modulusI % modulusII

modulusI = 10
modulusII = 3
print('Remainder of',modulusI,'divided by',modulusII,'is:',modulus(modulusI,modulusII))

def another_addition(addIII,addIV):
    addIII += addIV
    return addIII

addIII = 4
addIV = 8
print(addIII,'plus',addIV,'is:',another_addition(addIII,addIV))

def another_subtract(subtractIII,subtractIV):
    subtractIII -= subtractIV
    return subtractIII

subtractIII = 8
subtractIV = 4
print(subtractIII,' minus ',subtractIV,' is: ', another_subtract(subtractIII,subtractIV))

def another_multiplication(multiplyIII,multiplyIV):
    multiplyIII *= multiplyIV
    return multiplyIII

multiplyIII = 4
multiplyIV = 8
print("4 times is 8: ", another_multiplication(multiplyIII,multiplyIV))

def another_division(divideIII,divideIV):
    divideIII /= divideIV
    return divideIII

divideIII = 8
divideIV = 4
print(divideIII,'divide by',divideIV,'is: ',another_division(divideIII,divideIV))