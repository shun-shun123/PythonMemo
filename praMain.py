import functions
day, month = functions.get_date()
print("今日は" + str(month) + "月" + str(day) + "日です。")

print("\n~書き込み済みの課題一覧~")
try:
    jsonData = functions.outputJson()
except Exception:
    pass
####################################
# ここから
# listとdictionaryでgetしたJsonを簡単に扱ってみた
# お試し程度なので、参考ほどに、
# try_command = int(input('どの教科の課題を確認しますか？\n0:数学...'))
# if command == 0:
#     target = 'math'

# for data in jsonData:
#     if data['kadai1']['subject'] == target:
#         print(data['kadai1']['deadline'])

# ここまで
###################################
while 1:
    command = int(input('0: quit\n1: search\n2: write\n'))
    if command == 0:
        break
    elif command == 1:
        branch = int(input('教科名での検索なら1,締め切りでの検索なら2 : '))
        if branch == 1:
            name_subject = str(input('教科名 : '))
            for name in jsonData:
                if name['kadai1']['subject'] == name_subject:
                    print(name)
        elif branch == 2:
            name_deadline = int(input('締め切り : '))
            for name in jsonData:
                if name['kadai1']['deadline'] == name_deadline:
                    print(name)
    elif command == 2:
        subject = str(input('教科名 : '))
        assignment = str(input('課題名 : '))
        deadline = int(input('締め切り : '))
        functions.inputJson(subject, assignment, deadline)
