def string(txt):
    print(txt,"is a beautiful word.")

txt = "swiftkind"
string(txt)

def values_in_strings(txtI,picktxt):
    print(picktxt)

txtI = "samsung"
picktxt = txtI[0:3]
values_in_strings(txtI,picktxt)

def update_string(txtII,changeTo):
    first = txtII[:8]
    second = txtII[8:12]
    second = changeTo
    print(first,second)

txtII = "swift is kind"
changeTo = "good"
update_string(txtII,changeTo)

def concatinate_string(sentence,addSent):
    print(sentence,addSent)

sentence = "I want to"
addSent = "workout"
concatinate_string(sentence,addSent)

def string_length(txtIII):
    print("there are",len(txtIII),"letters in",txtIII)

txtIII = "random"
string_length(txtIII)

def convert_all_to_lowercase(uppercase):
    print(uppercase.lower())

uppercase = "PYTHON"
convert_all_to_lowercase(uppercase)

def convert_all_to_uppercase(lowercase):
    print(lowercase.upper())

lowercase = "python"
convert_all_to_uppercase(lowercase)

def identifying_lower_case(placetext):
    if placetext.islower():
        print(placetext,"text is in lower case.")
    else:
        print(placetext,"text is in uppercase or atleast one letter is in upper case.")

placetext = "helloworld"
identifying_lower_case(placetext)

def identifying_upper_case(placetextII):
    if placetextII.isupper():
        print(placetextII,"text is in uppercase.")
    else:
        print(placetextII,"text is in lowercase or atleast one letter is in lowercase.")

placetextII = "HELLOWORLD"
identifying_upper_case(placetextII)

def int_to_string(integer):
    print(integer,"integer becomes",str(integer),"string")

integer = 99
int_to_string(integer)