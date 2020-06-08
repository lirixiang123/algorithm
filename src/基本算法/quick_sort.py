"""
快速排序是基于分治法的一种排序算法
空间复杂度： 最坏情况下为 O(n)    平均栈深度为 O(log2n)
时间复杂度： O(nlog2n)
快速排序是所有内部排序算法中平均性能最优的一种排序算法
"""

def quick_sort(ll, low, high):
    """
    :param ll: 列表
    :param low: 最小索引
    :param high: 最大索引
    :return: 列表
    """
    if low < high:
        point = ll[low]
        i = low
        j = high
        while i < j:
            while i < j and ll[j] >= point:
                j -= 1
            ll[i], ll[j] = ll[j], ll[i]
            while i < j and ll[i] <= point:
                i += 1
            ll[j], ll[i] = ll[i], ll[j]
        ll[i] = point
        quick_sort(ll, low, i-1)
        quick_sort(ll, i+1, high)


ll = [10, 5, 1, 4, 14, 85, 21, 7, 15, 5, 48, 48, 46, 88, 84, 254, 8498, 4984, 5, 51651, 651, 6516, 156, 1651, 651, 61,
      61, 651, 651, 65]
n = len(ll)
quick_sort(ll, 0, n-1)
print(ll)

