package main

// lengthOfLongestSubstringASCII is optimized for ASCII characters using a fixed-size array
func lengthOfLongestSubstringASCII(s string) int {
	// For ASCII characters, we can use a fixed-size array
	// Initialize with -1 to indicate character hasn't been seen
	lastSeen := [128]int{}
	for i := range lastSeen {
		lastSeen[i] = -1
	}

	maxLength := 0
	start := 0

	for end := 0; end < len(s); end++ {
		// Get the ASCII value of the current character
		char := s[end]

		// If we've seen this character before and it's within our current window
		if lastSeen[char] >= start {
			start = lastSeen[char] + 1
		}

		// Update the last seen position
		lastSeen[char] = end

		// Update maxLength if current window is larger
		if end-start+1 > maxLength {
			maxLength = end - start + 1
		}
	}

	return maxLength
}

// lengthOfLongestSubstringUnicode handles all Unicode characters using a map
func lengthOfLongestSubstringUnicode(s string) int {
	// Create a map to store the last position of each character
	charPos := make(map[rune]int)

	// Initialize variables
	maxLength := 0
	start := 0

	// Iterate through the string
	for end, char := range s {
		// If we find a repeating character, update the start position
		if pos, exists := charPos[char]; exists && pos >= start {
			start = pos + 1
		}

		// Update the character's position
		charPos[char] = end

		// Update maxLength if current window is larger
		currentLength := end - start + 1
		if currentLength > maxLength {
			maxLength = currentLength
		}
	}

	return maxLength
}

// Example usage
func main() {
	testCases := []string{
		"abcabcbb", // Expected: 3 ("abc")
		"bbbbb",    // Expected: 1 ("b")
		"pwwkew",   // Expected: 3 ("wke")
		"你好世界",     // Expected: 4 (Unicode test)
	}

	println("Testing ASCII-optimized version:")
	for _, s := range testCases {
		result := lengthOfLongestSubstringASCII(s)
		println("Input:", s, "Output:", result)
	}

	println("\nTesting Unicode version:")
	for _, s := range testCases {
		result := lengthOfLongestSubstringUnicode(s)
		println("Input:", s, "Output:", result)
	}
}
