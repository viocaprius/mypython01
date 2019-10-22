"""
条件判断
1、if
2、if_else
3、if_elif_else
注意：字符串要转成数字比较
"""
myAge = 18
age = input("请输入你的年龄：")
print("---------------")

if myAge < int(age):
    print("你比我大。")
print("---------------")

if myAge < int(age):
    print("你比我大。")
else:
    print("你比我小。")
print("---------------")

if myAge < int(age):
    print("你比我大。")
elif myAge == int(age):
    print("你和我一样大。")
else:
    print("你比我小。")
print("---------------")