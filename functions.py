import json, datetime, math

# parameter
# subject: str // 教科名
# assignment: str // 課題名
# deadline: int // 提出期限
# function: input Jsondata to data.json file
def inputJson(subject, assignment, deadline, state, dueTime):
    dict = {
        'kadai':{
            'subject':subject,
            'assignment':assignment,
            'deadline':deadline,
            'state':state,
            'dueTime': dueTime
        }
    }
    li = list()
    with open('data.json', 'r') as target:
        li = json.load(target)
        li.append(dict)
    with open('data.json', 'w') as target:
        json.dump(li, target, indent=4)


# function: read json file and write the data into jsonData
def outputJson():
    f = open('data.json', 'r')
    jsonData = json.load(f)
    # print(jsonData)
    f.close()
    return jsonData

# function: return day, month in order
def get_date():
    day = datetime.date.today().day
    month = datetime.date.today().month
    return day, month

# function: return year
def get_year():
    year = datetime.date.today().year
    return year

def check_date(date):
    year = int (date / 10000)
    if(year % 400 == 0):
        leapyear = True
    elif(year % 100 == 0):
        leapyear = False
    elif(year % 4 == 0):
        leapyear = True
    else :
        leapyear = False
    mmdd = date % 10000
    day = mmdd % 100
    month = int (mmdd / 100)
    if month < 1 or month >= 13:
        print("正しい月を入力して下さい\n")
        return False
    elif month == 1 or month ==  3 or month == 5 or month ==  7 or month == 8 or month == 10 or month == 12:
        if day < 1 or day > 31:
            print("正しい日を入力して下さい\n")
            return False
    elif month == 4 or month == 6 or month == 9 or month ==11:
        if day < 1 or day > 30:
            print("正しい日を入力して下さい\n")
            return False
    elif month == 2:
        if leapyear:
            if day < 1 or day > 29:
                print("(閏年です)正しい日を入力して下さい\n")
                return False
        else:
            if day < 1 or day > 28:
                print("(閏年ではありません)正しい日を入力して下さい\n")
                return False
    return True

# parameter 
# deadline: yyyymmdd == Integer
# dueTime: dueTime == String
# function: print out deadline in an arrangemnt
def printout_deadline(deadline, dueTime):
    year = int (deadline / 10000)
    month = int (deadline % 10000 / 100)
    day = int (deadline % 10000 % 100)
    hour = int (dueTime / 100)
    minute = int (dueTime % 100)
    print("締め切り日 : " + str(year) + " / " + str(month) + " / " + str(day))
    print("締め切り時間 : " + "{0:02d}".format(hour) + ":" + "{0:02d}".format(minute))