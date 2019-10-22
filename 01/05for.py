"""
for循环的使用和优化
使用break跳出循环时，可以配合else
for else用法：当迭代的对象迭代完并为空时，位于else的子句将执行，而如果在for循环中含有break时则直接终止循环，并不会执行else子句。
range表示在一个范围内
导入time标准库，使用当前时间，默认是秒
"""
#range(10)表示从0-9的整数
import time

for x in range(10):
    print(x)
print("---------------------")

#range(1,10)表示从1-9的整数
for x in range(1,10):
    print(x)
print("---------------------")

#range(1,10,2)表示从1-9步长为2的整数
for x in range(1,10,2):
    print(x)
print("---------------------")

#for-else用法
for x in range(5):
    if x == 2:
        print(x)
        # break
else:
    print("执行else....")
print("---------------------")

#循环嵌套99乘法表
for x in range(1,10):
    for y in range(1,10):
        print("{0}*{1}={2}".format(x,y,x*y),end="\t")
        if x <= y:
            print("\n")
            break
print("---------------------")

"""
循环的优化
1、尽量减少循环内部不必要的计算
2、嵌套循环中，尽量减少内层循环的计算，尽量向外提
3、局部变量查询较快，尽量使用局部变量
"""

start = time.time()#默认是秒
for x in range(1000):
    for y in range(10000):
        x*1000+y*100
print("未优化消耗时间：{0}秒".format(time.time()-start))

start = time.time()
for x in range(1000):
    c = x*1000 #减少内层计算！
    for y in range(10000):
        c+y*100
print("优化后消耗时间：{0}秒".format(time.time()-start))