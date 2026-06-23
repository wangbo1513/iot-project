'''def say_hello():
    print("Hello!")

say_hello()
'''

'''def greet(name):
    print(f"Hello,{name}!")

greet("张三")
greet("李四")
'''

'''def add(a,b):
    return a + b

result = add(3,5)
print(result)
'''

def print_student(student):
    print(f"{student["name"]}今年{student["age"]}岁")
    print(f"成绩是{student["score"]}")

s = {"name":"张三","age":20,"score":90}
print_student(s)