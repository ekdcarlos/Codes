import matplotlib.pyplot as plt
import time 
data = [12, 3, 45, 28, 81, 34, 72, 90, 28, 7, 11, 63]
# Quick Sort
def quick_sort(arr, depth=0):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    print(" " * depth + f"QuickSort Divide: pivot={pivot}, left={left}, right={right}")
    sorted_left = quick_sort(left, depth + 2)
    sorted_right = quick_sort(right, depth + 2)
    combined = sorted_left + [pivot] + sorted_right
    print(" " * depth + f"QuickSort Conquer & Combine: {sorted_left} + [{pivot}] + {sorted_right} => {combined}")
    return combined

merge_data = data.copy()
start_merge = time.time()
sorted_merge = quick_sort(merge_data)
merge_duration = time.time() - start_merge