# ENSF 338 Lab 3: Exercise 4
import time
import numpy as np
import matplotlib.pyplot as plt

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

sizes = list(range(1, 17))
times = []

for size in sizes:
    arr = list(range(size, 0, -1))
    start = time.time()
    quickSort(arr, 0, len(arr) - 1)
    end = time.time()
    times.append(end - start)
    print(f"Sorted array of size {size}: {arr}")

plt.plot(sizes, times, 'ro-', label='Measured Execution Time')
plt.plot(sizes, np.array(sizes)**2 / max(sizes)**2 * max(times), 'b-', label='O(n^2) Fit')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (s)')
plt.title('Quicksort Worst-Case Complexity')
plt.legend()
plt.grid()
plt.savefig('ex4.3.png')
plt.show()



