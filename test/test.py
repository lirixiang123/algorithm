
def f(n):
    print(n)
    if n == 0:
        return 1
    if n== 2:
        return 2
    n = f(n - 1)



l = f(7)
