# ENSF 338 Lab 3: Exercise 5
import time
import numpy as np
import matplotlib.pyplot as plt

# 1. Traditional Insertion Sort and Binary Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def binary_search(arr, val, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
    return start

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        # Find the position where key should be inserted
        pos = binary_search(arr, key, 0, i - 1)
        # Move elements to make space for the key
        arr = arr[:pos] + [key] + arr[pos:i] + arr[i+1:]
    return arr

# 2. Testing each algorithm on a number of average-case inputs of increasing length
def generate_random_array(size):
    return np.random.randint(0, 10000, size).tolist()

sizes = list(range(1, 101, 5))
insertion_times = []
binary_insertion_times = []

for size in sizes:
    arr = generate_random_array(size)

    start = time.time()
    insertion_sort(arr.copy())
    end = time.time()
    insertion_times.append(end - start)
    
    start = time.time()
    binary_insertion_sort(arr.copy())
    end = time.time()
    binary_insertion_times.append(end - start)

print("Sizes:", sizes)
print("Insertion Sort Times:", insertion_times)
print("Binary Insertion Sort Times:", binary_insertion_times)

# 3. Plotted results
plt.plot(sizes, insertion_times, 'ro-', label='Insertion Sort')
plt.plot(sizes, binary_insertion_times, 'bo-', label='Binary Insertion Sort')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (s)')
plt.title('Comparison of Insertion Sort and Binary Insertion Sort')
plt.legend()
plt.grid()
plt.savefig('ex5.3.png')
plt.show()

'''
4. The following plot shows that the binary insertion sort (indicated by the blue line) is slightly faster compared to the insertion sort (indicated by the red line) as the input increases. This happens because the binary search reduces the number of comparisons from O(n) to O(log n) as it finds the insertion points. Nonetheless, both algorithms still need shifting elements to keep their overall time complexity at O(n^2). This is why the performance difference is observable-- however, not drastic. The mergesort or quicksort methods (having O(log n)) would be much more efficient when it comes to the case of larger inputs. 
'''
