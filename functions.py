import json, datetime

# parameter
# subject: str // 教科名
# assignment: str // 課題名
# deadline: int // 提出期限
# function: input Jsondata to data.json file
def inputJson(subject, assignment, deadline, state):
    dict = {
        'kadai1':{
            'subject':subject,
            'assignment':assignment,
            'deadline':deadline,
            'state':state
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

# parameter:
# date: date type (mmdd)
# return -> day, month
def parse_date(date):
    day = date % 100
    month = date / 100
    return day, month