def can_reach_end(arr):
    max_reach = 0
    for i, steps in enumerate(arr):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + steps)
    return max_reach >= len(arr) - 1

# Test cases
print(can_reach_end([1, 3, 1, 2, 0, 1]))  # Should return True
print(can_reach_end([1, 2, 1, 0, 0]))     # Should return False