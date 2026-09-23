# 考生文件夹下的 score.txt 文件记录了某班学生的学号、姓名和10门主干课程的成绩
#
# 请修改编辑器中的代码，完成以下功能：
# 读取 score.txt 文件，计算每位学生的总成绩。
# 按总成绩从高到低排序，筛选出前10名学生。
# 将前10名学生的学号、姓名及10门课程成绩写入文件 candidate0.txt，每行一个学生信息，格式与 score.txt 一致。


with open("score.txt", "r") as file:
	lines = file.readlines()
file.close()
S = []  # S中的元素是单个学生数据
L = []  # L中的元素是学生原始成绩和总成绩

for line in lines:
	S = line.split()
	score = 0
	for i in range(10):
		score += int(S[i + 2])
	S.append(score)
	L.append(S)
...  # 此处可多行

# 按学生总成绩从大到小排序
L.sort(key=lambda x: x[-1], reverse=True)

...  # 此处可多行
