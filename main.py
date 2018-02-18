# coding:UTF-8
# functions: 自作関数(functions.pyからインポート)
# Json: Jsonデータを扱うためのモジュール
# colorama: 出力文字色を変更するためのモジュール
import functions, json
import colorama
from colorama import Fore, Back, Style

# day, month, year に、当日の日付を代入
day, month = functions.get_date()
year = functions.get_year()
print("今日は" + str(month) + "月" + str(day) + "日です。")

# 既存のdata.jsonファイルからデータを読み込む
# try-exceptで例外処理
# data.jsonが空の場合(初回使用向け),エラーを防ぐために、ダミーデータを書き込む
try:
    li = list()
    jsonData = functions.outputJson()
    for data in jsonData:
        # dataからそれぞれの締切日を計算する
        data_year = int(data['kadai']['deadline'] / 10000)
        data_month = int(data['kadai']['deadline'] % 10000 / 100)
        data_day = int(data['kadai']['deadline'] % 10000 % 100)
        # ダミーデータを追加する
        if data['kadai']['subject'] == "ダミー":
            li.append(data)
            continue
        # data_year, data_month, data_day から締切日を過ぎているか判断
        if data_year > year:
            li.append(data)
            continue
        if data_year == year and data_month >= month:
            li.append(data)
            continue
        if data_year == year and data_month == month and data_day >= day:
            li.append(data)
            continue
    with open('data.json', 'w') as target:
        json.dump(li, target, indent=4)
    jsonData = functions.outputJson()
except Exception:
    # ダミーデータを作成
    print("ダミーデータ作成")
    dict = {
        'kadai': {
            'subject':"ダミー",
            'assignment':"00000",
            'deadline':00000,
            'detail':"00000000",
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
# 締め切り日当日のものだけ出力する
print("\n締め切り日当日です!!")
for data in jsonData:
    if data['kadai']['deadline'] == (year * 10000 + 100*month + day):
        print(Fore.GREEN + "教科名 : " + data['kadai']['subject'])
        print("課題名 : " + data['kadai']['assignment'])
        functions.printout_deadline(data['kadai']['deadline'], data['kadai']['dueTime'])
        print("[詳細]\n" + data['kadai']['detail'] + "\n" + Fore.WHITE)
# メイン処理
while 1:
    command = int(input("コマンドを入力してください\n0: 終了\n1: 書き込み\n2: 教科名検索\n3: 締め切り順ソート\n") )
    jsonData = functions.outputJson()
    # プログラムを終了する場合
    if command == 0:
        print("終了します")
        break
    # データベースに書き込む場合
    elif command == 1:
        print(Fore.CYAN + "書き込み")
        subject = str(input("教科名を入力してください"))
        assignment = str(input("課題を入力してください"))
        deadline = int(input("締め切りを入力してください(yyyymmdd)"))
        # 入力されたdeadlineが正しい形式か確かめる
        if functions.check_date(deadline) is False:
            continue
        dueTime = int(input("締め切り時間を入力して下さい(hhmm)"))
        detail = str(input("詳細を入力してください" + Fore.WHITE))
        functions.inputJson(subject, assignment, deadline, detail, dueTime)
    # 教科名検索を行う場合
    elif command == 2:
        print("教科名検索を行います")
        subject = str(input("教科名を入力してください"))
        for data in jsonData:
            if data['kadai']['subject'] == subject:
                print(Fore.GREEN + "\n課題名 : " + str(data['kadai']['assignment']))
                functions.printout_deadline(data['kadai']['deadline'], data['kadai']['dueTime'])
                print("[詳細]\n" + str(data['kadai']['detail']) + Fore.WHITE)
    # 締め切り順にソートする場合
    elif command == 3:
        print("締め切り順ソート")
        jsonData = functions.outputJson()
        all_data = sorted(jsonData, key=lambda x:x['kadai']['deadline'])
        for data in all_data:
            if data['kadai']['subject'] == 'ダミー':
                continue
            print(Fore.MAGENTA + "\n教科名 : " + data['kadai']['subject'])
            print("課題名 : " + data['kadai']['assignment'])
            functions.printout_deadline(data['kadai']['deadline'], data['kadai']['dueTime'])
            print("[詳細]\n" + data['kadai']['detail'] + Fore.WHITE)
    # 不正なコマンドが入力された場合
    else:
        print(Fore.RED + "正しいコマンドを入力してください" + Fore.WHITE)
