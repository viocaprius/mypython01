"""
1、while循环
2、break跳出循环
3、continue跳出此次循环，执行下一次循环
"""
age = 18
count = 1

"""
print("----------无限猜年龄-----------")
while True:
    age = input("请输入年龄：")
    print("你输入的是{0}".format(age))
"""

"""
print("----------猜年龄,猜对了结束-----------")
_age = int(input("请输入年龄："))
while age != _age:
    print("猜错了。")
    _age = int(input("请输入年龄："))
print("猜对了，结束。")
"""

"""
print("----------猜年龄,猜对了结束，注意input的位置-----------")
while age != int(input("请输入年龄：")):
    print("猜错了。")
print("猜对了，结束。")
"""


"""
print("----------猜年龄,猜3次退出，但是最后一句有bug-----------")
count = 1
while age != int(input("请输入年龄：")):
    print("第{0}次猜错了。".format(count))
    count += 1
    if count > 3:
        print("3次机会结束。")
        break
print("猜对了，结束。")
"""

"""
print("----------猜年龄,猜3次退出，使用else修改最后一句的bug-----------")
while age != int(input("请输入年龄：")):
    print("第{0}次猜错了。".format(count))
    count += 1
    if count > 3:
        print("3次机会结束。")
        break
else:
    print("猜对了，结束。")
#else表示当while条件不成立时，执行
"""


print("----------猜年龄,猜3次退出，输入yes可以继续-----------")
while age != int(input("请输入年龄：")):
    print("第{0}次猜错了。".format(count))
    count += 1
    if count > 3:
        print("3次机会结束。")
        aging = input("输入yes继续")
        if "yes" == aging:
            count = 1
            continue
        else:
            print("输入错误，结束。")
            break
else:
    print("猜对了，结束。")