def multi(*n):
    sum = 1
    for i in n:
        sum *= i
    return sum
print(multi(5,6,7))