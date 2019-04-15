# import numpy
# import matplotlib


# def pySum():
# 	a = [0, 1, 2, 3, 4]
# 	b = [9, 8, 7, 6, 5]
# 	c=[]
# 	for i in range(len(a)):
# 		c.append(a[i]**2 + b[i]**3)
# 	return c
# print(pySum())


#
# import numpy as np
# def nySum():
# 	a = np.array([0, 1, 2, 3, 4])
# 	b = np.array([9, 8, 7, 6, 5])
# 	c = a**2+b**3
# 	return c
# print(nySum())

 # 绘图区域
# import numpy as np
# import matplotlib.pyplot as plt
# plt.plot([3, 1, 4, 5, 2])
# plt.ylabel("Grade")
# plt.savefig('test',dpi = 600)
# plt.show()

# def f(t):
# 	return np.exp(-t) * np.cos(2 * np.pi * t)
# a = np.arange(0.0, 5.0, 0.02)
# plt.subplot(211)
# plt.plot(a, f(a))
#
# plt.subplot(2, 1, 2)
# plt.plot(a, np.cos(2 * np.pi * a), 'r--')
# plt.show()


# 中文显示
import numpy as np
import matplotlib.pyplot as plt