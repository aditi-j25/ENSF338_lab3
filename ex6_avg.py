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

# Function to measure performance of a task (searching for a constant element)
def measure_performance(search_algorithm, arr_size, n_tasks=100):
    total_time = 0
    target = random.randint(0, arr_size)  # Random target in the range of the array size
    for _ in range(n_tasks):
        arr = [random.randint(0, arr_size) for _ in range(arr_size)]  # Generate a random array
        start_time = time.time()
        search_algorithm(arr, target)
        total_time += (time.time() - start_time)
    return total_time / n_tasks  # Average time per task

# Define array sizes to test
input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

# Measure performance for Linear Search and Quicksort + Binary Search
linear_search_times = []
quicksort_binary_search_times = []

for size in input_sizes:
    linear_search_times.append(measure_performance(linear_search, size))
    quicksort_binary_search_times.append(measure_performance(quicksort_binary_search, size))

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, linear_search_times, label="Linear Search", color='r', marker='o')
plt.plot(input_sizes, quicksort_binary_search_times, label="Quicksort + Binary Search", color='b', marker='s')
plt.xlabel("Array Size")
plt.ylabel("Average Time (seconds)")
plt.title("Performance of Linear Search vs. Quicksort + Binary Search")
plt.legend()
plt.grid(True)
plt.show()

# Discussion for Question 4:
# - As we can observe from the plot, for smaller input sizes (e.g., size <= 50), Linear Search is faster because 
#   the overhead of sorting in Quicksort + Binary Search becomes significant.
# - As the input size increases (e.g., size > 100), the performance of Quicksort + Binary Search improves, 
#   and it becomes more efficient due to its O(n log n) sorting complexity and O(log n) searching time.
# - Linear Search has a time complexity of O(n), meaning the time it takes to search grows linearly with the array size.
# - Therefore, Linear Search is more efficient for small inputs (typically under 100), while Quicksort + Binary Search
#   is better suited for larger inputs due to its logarithmic search time after sorting.
