"""
快速排序是基于分治法的一种排序算法
空间复杂度： 最坏情况下为 O(n)    平均栈深度为 O(log2n)
时间复杂度： O(nlog2n)
快速排序是所有内部排序算法中平均性能最优的一种排序算法
"""

def quick_sort(A,p,r,k):
    """
    :param ll: 列表
    :param low: 最小索引
    :param high: 最大索引
    :return: 列表
    """


    def partition(A, p, r):
        pivot = A[r]
        i = p
        for j in range(p, r):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                i = i + 1
        A[i], A[r] = A[r], A[i]
        return i


    q =  partition(A, p, r)
    if q - p == k - 1:
        return A[q]
    elif q - p> k - 1:
        return quick_sort(A,p,q - 1,k)
    else:
        return quick_sort(A,q + 1,r,k-1-(q-p))


ll = [10, 5, 1, 4, 14, 85, 21, 7, 15, 5, 48, 48, 46, 88, 84, 254, 8498, 4984, 5, 51651, 651, 6516, 156, 1651, 651, 61,
      61, 651, 651, 65]
res = quick_sort(ll, 0, len(ll)-1,3)
print(ll)
print(res)
