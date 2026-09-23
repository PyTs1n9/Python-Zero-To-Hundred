import datetime
from calendar import weekday

date_str = input("请输入日期（如2026-09-10）：")

# date_obj = __________①__________
data_obj = datetime.datetime.strptime(date_str,format("%Y-%m-%d"))
# week = __________②__________
week = data_obj.weekday()
week_names = [
    "星期一", "星期二", "星期三",
    "星期四", "星期五", "星期六", "星期日"
]

# print("这一天是：", __________③__________)
print("这一天是：",week_names[week])