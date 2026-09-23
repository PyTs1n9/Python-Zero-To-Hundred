import random
n = int(input())
random.seed(100)
for i in range(1,11):
    if i<10:
        print(random.randint(1,n), end='，')
    else:
        print(random.randint(1,n))