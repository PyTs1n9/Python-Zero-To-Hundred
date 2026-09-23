import statistics
from statistics import stdev

scores = []

for i in range(5):
    score = float(input("请输入成绩："))
    scores.append(score)
#
# average = __________②__________
average = statistics.mean(scores)
# middle = __________③__________
middle = statistics.median(scores)
# deviation = __________④__________
deviation = statistics.stdev(scores)

print("平均分：{:.1f}".format(average))
print("中位数：{:.1f}".format(middle))
print("标准差：{:.1f}".format(deviation))