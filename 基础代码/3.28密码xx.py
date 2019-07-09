import random
allList = list("qwertyuioplkjhgfdsazxcvbnm123456789QWERTYUIOPLKJHGFDSAZXCVBNM")
keyword = []
for j in range(10):
    for i in range(8):
        keyword.append(random.choice(allList))
    for t in keyword:
        print(t, end=' ')
    print("\n")
    keyword = []
