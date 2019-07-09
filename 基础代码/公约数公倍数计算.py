num1, num2 =eval(input("请输入两个整数，以逗号隔开："))
num1 = int(num1)
num2 = int(num2)
if num1 > num2:
    smaller = num2
else:
    smaller = num1
for i in range(1, smaller+1):
    if(num1 % i == 0 and num2 % i == 0):
        yue = i
bei = num1 * num2 / yue
print("两个整数的最大公约数为：{}，最大公倍数为：{}。".format(yue,bei))
