import os

# file_list = __________①__________
file_list = os.listdir()

count = 0

for filename in file_list:
    # if __________②__________:
    #     count = __________③__________
    if filename.endswith(".txt"):
        count+=1

print("txt文件数量：", count)