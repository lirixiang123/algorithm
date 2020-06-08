def merge_sort(alist):
    n = len(alist)
    if n<=1:
        return alist
    mid = n//2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    left_p, right_p = 0,0
    result = []
    while left_p < len(left) and right_p < len(right):

        if left[left_p]<right[right_p]:
            result.append(left[left_p])
            left_p += 1
        else:
            result.append(right[right_p])
            right_p += 1

    result += left[left_p:]
    result += right[right_p:]
    return result

