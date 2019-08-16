def index_in_an_index(inTuple):
    for index in inTuple:
        print("\n")
        for ind in index:
            print(ind,end=" ")

inTuple = ((1,2,3),(4,5,6),
          (7,8,9)
          )

index_in_an_index(inTuple)
print("\n")


def show_picked_element(pickNumIndex,TupleIII):
    print(TupleIII[pickNumIndex])


TupleIII = (10,20,
            30,40,
            50,60,
            70,80,
            90)

pickNumIndex = 2

show_picked_element(pickNumIndex,TupleIII)


def largest_value_in_element(TupleIV):
    print("largest number in the tuple is",max(TupleIV))

TupleIV = (10,20,
            30,40,
            50,60,
            100,70,
            80,90)

largest_value_in_element(TupleIV)

def show_tuple(tuple_name):
    for index in tuple_name:
        print(index,end=" ")

tuple_name = ("Russel","Lacorte",
              "Wee")

show_tuple(tuple_name)
print("\n")


def pick_in_tuple(lists,choicenumberindex):
    print("the",choicenumberindex,"index in the tuple is",tuples[choicenumberindex])

tuples = ("one","two",
          "three")

choicenumberindex = 2
pick_in_tuple(tuples,choicenumberindex)

def select_letter_index_of_each_word(tuplesI,choicenumberindexI):
    print("The",choicenumberindexI,"index letter for each word are: ")
    for index in tuplesI:
        print(index[choicenumberindexI],end=" ")

tuplesI = ("one","two",
           "three","four",
           "five")

choicenumberindexI = 0
select_letter_index_of_each_word(tuplesI,choicenumberindexI)
print("\n")

def tuples_same_values(valueTuples,sameValues):
    count = 0
    for index in valueTuples:
        if index == sameValues:
            count += 1
    if count > 0:
        print(sameValues,"is multiple in this list")

valueTuples = ("one","two",
               "three","four",
               "five","one")

sameValues = "one"
tuples_same_values(valueTuples,sameValues)


def index_position(positionTuple,searchWord):
    indexs = positionTuple.index(searchWord)
    for index in positionTuple:
        if index == searchWord:
            print(searchWord,"is in index",indexs)

positionTuple = ("five","four",
                 "three","two",
                 "one")

searchWord = "four"
index_position(positionTuple,searchWord)

def index_not_present(valueTupleI,searchWordI):
    count = len(valueTupleI)
    for index in valueTupleI:
        if index != searchWordI:
            count -= 1
    if count == 0:
        print(searchWordI,"is not found in the list.")

valueTupleI = ("two","three",
               "four","five")

searchWordI = "six"
index_not_present(valueTupleI,searchWordI)


def index_present(valueTupleII,searchWordII):
    count = 0
    for index in valueTupleII:
        if index == searchWordII:
            count += 1
    if count > 0:
        print(searchWordII,"is found in the list.")

valueTupleII = ("isa","dalawa",
                "tatlo")

searchWordII = "isa"
index_present(valueTupleII,searchWordII)