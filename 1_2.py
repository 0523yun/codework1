#用海伦公式计算三角形面积，判断是否构成三角形的条件
import math
try:
    a = eval(input("请输入a边长："))
    b = eval(input("请输入b边长："))
    c = eval(input("请输入c边长："))
    if a < 0 or b < 0 or c < 0:
        print("输入数据不可为负数")
    elif a + b <= c or c + b <= a or b + c <= a:
        print("不符合两边之和大于第三边原则")
    else:
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("三角形的面积是{:.2f}".format(S))
except NameError:
    print("请输入正整数")
