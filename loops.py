def displayNames():

    Names = ["Russel", "Dom",
             "Melch", "Ian"
            ]

    for index in Names:
        print(index, end= " ")
    print("\n")

displayNames()


def displayNumbers():

    num = 0
    while num != 10:
        num += 1
        print(num, end=" ")
    print("\n")

displayNumbers()

def letterWord():

    for index in "Swift Kind":
        print(index, end=" ")
    print("\n")

letterWord()

def loopBreak():

    Names = ["Russel", "Melch",
             "Dom", "Mary"
            ]
    for index in Names:
        if index == "Dom":
            break
        print(index, end=" ")

    print("\n")

loopBreak()



def loopContinue():

    Names = ["Russel", "Melch",
             "Dom", "Mary"
            ]
    for index in Names:
        if index == "Dom":
            continue
        print(index, end=" ")
    print("\n")

loopContinue() 

def loopRange(a):

    for index in range(a):
        print(index, end=" ")
    print("\n")

loopRange(9)

def listNames():
    Names = ["Russel", "Melch",
             "Dom", "Mary"
            ]
    for index in Names:
        print(index, end=" ")
    else:
        print("\nHonor students")

listNames()

def nestedLoop():
    numbers = [[1,1,1], [2,2,2],[3,3,3]]

    for index in numbers:
        print("\n")

        for each in index:
             print(each, end = " ")
    print("\n")
nestedLoop()


def whileCount():
    count = 0
    while count < 5:
        print(count, "is less than 5")
        count += 1
    else:
        print(count, "is equal to 5")

whileCount()


def whileCountless():
    count = 5
    while count >= 0:
        if count == 5:
            print(count, "is equal to 5")
        count -= 1
        print(count,"is less than 5")


whileCountless()