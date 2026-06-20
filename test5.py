"""score = [85,90,78,70,66]
print("第一个：",score[0])
print("第二个：",score[1])
print("最后一个：",score[-1])
print("倒数第二个：",score[-2])
print("第3个：",score[0:3])
print("第2到第4个：",score[1:4])

scores= [85,90,78,70,66]
#修改
scores[0] = 95
print(scores)
#增加
scores.append(100)
print(scores)

scores.insert(0,60)    #位置0插入60
print(scores)

#删除
scores.remove(90)    #删除90
print(scores)

popped = scores.pop(0)    #删除位置0，返回删除的值
print("删除的：",popped)
print(scores)"""


"""scores = [85, 90, 78, 92, 88]
#方法1：for循环
for score in scores:
    print(score)

#放法2：带索引
for i in range(len(scores)):
    print(f"第{i+1}个:{scores[i]}")

#方法3：同时要索引和值
for i, score in enumerate(scores):
    print(f"索引{i}，值{score}")"""

scores = [85, 90, 78, 92, 88]
print(scores[0]) 
print(scores[-1])

#加一个新成绩
scores.append(95)
print(scores)

#算平均分
total = sum(scores)
count = len(scores)
avg = total/count
print(f"平均分是{avg}")