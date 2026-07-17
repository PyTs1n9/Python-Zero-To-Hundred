list = []
for i in range(1,10,1):
	arr = []
	for j in range(1,i+1,1):
		arr.append(f"{j}*{i}={i*j}")
	list.append((" ").join(arr))
print(list)