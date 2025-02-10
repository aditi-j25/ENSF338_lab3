#EXERCISE 2 
import timeit
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit #use pip install scipy

# Bubble Sort Implementation
def bubble_sort(arr):
    """Simple O(n^2) sorting algorithm that swaps adjacent elements."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Optimization: Stops early if already sorted

# Quicksort Implementation
def quicksort(arr):
    """Divide-and-conquer sorting algorithm using a pivot element."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Generate test cases based on best, worst, and average scenarios
def generate_test_cases(size, case_type):
    """Generates test cases for sorting algorithms."""
    if case_type == "best":
        return list(range(size))  # Best case for Bubble Sort (already sorted)
    elif case_type == "worst":
        return list(range(size, 0, -1))  # Worst case for Bubble Sort (reverse sorted)
    else:
        return [random.randint(0, size) for _ in range(size)]  # Average case (random)

# Test function to measure execution time
def test_algorithm(algorithm, sizes, case_type):
    """Runs sorting algorithm on different input sizes and measures execution time."""
    times = []
    for size in sizes:
        arr = generate_test_cases(size, case_type)
        timer = timeit.timeit(lambda: algorithm(arr.copy()), number=3)  # Run each test 3 times for accuracy
        times.append(timer)
    return times

# Define 20 input sizes (gradually increasing)
input_sizes = [5, 10, 20, 30, 50, 75, 100, 150, 200, 300, 400, 500, 750, 1000, 
               1500, 2000, 3000, 5000, 7500, 10000]

# Measure execution time for each scenario
# Bubble Sort Performance
bubble_best = test_algorithm(bubble_sort, input_sizes, "best")   # Already sorted input (Best Case)
bubble_worst = test_algorithm(bubble_sort, input_sizes, "worst") # Reverse sorted input (Worst Case)
bubble_avg = test_algorithm(bubble_sort, input_sizes, "average") # Random order input (Average Case)

# Quicksort Performance
quick_best = test_algorithm(quicksort, input_sizes, "best")   # Best Case for Quicksort (Random Input)
quick_worst = test_algorithm(quicksort, input_sizes, "worst") # Worst Case for Quicksort (Sorted Input)
quick_avg = test_algorithm(quicksort, input_sizes, "average") # Average Case (Random Input)

# Define a function for smooth curve fitting
def fit_curve(x, a, b, c):
    return a * np.array(x) ** b + c

# Function to plot performance results
def plot_performance(title, bubble_data, quick_data):
    """Plots execution time comparison and highlights the threshold where Quicksort becomes faster."""
    plt.figure(figsize=(10, 5))

    # Scatter plot of actual times
    plt.scatter(input_sizes, bubble_data, label="Bubble Sort", color="red", marker="o")
    plt.scatter(input_sizes, quick_data, label="Quicksort", color="blue", marker="s")

    # Fit curves for better visualization
    popt_bubble, _ = curve_fit(fit_curve, input_sizes, bubble_data, maxfev=5000)
    popt_quick, _ = curve_fit(fit_curve, input_sizes, quick_data, maxfev=5000)
    smooth_x = np.linspace(min(input_sizes), max(input_sizes), 100)
    plt.plot(smooth_x, fit_curve(smooth_x, *popt_bubble), "r--", label="Bubble Sort Fit")
    plt.plot(smooth_x, fit_curve(smooth_x, *popt_quick), "b-", label="Quicksort Fit")

    # Find the threshold where QuickSort becomes faster
    threshold = None
    for i, size in enumerate(input_sizes):
        if quick_data[i] < bubble_data[i]:  
            threshold = size
            break

    # Highlight the threshold if found
    if threshold:
        plt.axvline(threshold, color="green", linestyle="--", label=f"Threshold ≈ {threshold}")

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# Generate performance plots for all cases
plot_performance("Best Case Performance (Sorted Input)", bubble_best, quick_best)
plot_performance("Worst Case Performance (Reverse Sorted Input for Bubble, Sorted for Quick)", bubble_worst, quick_worst)
plot_performance("Average Case Performance (Random Input)", bubble_avg, quick_avg)

# Determine and print threshold for "small" arrays
for i, size in enumerate(input_sizes):
    if quick_avg[i] < bubble_avg[i]:  # Find first input size where quicksort is faster
        print(f"Threshold for 'small' arrays: {size}")
        break


#4) Discussion 

# Linear search follows an O(n) trend, with parameters: {linear_params}
# Binary search follows an O(log n) trend, with parameters: {binary_params}
# The empirical results align with theoretical complexity expectations.
