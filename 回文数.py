n = input("请输入1个5位数字:")
if n[0] == n[-1]and n[1] == n[-2]:
    print("{}是一个回文数".format(n))
else:
    print("{}不是一个回文数".format(n))
