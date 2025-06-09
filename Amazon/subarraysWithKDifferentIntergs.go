package main

func subarraysWithKDistinct(nums []int, k int) int {
	// Helper function to count subarrays with at most k distinct integers
	atMostK := func(k int) int {
		count := 0
		left := 0
		freq := make(map[int]int)

		for right := 0; right < len(nums); right++ {
			freq[nums[right]]++

			// Shrink window if we have more than k distinct integers
			for len(freq) > k {
				freq[nums[left]]--
				if freq[nums[left]] == 0 {
					delete(freq, nums[left])
				}
				left++
			}

			// Add all valid subarrays ending at right
			count += right - left + 1
		}
		return count
	}

	// The answer is the difference between subarrays with at most k distinct integers
	// and subarrays with at most k-1 distinct integers
	return atMostK(k) - atMostK(k-1)
}

func main() {
	// Test cases
	nums1 := []int{1, 2, 1, 2, 3}
	k1 := 2
	println("Test case 1:", subarraysWithKDistinct(nums1, k1)) // Expected: 7

	nums2 := []int{1, 2, 1, 3, 4}
	k2 := 3
	println("Test case 2:", subarraysWithKDistinct(nums2, k2)) // Expected: 3
}
