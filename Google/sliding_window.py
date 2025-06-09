def length_of_longest_substring(s: str) -> int:
    # Hash map to store the last occurrence of each character
    char_index = {}
    max_length = 0
    start = 0  # Left pointer of the sliding window

    for end in range(len(s)):
        
        if s[end] in char_index:
            # Move the start pointer to the right of the last occurrence
            start = max(start, char_index[s[end]] + 1)

        # Update the last occurrence of the current character
        char_index[s[end]] = end

        # Calculate the maximum length of the substring
        max_length = max(max_length, end - start + 1)

    return max_length


# Test cases
print(length_of_longest_substring("abcabcbb"))  # Output: 3 (substring: "abc")
print(length_of_longest_substring("bbbbb"))     # Output: 1 (substring: "b")
print(length_of_longest_substring("pwwkew"))    # Output: 3 (substring: "wke")
print(length_of_longest_substring(""))          # Output: 0 (empty string)
print(length_of_longest_substring("abcdef"))    # Output: 6 (substring: "abcdef")
print(length_of_longest_substring("aab"))       # Output: 2 (substring: "ab")
