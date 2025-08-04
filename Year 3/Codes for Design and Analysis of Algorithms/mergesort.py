import matplotlib.pyplot as plt
import time
data = [12, 3, 45, 28, 81, 34, 72, 90, 28, 7, 11, 63]
# Merge Sort
def merge_sort(arr, depth=0):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    print(" " * depth + f"MergeSort Divide: {arr[:mid]} | {arr[mid:]}")
    left = merge_sort(arr[:mid], depth + 2)
    right = merge_sort(arr[mid:], depth + 2)
    merged = merge(left, right)
    print(" " * depth + f"MergeSort Conquer: {left} + {right} => Combine: {merged}")
    return merged

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Timing Merge Sort
merge_data = data.copy()
start_merge = time.time()
sorted_merge = merge_sort(merge_data)
merge_duration = time.time() - start_merge
