# sliding_window.py

# Fixed-size sliding window
def fixed_size_sliding_window(arr, k):
    n = len(arr)
    if n * k == 0:
        return []
    if k > n:
        return []

    result = []
    window_sum = sum(arr[:k])
    result.append(window_sum)

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        result.append(window_sum)

    return result

# Variable-size sliding window (Longest Substring Without Repeating Characters)
def longest_substring_without_repeating(s):
    n = len(s)
    if n == 0:
        return 0

    char_index_map = {}
    left = 0
    max_length = 0

    for right in range(n):
        if s[right] in char_index_map:
            left = max(left, char_index_map[s[right]] + 1)
        char_index_map[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

# Maximum sum subarray of size k
def max_sum_subarray(arr, k):
    n = len(arr)
    if n * k == 0:
        return 0
    if k > n:
        return 0

    max_sum = float('-inf')
    window_sum = sum(arr[:k])

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Minimum window substring
def min_window_substring(s, t):
    if not s or not t:
        return ""

    dict_t = {}
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1

    required = len(dict_t)
    l, r = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None

    while r < len(s):
        char = s[r]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1

        while l <= r and formed == required:
            char = s[l]

            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1

            l += 1

        r += 1

    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

# Example usage
if __name__ == "__main__":
    print(fixed_size_sliding_window([1, 2, 3, 4, 5, 6], 3))
    print(longest_substring_without_repeating("abcabcbb"))
    print(max_sum_subarray([1, 2, 3, 4, 5, 6], 3))
    print(min_window_substring("ADOBECODEBANC", "ABC"))