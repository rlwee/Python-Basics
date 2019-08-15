def even(test):
    if test%2 == 0:
        even = "even"
        odd = "odd"
        return even

test = 2
print(test,'is an',even(test), 'number')


def greater_number(greater,less):
    if greater > less:
        msg = f"{greater} is greater than {less}"
        return msg

greater = 9
less = 3
print(greater_number(greater,less))

def lesser_number(lesser,more):
        if lesser < more:
                msg = f"{lesser} is lesser than {more}"
                return msg

lesser = 3
more = 9
print(lesser_number(lesser,more))


def huge_number(huge):

    if huge > 500:
        msg_huge = f"{huge} is a huge number"
        return msg_huge
    else:
        msg_low = f"{huge} is not huge after all"
        return msg_low

huge = 1000
print(huge_number(huge))


def nested_identifying_number(number_value):
    msg_identified =f"{number_value} is an even number and a small number"
    if number_value % 2 == 0:
        if number_value < 100:
            return msg_identified
        else:
            return "Bye"

number_value = 50
print(nested_identifying_number(number_value))


def convert_to_even(number_convert):
    before_convert = number_convert
    number_convert *= 2
    msg_converted =f'{before_convert} is now {number_convert}.Any number multiplied by 2 will be even'
    if number_convert %2 == 0:
        return msg_converted

number_convert = 9
print(convert_to_even(number_convert))


def elseIf_courses(course):
    msg_cs=f'{course} is an ez course.'
    msg_IT=f'{course} is an ez pz course.'
    if course == "comsci":
        return msg_cs
    elif course == "IT":
        return msg_IT

course = 'comsci'
print(elseIf_courses(course))


def senior_citizen(age):
    msg_old =f'{age} is an old age! Please retire.'
    msg_young =f'{age} is young.Keep working'
    if age >= 60:
        return msg_old
    else:
        return msg_young

age = 70
print(senior_citizen(age))

def work_eligibility(status):
    if status == 'student':
        return 'You are eligible for a part time job.'
    if status == 'graduate':
        return 'Please apply for a fulltime job.'

status = 'graduate'
print(work_eligibility(status))

def hardworker(more):
    if  == "yes":
        return "Unli durian!!!"
    else:
        return "No durian"

more = 'yes'
print(hardworker(more))