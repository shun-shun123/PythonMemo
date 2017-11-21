from functions import get_date
day, month = get_date()
print("今日は" + str(month) + "月" + str(day) + "日です。")

fout = open("data.txt", "r")
print("\n~書き込み済みの課題一覧~")
print(fout.read())
fout.close()


dic_subject = {}

while 1:
    subject = str(input("教科名:"))
    assignment = str(input("課題名:"))
    deadline = int(input("締め切り(mmdd):"))
    dic_subject[subject] = assignment
    fout = open("data.txt", "a")
    fout.write(subject + " " + dic_subject[subject] + " " +str(deadline) )
    fout.write("\n")
    fout.close()
    process = int(input("0 for quit"))
    if process == 0:
        break