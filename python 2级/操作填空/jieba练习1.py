import jieba

with open("data.txt", "r") as file:
	txt = file.read()
words = jieba.__lcut(txt)
d = {}
for word in words:
	if len(word) >= 2:
		d[word] = d.get(word, 0) + 1
items = list(d.items())
items.sort(key=lambda x:[1],reverse=True)
for i in range(10):
	word,count = items[i]
	print("{}:{}".format(word,count))