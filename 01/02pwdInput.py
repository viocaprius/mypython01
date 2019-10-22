"""
1、获取键盘输入使用input
2、获取密文输入，需要导入getpass标准库，但是这个功能在pycharm中不好用，需要在控制台测试
通过import导入
"""
import getpass

print("---普通方式---")
username = input("username:")
password = input("password:")
print("用户名：{0}，密码：{1}".format(username,password))

print("---密文方式---")
username1 = input("username:")
password1= getpass.getpass("password:")
print("用户名：{0}，密码：{1}".format(username1,password1))

