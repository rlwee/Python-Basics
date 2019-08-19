def dictionary(dictio):
    print("I am in year",dictio['Fourth year'],"in college")


dictio = {"First year":1,
          "Second year":2,
          "Third year":3,
          "Fourth year":4
          }

dictionary(dictio)

def get_dictionary(diction,getValue):
    print("one is ",diction.get("one"))

diction = {"one":1,
           "two":2,
           "three":3
          }

getValue = "one"
get_dictionary(diction,getValue)

def show_keys(keysdict):
    print("keys are: ")
    for index in keysdict:
        print(index,end= " ")

keysdict = {"four":4,
            "five":5,
            "six":6
           }

show_keys(keysdict)
print("")

def show_values(valuesdict):
    print("values in this dictionary are")
    for index in valuesdict:
        print(valuesdict[index],end=" ")


valuesdict = {"seven":7,
              "eight":8,
              "nine":9
             }

show_values(valuesdict)
print("")

def check_dicionary(checkdict,checkdictvalue):
    if checkdictvalue in checkdict:
        print(checkdictvalue,"is in the dictionary")
    else:
        print("not found!")
    


checkdict = {"ten":10,
             "eleven":11,
             "twelve":12
            }

checkdictvalue = "twelve"

check_dicionary(checkdict,checkdictvalue)


def change_dictionary(defaultdict,changeValue,changeKey):
    defaultdict[changeValue] = changeKey
    print("new value for",changeValue,"is",defaultdict[changeValue])


defaultdict = {"eleven":11,
               "twelve":12,
               "thirteen":13
              }

changeValue = "eleven"
changeKey = 11

change_dictionary(defaultdict,changeValue,changeKey)


def remove_element(removedict,removeKey):
    removedict.pop(removeKey)
    print("The dictionary is now ",removedict)


removedict = {"twenty": 20,
              "thirty": 30,
              "forty": 40
             }

removeKey = "twenty"

remove_element(removedict,removeKey)


def remove_last_item(lastdict,response):
    if response == "yes":
        lastdict.popitem()
        print("dicitonary is now",lastdict)
    else:
        print("dictionary is untouched")


lastdict = {"ten": 10,
            "twenty": 20,
            "thirty": 30
           }

response = "yes"
remove_last_item(lastdict,response)


def clear_dictionary(cleardict,clear):
    if clear == "yes":
        cleardict.clear()
        print("dictionary is now empty")
    else:
        print("dictionary untouched",cleardict)

cleardict = {"fourty":40,
             "fifty":50,
             "sixty":60
            }

clear = "yes"

clear_dictionary(cleardict,clear)

def copy_dict(firstdict,copy):
    if copy == "yes":
        seconddict = firstdict.copy()
        print("second duplicate dictionary is now ",seconddict)
    else:
        print("no duplicate dictionary made.")


firstdict = {"one hundred":100,
             "two hundred":200,
             "three hundred":30
            }

copy = "yes"

copy_dict(firstdict,copy)