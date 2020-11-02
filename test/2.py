def getNext(p):
    """
    p为模式串
    返回next数组，即部分匹配表
    """
    nex = [0] * (len(p) + 1)
    nex[0] = -1
    i = 0
    j = -1
    while i < len(p):
        if j == -1 or p[i] == p[j]:
            i += 1
            print(i)
            j += 1

            nex[i] = j  # 这是最大的不同：记录next[i]
        else:
            j = nex[j]

    return nex


r = getNext("ababac")
print(r)