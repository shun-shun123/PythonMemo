import functions, json
day, month = functions.get_date()
year = functions.get_year()
print("今日は" + str(month) + "月" + str(day) + "日です。")

try:
    li = list()
    jsonData = functions.outputJson()
    for data in jsonData:
        if data['kadai']['subject'] == "ダミー":
            continue
        elif int (data['kadai']['deadline'] / 10000) >= year and month <= int (data['kadai']['deadline'] % 10000 / 100) and day <= int (data['kadai']['deadline'] % 10000 % 100):
            li.append(data)
    with open('data.json', 'w') as target:
        json.dump(li, target, indent=4)
    jsonData = functions.outputJson()
except Exception:
    dict = {
        'kadai': {
            'subject':"ダミー",
            'assignment':"00000",
            'deadline':00000,
            'state':"00000000",
            'dueTime':2460
        }
    }
    li = list()
    with open('data.json', 'r') as target:
        li.append(dict)
    with open('data.json', 'w') as target:
        json.dump(li, target, indent=4)
    jsonData = functions.outputJson()
    pass

print("\n~書き込み済みの課題一覧~")
for data in jsonData:
    print("教科名 : " + data['kadai']['subject'])
    print("課題名 : "  + data['kadai']['assignment'])
    functions.printout_deadline(data['kadai']['deadline'], data['kadai']['dueTime'])
    print("[詳細]\n" + data['kadai']['state'] + "\n")

while 1:
    command = int(input("コマンドを入力してください\n0: 終了\n1: 書き込み\n2: 教科名検索\n3: 締め切り順ソート\n"))
    jsonData = functions.outputJson()
    if command == 0:
        print("終了します")
        break
    elif command == 1:
        print("書き込み")
        subject = str(input("教科名を入力してください"))
        assignment = str(input("課題を入力してください"))
        deadline = int(input("締め切りを入力してください(yyyymmdd)"))
        # 入力されたdeadlineが正しい形式か確かめる
        if functions.check_date(deadline) is False:
            continue
        dueTime = int(input("締め切り時間を入力して下さい(hhmm)"))
        state = str(input("詳細を入力してください"))
        functions.inputJson(subject, assignment, deadline, state, dueTime)
    elif command == 2:
        print("教科名検索を行います")
        subject = str(input("教科名を入力してください"))
        for data in jsonData:
            if data['kadai']['subject'] == subject:
                print("\n課題名 : " + str(data['kadai']['assignment']))
                functions.printout_deadline(data['kadai']['deadline'], data['kadai']['dueTime'])
    elif command == 3:
        print("締め切り順ソート")
        jsonData = functions.outputJson()
        all_data = sorted(jsonData, key=lambda x:x['kadai']['deadline'])
        for data in all_data:
            if data['kadai']['subject'] == 'ダミー':
                continue
            print("\n教科名 : " + data['kadai']['subject'])
            print("課題名 : " + data['kadai']['assignment'])
            functions.printout_deadline(data['kadai']['deadline'], data['kadai']['dueTime'])
            print("[詳細]\n" + data['kadai']['state'])
    else:
        print("正しいコマンドを入力してください")
