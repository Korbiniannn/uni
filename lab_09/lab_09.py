def is_sorted(L1):
    """
    >>> is_sorted([3, 2, 4, 1])
    False
    >>> is_sorted([1, 3, 5, 7])
    True
    """
    
    for idx in range(0, len(L1) - 2):
        for idx2 in range(1, len(L1) - 1):
            if L1[idx] <= L1[idx2]:
                pass 
            else:
                return False
    return True

def bubb_sort(L1):
    """
    >>> bubb_sort([3, 2, 4, 1])
    [1, 2, 3, 4]
    >>> bubb_sort([1, 3, 5, 7])
    [1, 3, 5, 7]
    """
    for idx in range(0, len(L1)):
        for idx2 in range(idx + 1, len(L1)):
            if L1[idx] > L1[idx2]:
                L1[idx], L1[idx2] = L1[idx2], L1[idx]

    return L1

def select_sort(L1):
    """
    >>> select_sort([2, 1, 3, 4, 1, 6, 2, 1, 4, 8])
    [1, 1, 1, 2, 2, 3, 4, 4, 6, 8]
    >>> select_sort([3, 2, 4, 1])
    [1, 2, 3, 4]
    >>> select_sort([1, 3, 5, 7])
    [1, 3, 5, 7]
    """
    i = 0
    for idx_elem in range(len(L1)):
        min_elem = idx_elem
        for pos in range(i, len(L1)):
            if L1[min_elem] > L1[pos]:
                min_elem = pos
        i += 1
        L1[idx_elem], L1[min_elem] = L1[min_elem], L1[idx_elem]

    return L1

def insert_sort(L1):
    """
    >>> insert_sort([2, 1, 3, 4, 1, 6, 2, 1, 4, 8])
    [1, 1, 1, 2, 2, 3, 4, 4, 6, 8]
    >>> insert_sort([3, 2, 4, 1])
    [1, 2, 3, 4]
    >>> insert_sort([1, 3, 5, 7])
    [1, 3, 5, 7]
    """
    i = 0
    while i < len(L1):
        key = i
        while key > 0:
            if L1[key - 1] > L1[key]:
                L1[key -1], L1[key] = L1[key], L1[key -1]
            key -= 1
        i += 1
    return L1

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
    
def merge(left, right):
    result = []
    i, j = 0, 0 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result