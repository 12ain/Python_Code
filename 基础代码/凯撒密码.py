code = input("输入密文")
for p in code:
    if ord("a") <= ord(p) <=ord("z"):
        print(chr(ord("a")+(ord(p) - ord("a") - 3)%26),end = '')
    else:
        print(p, end = '')
