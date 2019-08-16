def get_name_index(name, letter):
    for index, lett in enumerate(name):
        if lett == letter:
            print(lett, ' found in ', index)



name = "russel"
letter = "e"
get_name_index(name, letter)


def count_letter_vowels(word,vowels):
    count = 0
    for letter in word:
        for vow in vowels:
            if letter == vow:
                count += 1
    if count == 1:
        print('only ',count,' vowel in ', word)
    elif count == 0:
        print('No vowels in ', word)
    else: print('There are ',count,' vowels in ', word)


word= "swiftkind"
vowels= "aeiou"
count_letter_vowels(word,vowels)

def count_letter_consonant(wordII,consonant):
    count = 0 
    for letter in wordII:
        for cons in consonant:
            if letter == cons:
                count += 1
    if count == 1:
        print('only ',count,' consonant in ', wordII)
    elif count == 0:
        print('No consonants in ', wordII)
    else: print('There are ',count,' consonants in ', wordII)

wordII = "swiftgood"
consonant = "bcdfghjklmnpqrstvwxyz"
count_letter_consonant(wordII,consonant)


def letter_by_letter(wordI):
    for index in wordI:
        print(index, end=" ")
    print("\n")

wordI= "Swiftkind"
letter_by_letter(wordI)


def loop_break(lists):
    for index in lists:
        if index == "Dom":
            break
        print(index, end=" ")
    print('\n')

Names = ["Russel", "Melch",
         "Dom", "Mary"
        ]
loop_break(Names)



def loop_continue(listII):
    for index in listII:
        if index == "Dom":
            continue
        print(index, end=" ")
    print("\n")

NamesII = ["Russel", "Melch",
           "Dom", "Ian"
          ]

loop_continue(NamesII) 



def loop_range(numI):
    for index in range(numI):
        print(index, end=" ")
    print("\n")

numI = 9
loop_range(numI)


def list_show(listI):
    for index in listI:
        print(index, end=" ")
    print("\n")

listI = ["Russel", "Melch",
    "Dom"]
list_show(listI)


def while_count(valueI,countI):
    while countI < valueI:
        print(countI,"is less than ",valueI)
        countI += 1
    else:
        print(countI,"is equal to ",valueI)

countI = 0
valueI = 5
while_count(valueI,countI)

print('\n')
def while_count_decrease(valueII,countII):
    while countII > valueII:
        countII -= 1
        if countII > valueII:
            print(countII,' is greater than ',valueII)
        elif countII <valueII: 
            print(countII,' is less than ',valueII)
        if countII == valueII:
            print(countII,' is equal to ',valueII)

countII =5
valueII =0
while_count_decrease(valueII,countII)



def show_lists(name):
    for index in name:
        print(index)


name = ["russel","lacorte","wee"]
show_lists(name)