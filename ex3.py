def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        for j in range(n - i - 1):
            # Each if-check is a comparison
            comparisons += 1
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                
    return comparisons, swaps


import numpy as np
import matplotlib.pyplot as plt


# 3
sizes = [10, 20, 30, 40, 50, 100, 150, 200]

comparison_counts = []
swap_counts = []

for size in sizes:
    arr = np.random.randint(0, 1000, size)
    
    comparisons, swaps = bubble_sort(arr.copy())
    
    comparison_counts.append(comparisons)
    swap_counts.append(swaps)

# 4
plt.figure(figsize=(12, 5))

# comparisons
plt.subplot(1, 2, 1)
plt.plot(sizes, comparison_counts, marker='o', label="Measured Comparisons")
# Theoretical ~ n(n-1)/2
theoretical_comparisons = [s*(s-1)/2 for s in sizes]
plt.plot(sizes, theoretical_comparisons, '--', label="Theoretical O(n²)")
plt.xlabel("Input Size (n)")
plt.ylabel("Number of Comparisons")
plt.title("Bubble Sort: Comparisons")
plt.legend()

#swaps
plt.subplot(1, 2, 2)
plt.plot(sizes, swap_counts, marker='s', label="Measured Swaps")
# Theoretical average ~ n(n-1)/4
theoretical_swaps = [s*(s-1)/4 for s in sizes]
plt.plot(sizes, theoretical_swaps, '--', label="Theoretical O(n²) Average")
plt.xlabel("Input Size (n)")
plt.ylabel("Number of Swaps")
plt.title("Bubble Sort: Swaps")
plt.legend()

plt.tight_layout()
plt.show()
