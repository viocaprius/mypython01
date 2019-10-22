"""
1、注释的说明
2、字符串的格式化输出
"""
#代表单行注释

'''
三个引号代表多行注释
'''

"""
三个双引号同样代表多行注释，但是还可以赋值给变量表示字符串
"""
name = "悟空"
age = "1000"
job = "IT"

#1、加号拼接法
info1 = """
------info1------
name:""" + name + """
age:""" + age + """
job:""" + job + """
"""
print(info1)

#2、%占位符方式，%s表示字符串，%d表示整数，%f表示浮点数
info2 = """
------info2------
name:%s
age:%s
job:%s
"""%(name,age,job)
print(info2)

#3、format的key/value方式
info3 = """
------info3------
name:{_name}
age:{_age}
job:{_job}
""".format(_name = name,_age = age,_job = job)
print(info3)

#4、format顺序变量方式
info4 = """
------info4------
name:{0}
age:{1}
job:{2}
""".format(name,age,job)
print(info4)