import datetime

def show_time():
    time =  datetime.datetime.now()
    print("the time today is",time)

show_time()

def create_date(showtime):
    year = datetime.datetime(2019,10,19)
    if showtime is True:
        print(year)


showtime = True
create_date(showtime)

def show_month(timeI):
    print("today is month of ",timeI.strftime("%B"))


timeI = datetime.datetime(2019,8,19)
show_month(timeI)

def day_month(today):
    print("today is ",today.strftime("%A"))


today = datetime.datetime.now()
day_month(today)

def month_day(timeII):
    print("today is",timeII.strftime("%d"),"of",timeII.strftime("%B"))


timeII = datetime.datetime.now()
month_day(timeII)

def local_version(timelocal):
    print("the local time it",timelocal.strftime("%c"))


timelocal = datetime.datetime.now()
local_version(timelocal)

def another_example(birthdate):
    print("I was born on",birthdate.strftime("%B"),birthdate.strftime("%d"),birthdate.strftime("%Y"))


birthdate = datetime.datetime(1997,3,9)
another_example(birthdate)


def year_now(yearnow):
    print("the year today is",yearnow.strftime("%Y"))


yearnow = datetime.datetime.now()
year_now(yearnow)

def days_year(daysI):
    print("today is",daysI.strftime("%j"),"days out of","365 days")

daysI = datetime.datetime.now()
days_year(daysI)

def hour(hourI):
    print("time now is",hourI.strftime("%I"),hourI.strftime("%p"))


hourI = datetime.datetime.now()
hour(hourI)