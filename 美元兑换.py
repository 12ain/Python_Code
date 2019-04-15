#美元与人民币双向兑换程序
hui = input("请输入当前汇率")
TempStr = input("请输入你要兑换的货币数量和种类(m或r)")
if TempStr[-1] in ['r','R']:
    rmb = (eval(TempStr[0:-1])) / eval(hui)
    print("相应的美元数量为:",rmb,"美元")
if TempStr[-1] in ['m','M']:
    dollar = (eval(TempStr[0:-1])) * eval(hui)
    print("相应的人民币数量为:",dollar,"元")