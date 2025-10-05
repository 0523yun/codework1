file=open("score.txt", "r", encoding='utf-8')
s1=file.read()
file.close()
lst=s1.split(",")
lst2=[]
for item in lst:
    lst2.append(eval(item))
notpass=maxscore=0
for item in lst2:
    if item > maxscore:
        maxscore=item
    if item < 60:
        notpass+=1
print("最高分是{},不及格人数是{}".format(maxscore,notpass))