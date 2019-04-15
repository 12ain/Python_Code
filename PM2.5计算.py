p = eval(input("输入当前pm2.5的值"))
if 0 <= p < 35 :
    print("空气优质,非常适合户外运动哦")
elif 35 <= p <75:
    print("空气良好,适合户外活动！")
else:
    print("空气污染严重,请小心哦")
