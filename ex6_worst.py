import random
import time
import matplotlib.pyplot as plt

# Linear Search Algorithm
def linear_search(arr, target):
    """Performs linear search, checking each element one by one."""
    for i, value in enumerate(arr):
        if value == target:
            return i  # Found, return index
    return -1  # Not found

# Quicksort Algorithm
def quicksort(arr):
    """Sorts the array using Quicksort before performing binary search."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Binary Search Algorithm
def binary_search(arr, target):
    """Performs binary search on a sorted array."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Found, return index
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found

# Combined Quicksort + Binary Search
def quicksort_binary_search(arr, target):
    """Sorts the array with Quicksort, then searches using Binary Search."""
    sorted_arr = quicksort(arr)  # Sorting first
    return binary_search(sorted_arr, target)

# Worst-case scenario for Quicksort: reverse-sorted array
def worst_case_performance(arr_size, n_tasks=100):
    total_time = 0
    target = random.randint(0, arr_size)
    for _ in range(n_tasks):
        arr = list(range(arr_size, 0, -1))  # Reverse sorted array (worst case for quicksort)
        start_time = time.time()
        quicksort_binary_search(arr, target)
        total_time += (time.time() - start_time)
    return total_time / n_tasks

# Define array sizes to test
input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

# Measure worst-case performance of Quicksort + Binary Search
worst_case_times = []
for size in input_sizes:
    worst_case_times.append(worst_case_performance(size))

# Plotting the worst-case scenario performance
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, worst_case_times, label="Worst-case Quicksort + Binary Search", color='g', marker='^')
plt.xlabel("Array Size")
plt.ylabel("Average Time (seconds)")
plt.title("Worst-case Performance of Quicksort + Binary Search")
plt.legend()
plt.grid(True)
plt.show()
