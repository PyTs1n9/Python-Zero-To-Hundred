seconds = 3661

hour = seconds // 3600
minute = seconds % 3600 // 60
second = seconds % 3600 % 60
print((hour, minute, second))
