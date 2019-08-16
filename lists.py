def show_list(name):
    for index in name:
        print(index, end=" ")

name = ["russel","lacorte",
        "Wee"
       ]

show_list(name)
print("\n")


def pick_in_list(lists,choicenumberindex):
    print("the",choicenumberindex,"index in the list is",lists[choicenumberindex])


lists = ["one","two",
         "three"
        ]

choicenumberindex = 0
pick_in_list(lists,choicenumberindex)


def select_letter_of_each_word(listI,choicenumberindexI):
    print("The",choicenumberindexI,"index letter for each word are: \b")
    for index in listI:
        print(index[choicenumberindexI],end=" ")

listI = ["one","two",
         "three","four",
         "five"
        ]

choicenumberindexI = 0

select_letter_of_each_word(listI,choicenumberindexI)
print("\n")


def append_list(before,toAdd):
    before.append(toAdd)
    print("list updated is now ",before)


before= ["swift"]
toAdd= "kind"
append_list(before,toAdd)

def add_list(emptyList,addtxt):
    emptyList.append(addtxt)
    print("the list now contains ",emptyList)

emptyList = []
addtxt = "first"
add_list(emptyList,addtxt)

def list_same_values(valueList,sameValues):
    count = 0
    for index in valueList:
        if index == sameValues:
            count += 1
    if count > 0:
        print(sameValues,"is multiple in this list")

valueList = ["one","two",
             "three","four",
             "five","one"]

sameValues = "one"
list_same_values(valueList,sameValues)

def index_position(positionList,searchWord):
    indexs = positionList.index(searchWord)
    for index in positionList:
        if index == searchWord:
            print(searchWord,"is in index",indexs)

positionList = ["five","four",
                "three","two",
                "one"]

searchWord = "four"
index_position(positionList,searchWord)

def index_not_present(valueListI,searchWordI):
    count = len(valueListI)
    for index in valueListI:
        if index != searchWordI:
            count -= 1
    if count == 0:
        print(searchWordI,"is not found in the list.")

valueListI = ["two","three",
              "four","five"]

searchWordI = "six"
index_not_present(valueListI,searchWordI)


def index_present(valueListII,searchWordII):
    count = 0
    for index in valueListII:
        if index == searchWordII:
            count += 1
    if count > 0:
        print(searchWordII,"is found in the list.")


valueListII = ["isa","dalawa",
               "tatlo"]

searchWordII = "isa"
index_present(valueListII,searchWordII)


def remove_element(listRemove,numRemove):
    listRemove.remove(numRemove)
    print("The new list will be ",listRemove)


listRemove = [100,200,300,400,500]
numRemove = 500
remove_element(listRemove,numRemove)