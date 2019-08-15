import random

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

def even_random_number(firstrand,secondrand):
    randvalue = random.randrange(firstrand,secondrand)
    if randvalue % 2 == 0:
        print(randvalue," random number value is even.")
    else:
        print(randvalue," is not an even number.")

firstrand = 10
secondrand = 20
even_random_number(firstrand,secondrand)