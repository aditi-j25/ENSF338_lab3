import time
import numpy as np
import json
import matplotlib.pyplot as plt

# 1. Implement a standard binary search with a configurable midpoint
def binary_search_with_custom_midpoint(arr, target, custom_midpoint=None):
    """Performs binary search with a configurable midpoint for the first iteration."""
    left, right = 0, len(arr) - 1

    # If a custom midpoint is provided, use it for the first iteration
    if custom_midpoint is not None:
        mid = custom_midpoint
    else:
        mid = (left + right) // 2

    while left <= right:
        mid = (left + right) // 2 if custom_midpoint is None else mid

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found

# 2. Time the performance of each search task with different midpoints
# Function to measure the time taken for a search task with a custom midpoint
def time_search(arr, target, custom_midpoint=None):
    start_time = time.time()
    binary_search_with_custom_midpoint(arr, target, custom_midpoint)
    return time.time() - start_time  # Return the time taken for the search

# Load the data (you'll need to adjust the file paths)
with open('ex7data.json') as f:
    arr = json.load(f)  # Assuming it's a sorted array

with open('ex7tasks.json') as f:
    tasks = json.load(f)  # List of search tasks (targets to find in arr)

# Generate possible midpoints for the first search
midpoints_to_test = [len(arr)//4, len(arr)//2, 3*len(arr)//4]

# Dictionary to store the best midpoint for each task
best_midpoints = {}

# Dictionary to store the time for each task with different midpoints
midpoint_times = {}

# Measure the performance for each task
for task in tasks:
    best_time = float('inf')
    best_midpoint = None

    for midpoint in midpoints_to_test:
        time_taken = time_search(arr, task, custom_midpoint=midpoint)

        # Track the best midpoint
        if time_taken < best_time:
            best_time = time_taken
            best_midpoint = midpoint

    best_midpoints[task] = best_midpoint
    midpoint_times[task] = best_time

# 3. Print best midpoints for each task
print("Best Midpoints for each task:", best_midpoints)

# 4. Scatter plot of tasks vs. chosen midpoints
tasks_list = list(best_midpoints.keys())
midpoints_list = list(best_midpoints.values())

plt.figure(figsize=(10, 6))
plt.scatter(tasks_list, midpoints_list, color='b', label='Chosen Midpoints')
plt.xlabel("Task (Target)")
plt.ylabel("Chosen Midpoint")
plt.title("Best Midpoint for Each Search Task")
plt.grid(True)
plt.show()

# Description od the graph:
# - From the scatterplot, we can observe how the choice of initial midpoint affects the search task.
# - If the data is evenly distributed, choosing the exact midpoint (i.e., len(arr) // 2) typically yields the fastest search time.
# - If the data is skewed or has certain patterns, a midpoint closer to the 1/4th or 3/4th of the array might work better, depending on the task.
# - The graph helps identify any tasks where unusual midpoints are optimal, which may suggest the data has specific characteristics.
