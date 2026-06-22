'''school = '大学'

name = "张三"
print(school,name)'''

'''i = len("hello")
print(i)'''

#1.创建字符串
name = "张三"
age = 18

#2.拼接（+号）
info = "我叫" + name + ",今年"+str(age)+"岁"
info1 = f"我叫{name},今年{age}岁"
print(info,info1)

#3.字符串长度
s = "Hello World"
print(f"长度为{len(s)}")

#4.取字符（编号从0开始）
print(f"第一个字符为{s[0]}")
print(f"第7个字符为{s[6]}")

#5.切片[开始：结束]
print(f"前五个:{s[0:5]}")
print(f"后五个:{s[6:11]}")

#6.查找
pos = s.find("world")
print(f"world在第{pos}位")

#7.替换
new_s = s.replace("world","python")
print(new_s)

#8.分割
date = "2026,6,21"
parts= date.split(",")
print(parts)