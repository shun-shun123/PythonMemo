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
    command = int(input("コマンドを入力してください\n0: 終了\n1: 書き込み\n2: 教科名検索\n3: 締め切り順ソート\n4: 消去\n"))
    if command == 0:
        print("終了します")
        break
    elif command == 1:
        print("書き込み")
        subject = str(input("教科名を入力してください"))
        assignment = str(input("課題を入力してください"))
        deadline = int(input("締め切りを入力してください"))
        state = int(input("状態を入力してください"))
        functions.inputJson(subject, assignment, deadline, state)
    elif command == 2:
        print("教科名検索を行います")
        subject = str(input("教科名を入力してください"))
        for data in jsonData:
            if data['kadai1']['subject'] == subject:
                assignment = data['kadai1']['assignment']
                deadline = data['kadai1']['deadline']
                print("\n課題名 : " + assignment)
                print("締め切り : " + str(deadline))
    elif command == 3:
        print("締め切り順ソート")
        all_data = sorted(jsonData, key=lambda x:x['kadai1']['deadline'])
        for data in all_data:
            print("\n教科名 : " + data['kadai1']['subject'])
            print("課題名 : " + data['kadai1']['assignment'])
            print("締め切り : " + str(data['kadai1']['deadline']))
    elif command == 4:
        print("消去")
    else:
        print("正しいコマンドを入力してください")
