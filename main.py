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
command = int(input('どの教科の課題を確認しますか？\n0:数学...'))
if command == 0:
    target = 'math'

for data in jsonData:
    if data['kadai1']['subject'] == target:
        print(data['kadai1']['deadline'])

# ここまで
###################################
while 1:
    subject = str(input("教科名:"))
    assignment = str(input("課題名:"))
    deadline = int(input("締め切り(mmdd):"))
    functions.inputJson(subject, assignment, deadline)
    process = int(input("0 for quit"))
    if process == 0:
        break
