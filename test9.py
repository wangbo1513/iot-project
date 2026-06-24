'''f = open("data.txt","w",encoding="utf-8")

f.write("张三,85\n")
f.write("李四,90\n")

f.close

f = open("data.txt","r",encoding="utf-8")

content = f.read
print(content)
f.close'''

students = {
    "张三": 85,
    "李四": 90,
    "王五": 78,
}

# 1. 把字典存到文件（格式：姓名,成绩）
with open("scores.txt", "w", encoding="utf-8") as f:
    for name, score in students.items():
        f.write(f"{name},{score}\n")

# 2. 从文件读取，恢复成字典
new_students = {}
with open("scores.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()      # 去掉换行符
        name, score = line.split(",")  # 按逗号分割
        new_students[name] = int(score)  # 转整数

print(new_students)