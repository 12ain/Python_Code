try:
    def isPrime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        i = 2
        while i < n:
            if(n % i == 0):
                return False
                i += 1
                break
            else:
                return True
    n = int(input("输入一个整数"))
    print(isPrime(n))
except ValueError:
    print("输入错误，请输入整数")