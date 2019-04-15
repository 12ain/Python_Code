# 天天向上的力量
import math
dayup = math.pow((1.0 + 0.001),365)
daydowm = math.pow((1.0 - 0.001),365)
print("向上: {:.2f},向下: {:.2f} .".format(dayup,daydowm))