# txt = open('new.txt', 'rt')
# print(txt.readline())
# txt.close()
# binFile = open('new.txt', 'rb')
# print(binFile.readline())
# binFile.close()


# 实例7.3
fname = input("请输入要写入的文件: ")
fo = open(fname, "w+")
ls = ["唐诗", "宋词", "元曲", "hello", "world"]
fo.writelines(ls)
for line in fo:
    print(line)
fo.close()


