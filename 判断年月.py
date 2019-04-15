dat = input('请输入某年某月某日，格式为 yyyy-mm-dd ：')
y = int(dat[0:4])
m = int(dat[5:7])
d = int(dat[8:])
ly = False
if y%100 == 0:
    if y%400 == 0:
        ly = True
    else:
        ly = False
elif y%4 == 0:
    ly = True
else:
    ly = False
if ly == True:
    ms = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    ms = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 0
for i in range(1, 13):
    if i == m:
        for j in range(i-1):
            days += ms[j]
        print('%s是该年份的第%s天。' % (dat, (days + d))) #最后再加上“日”，即是答案