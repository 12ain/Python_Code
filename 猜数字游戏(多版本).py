# for i in range(1,6,2):
#     print(i)
# else:
#     print("完成")
#

# s, idx = "BIT",0
# while idx <len(s) :
#     print(s[idx])
#     idx += 1

# s = "python "
# while s != "":
#     for c in s :
#         print(c,end="")
#     s = s[:-1]
#

# s = "python"
# while s != "":
#     for c in s :
#         if c == "T":
#             break
#         print(c,end="")
#     s = s[:-1]


import random
# 0到100的10个整数
# print("{},{},{},{},{},{},{},{},{},{}".format(random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),))

# 0到100的奇数
# print("{}".format(random.randrange(1, 100, 2)))

# 随机选取4个字符
# s = "abcdefghij"
# a = random.randint(0,9)
# b = random.randint(0,9)
# c = random.randint(0,9)
# d = random.randint(0,9)
# print(s[a],s[b],s[c],s[d])
#


# 猜数字游戏(1)
# x = random.randint(0,9)
# print(x)
# i = eval(input("输入数字"))
# ci = 1
# f = 0
# while(f == 0):
#     if (i == x):
#         f = 1
#         print("恭喜用{}次猜对了".format(ci))
#     elif (i > x):
#         f = 0
#         ci += 1
#         print("输入太大了")
#         i = eval(input("输入数字"))
#     else:
#         f = 0
#         ci += 1
#         print("输入太小了")
#         i = eval(input("输入数字"))

# 猜数字游戏(2)
# x = random.randint(0,100)
# print(x)
# i = eval(input("输入数字"))
# ci = 1
# f = 0
# while(f == 0):
#     if (i == x):
#         f = 1
#         print("恭喜用{}次猜对了".format(ci))
#     elif (i > x):
#         f = 0
#         ci += 1
#         print("输入太大了")
#         i = eval(input("输入数字"))
#     else:
#         f = 0
#         ci += 1
#         print("输入太小了")
#         i = eval(input("输入数字"))

# 猜数字游戏(3)
x = random.randint(0,100)
print(x)
i = eval(input("输入数字"))
ci = 1
f = 0
while(f == 0):
    if (i == x):
        f = 1
        print("恭喜用{}次猜对了".format(ci))
    elif (i > x):
        f = 0
        ci += 1
        print("输入太大了")
        i = eval(input("输入数字"))
    else:
        f = 0
        ci += 1
        print("输入太小了")
        i = eval(input("输入数字"))

