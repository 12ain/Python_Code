num = "ab2b3n5n2n67mm4n2"
num1 = []
sum = 0
for i in range(17):
    if(num[i] == "n"):
        sum += 1
    if(num[i].isnumeric() == 1):
            num1.append(num[i])
print("字母n的个数为:",sum)
print("".join(num1))
