str=input("请输入变量名")
flag = 1
if (not (str[0]=='_'or'a'<=str[0]<='z'or'A'<=str[0]<='Z')):#判断首字符
    flag=0
if(flag==1):
    for i in str :
        if (not (str[0] == '_' or 'a' <= str[0] <= 'z' or 'A' <= str[0] <= 'Z'or'0' <= str[0] <= '9' )):
            flag = 0
if str in ["False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda","nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"]:
    flag = 0
if(flag==1):
    print("yes")
else:
    print("no")
