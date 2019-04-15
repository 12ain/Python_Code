# 带刷新进度条
# import time
# scale = 50
# print("执行开始".center(scale//2, '-'))
# t = time.clock()
# for i in range(scale+1):
#     a = '*' * i
#     b = '.' * (scale - i)
#     c = (i/scale)*100
#     t = time.clock()
#     print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, t), end="")
#     time.sleep(0.05)
# print("\n"+"执行结束".center(scale//2, "-"))

# 最简单进度
import time
print("Starting...")
for i in range(101):
    print("\r{:3}%".format(i), end="")
    time.sleep(0.05)
print("Done!")


# 带刷新进度条
# import time
# scale = 50
# print("执行开始".center(scale//2,"-"))
# start = time.perf_counter()
# for i in range(scale+1):
#     a = '*' * i
#     b = '.' * (scale-i)
#     c = (i/scale)*100
#     dur = time.perf_counter() - start
#     print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end=' ')
#     time.sleep(0.05)
# print("\n"+"执行结束".center(scale//2,'-'))

