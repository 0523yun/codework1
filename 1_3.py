#列表保存一组成绩数据，统计不及格的人数和最高分
lst={89,45,23,1,98,33}
notpass=maxscore=0
for item in lst:
    if item > maxscore:
        maxscore=item
    if item < 60:
        notpass+=1
print("最高分是{}，不及格人数是{}".format(maxscore,notpass))