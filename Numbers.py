import math
import random
from fractions import Fraction as F

def get_random_numbers(randomI,randomII):
    print(random.randrange(randomI,randomII))


randomI = 10
randomII = 20
get_random_numbers(randomI,randomII)

def add_random_numbers(randI,randII):
    first_rand = random.randrange(randI,randII)
    second_rand = random.randrange(randI,randII)
    sums = first_rand + second_rand

    print("first random ",first_rand,"added to second random",second_rand,'is',sums)

randI = 20
randII = 30
add_random_numbers(randI,randII)

def even_random_number_in_range(firstrand,secondrand):
    randvalue = random.randrange(firstrand,secondrand)
    if randvalue % 2 == 0:
        print(randvalue,"random number value is even.")
    else:
        print(randvalue,"is not an even number.")

firstrand = 10
secondrand = 20
even_random_number_in_range(firstrand,secondrand)


def string_to_int(string_letter):
    print(string_letter,"string becomes an interger ",int(string_letter))


string_letter = "27"
string_to_int(string_letter)


def def_odd_random_number_in_range(firstOddrange,secondOddrange):
    oddRandom = random.randrange(firstOddrange,secondOddrange)
    if oddRandom % 2 != 0:
        print(oddRandom,"is an odd number.")
    else:
        print(oddRandom,"is an even number.")


firstOddrange = 10
secondOddrange = 20
def_odd_random_number_in_range(firstOddrange,secondOddrange)

def greater_than_random_range(firstNumber,secondNumber):
    greaterrangeI = random.randrange(firstNumber,secondNumber)
    greaterrangeII = random.randrange(firstNumber,secondNumber) 
    if greaterrangeI > greaterrangeII:
        print(greaterrangeI,"generated random number is greater than the second generated random number",greaterrangeII)
    if greaterrangeII > greaterrangeI:
        print(greaterrangeII,"generated random number is greater than the second generated random number",greaterrangeI)

firstNumber = 10
secondNumber = 20
greater_than_random_range(firstNumber,secondNumber)

def exponent(base,power):
    resultExponent = pow(base,power)
    print(base,"to the power of",power,"is",resultExponent)

base = 2
power = 2
exponent(base,power)


def fraction(fractionValueI,fractionValueII):
    fracted = F(fractionValueI,fractionValueII)

    print("fraction of value",fractionValueI,"and value",fractionValueII,"(simplified) is ",fracted)


fractionValueI = 45
fractionValueII = 54
fraction(fractionValueI,fractionValueII)

def square_root(squarevalueI):
    squared = math.sqrt(squarevalueI)

    print(squarevalueI,"squared is",squared)


squarevalueI = 16
square_root(squarevalueI)

def number_index(numList,ber):
    count = 0
    for index in numList:
        if index == ber:
            print(ber,"found in index",index)
            count += 1
    if count == 0:
        print("not found")

            
numList = [1,2,3,4,5,6,7,8,9]
ber = 9
number_index(numList,ber)