def even(a):

    if a%2 == 0:
        even = "even"
        odd = "odd"
        return even

print("2 is an", even(2), ' number')




def greaterNumber(a,b):

    if a > b:
        return "9 is greater than 3"
        

print(greaterNumber(9,3))

def lesserNumber(a,b):

    if a < b:
        return "3 is less than 9"

print(lesserNumber(3,9))


def elsa(a,b):

    if a > b:
        return "Value a is greater than b"
    else:
        return "Value b is greater than a"

print(elsa(3,9))


def nested(a):

    if a % 2 == 0:
        if a < 100:
            return "Value a is an even and a small number"
        else:
            return "Bye"

print(nested(50))


def nesting(a):

    if a < 100:
        a *= 2
        if a == 100:
            return "value a is 50 less than 100 then multiplied by 2 is 100"

print(nesting(50))


def elseIf(a):

    if a == "comsci":
        return "ez"
    elif a == "IT":
        return "ez pz"


print(elseIf("IT"))


def seniorCitizen(age):

    if age >= 60:
        return "Please retire"
    else:
        return "Keep working"

print(seniorCitizen(75))

def work(age, student):

    if age >= 18:
        if student == "Student":
            return "You are eligible for a part time job"
    else:
        return "you are not eligible to apply"

print(work(18, "Student"))

def hardworker(a):

    if a == "Yes":
        return "Unli durian!!!"
    else:
        return "No durian"

print(hardworker("Yes"))