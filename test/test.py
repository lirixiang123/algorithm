d = {
    "a":1,
    "b":2,
    "c":3,
}
b = [1,2,3,4,5,6]

dp = [[False for _ in range(3)] for _ in range(4)]
dp.pop()
print(dp.pop())
print(246&1)

def f(n):
    if n == 0:
        return None

    return f(n-1)


def getDigitSum(self, number):
        sum_ = 0
        for i in str(number):
            sum_ += int(i)
        return sum_


print(list(map(int, str(12) + str(24))))