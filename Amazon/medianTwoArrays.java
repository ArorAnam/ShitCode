public class medianTwoArrays {
    // Brute Force Solution
    // Time Complexity: O((m+n)log(m+n)) due to sorting
    // Space Complexity: O(m+n) for storing merged array
    public static double findMedianSortedArraysBruteForce(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int[] merged = new int[m + n];
        
        // Copy elements from both arrays
        System.arraycopy(nums1, 0, merged, 0, m);
        System.arraycopy(nums2, 0, merged, m, n);
        
        // Sort the merged array
        Arrays.sort(merged);
        
        // Find median
        int totalLength = m + n;
        if (totalLength % 2 == 0) {
            // If even length, return average of two middle elements
            return (merged[totalLength/2 - 1] + merged[totalLength/2]) / 2.0;
        } else {
            // If odd length, return middle element
            return merged[totalLength/2];
        }
    }
    
    // Optimized Solution using Binary Search
    // Time Complexity: O(log(min(m,n)))
    // Space Complexity: O(1)
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // Ensure nums1 is the smaller array
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int m = nums1.length;
        int n = nums2.length;
        int left = 0;
        int right = m;
        
        while (left <= right) {
            int partitionX = (left + right) / 2;
            int partitionY = (m + n + 1) / 2 - partitionX;
            
            // Find elements around partition
            int maxLeftX = (partitionX == 0) ? Integer.MIN_VALUE : nums1[partitionX - 1];
            int minRightX = (partitionX == m) ? Integer.MAX_VALUE : nums1[partitionX];
            
            int maxLeftY = (partitionY == 0) ? Integer.MIN_VALUE : nums2[partitionY - 1];
            int minRightY = (partitionY == n) ? Integer.MAX_VALUE : nums2[partitionY];
            
            // Check if we found the correct partition
            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                // Found the correct partition
                if ((m + n) % 2 == 0) {
                    // Even length
                    return (Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2.0;
                } else {
                    // Odd length
                    return Math.max(maxLeftX, maxLeftY);
                }
            } else if (maxLeftX > minRightY) {
                // Move partition left
                right = partitionX - 1;
            } else {
                // Move partition right
                left = partitionX + 1;
            }
        }
        
        throw new IllegalArgumentException("Input arrays are not sorted");
    }
    
    // Main method for testing
    public static void main(String[] args) {
        // Test cases
        int[] nums1 = {1, 3};
        int[] nums2 = {2};
        System.out.println("Brute Force Solution: " + findMedianSortedArraysBruteForce(nums1, nums2));
        System.out.println("Optimized Solution: " + findMedianSortedArrays(nums1, nums2));
        
        int[] nums3 = {1, 2};
        int[] nums4 = {3, 4};
        System.out.println("\nBrute Force Solution: " + findMedianSortedArraysBruteForce(nums3, nums4));
        System.out.println("Optimized Solution: " + findMedianSortedArrays(nums3, nums4));
    }
}
