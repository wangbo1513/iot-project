'''students = {"张三":85,"李四":90,"王五":100}
print(students["王五"])'''

'''students = {
    "张三":85,
    "李四":90,
    "王五":95,
    "赵六":100
}
#1.查成绩
print(f"张三考了{students["张三"]}分")

#2.改成绩
students["张三"] = 88
print(f"张三考了{students["张三"]}分")

#3.加学生
students["钱七"] = 66
print("students")

#4.遍历所有学生
print("---全班成绩---")
for name, score in students.items():
    print(f"{name}:{score}分")

#5.算平均分
avg = sum(students.values())/len(students)
print(f"平均分:{avg:.2f}分")

#6.找出不及格的
print("---不及格---")
for name, score in students.items():
    if score < 80:
        print(f"{name}:{score}分")
'''

students = {"name":"张三",
            "age":20,
            "score": 85
            }
print(f"张三今年{students["age"]}岁，成绩为{students["score"]}分")
students["score"] = 90
students["school"] = "大学"
for key,value in students.items():
    print(f"{key}:{value}")