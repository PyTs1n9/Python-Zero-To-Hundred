import math

distance = 4.2
if 0 < distance <= 3:
	print("13")
else:
	print(f"{math.ceil(math.ceil(distance - 3) * 2.3 + 13)}")
