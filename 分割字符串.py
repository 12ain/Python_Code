# months = "JanFebMarAprMayJunJulAugSepOctNovDec"
# n = input("请输入月份(1-12):")
# pos = (int(n)-1 )* 3
# monthAbbrev = months[pos:pos+3]
# print("月份简写是" + monthAbbrev+ ".")

import keyword
str=input("请输入变量名")
flag = 1
if (not (str[0]=='_'or'a'<=str[0]<='z'or'A'<=str[0]<='Z')):
    flag=0
if(flag==1):
    for i in str :
        if (not (str[0] == '_' or 'a' <= str[0] <= 'z' or 'A' <= str[0] <= 'Z'or'0' <= str[0] <= '9' )):
            flag = 0
if str in  keyword.kwlist:
    flag = 0
if(flag==1):
    print("输入正确")
else:
    print("输入错误")