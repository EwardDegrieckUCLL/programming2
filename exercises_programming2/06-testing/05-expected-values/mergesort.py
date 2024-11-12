def split_in_two(ns):
    middle_index = len(ns) // 2
    return (ns[:middle_index], ns[middle_index:])

def merge_sorted(left, right):
    result = []
    i=0
    j=0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
    
    if i < len(left) and j == len(right):
        result += left[i:]
    
    if i == len(left) and j < len(right):
        result += right[j:]

    return result

def merge_sort(ns):
    if len(ns) <= 1:
        return ns   
    
    left, right = split_in_two(ns)
    return merge_sorted(merge_sort(left), merge_sort(right))