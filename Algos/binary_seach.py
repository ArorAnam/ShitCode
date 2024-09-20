import time
import random

def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def binary_search_recursive(arr, target):
    def helper(left, right):
        if left > right:
            return -1

        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return helper(mid + 1, right)
        else:
            return helper(left, mid - 1)

    return helper(0, len(arr) - 1)

# Example usage
# Generate a large sorted list of random integers
large_list = sorted(random.sample(range(1, 1000000), 100000))

# Choose a target that is guaranteed to be in the list
target = large_list[len(large_list) // 2]

# Measure time for iterative binary search
start_time = time.time()
iterative_result = binary_search_iterative(large_list, target)
iterative_time = time.time() - start_time

# Measure time for recursive binary search
start_time = time.time()
recursive_result = binary_search_recursive(large_list, target)
recursive_time = time.time() - start_time

print(f"Iterative result: {iterative_result}, Time taken: {iterative_time:.6f} seconds")
print(f"Recursive result: {recursive_result}, Time taken: {recursive_time:.6f} seconds")

