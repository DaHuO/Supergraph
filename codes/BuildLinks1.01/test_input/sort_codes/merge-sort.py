
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
            if left[i] > right[j]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1
    result += left[i:]
    result += right[j:]
    return result

def mergeSort(u):
    if len(u) < 2:
        return u

    left = []
    right = []
    middle = len(u) // 2

    left = u[:middle]
    right = u[middle:]
    return merge(mergeSort(left),mergeSort(right))
