import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean canPartition(int[] nums, int target) {
        // Calculate total product of all numbers
        long totalProduct = 1;
        for (int num : nums) {
            totalProduct *= num;
        }
        
        // If total product is not divisible by target^2, it's impossible
        if (totalProduct % (target * target) != 0) {
            return false;
        }
        
        // Sort array in descending order to try larger numbers first
        // This helps in pruning branches earlier
        Arrays.sort(nums);
        reverse(nums);
        
        // Create memoization map
        Map<String, Boolean> memo = new HashMap<>();
        
        // Try to find two subsets with product equal to target
        return backtrack(nums, 0, 1, 1, target, memo);
    }
    
    private void reverse(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
    }
    
    private boolean backtrack(int[] nums, int index, long subset1Product, long subset2Product, int target, Map<String, Boolean> memo) {
        // If we've used all numbers, check if both subsets have product equal to target
        if (index == nums.length) {
            return subset1Product == target && subset2Product == target;
        }
        
        // Create a unique key for the current state
        String key = index + "," + subset1Product + "," + subset2Product;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        
        // If either subset's product is already greater than target, we can't proceed
        if (subset1Product > target || subset2Product > target) {
            memo.put(key, false);
            return false;
        }
        
        // Try adding current number to first subset
        if (subset1Product * nums[index] <= target) {
            if (backtrack(nums, index + 1, subset1Product * nums[index], subset2Product, target, memo)) {
                memo.put(key, true);
                return true;
            }
        }
        
        // Try adding current number to second subset
        if (subset2Product * nums[index] <= target) {
            if (backtrack(nums, index + 1, subset1Product, subset2Product * nums[index], target, memo)) {
                memo.put(key, true);
                return true;
            }
        }
        
        memo.put(key, false);
        return false;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test Case 1: Original test case
        int[] nums1 = {14, 1, 8, 23, 12, 19, 24, 15, 7};
        int target1 = 1;
        System.out.println("Test Case 1:");
        System.out.println("Input: nums = " + Arrays.toString(nums1) + ", target = " + target1);
        System.out.println("Output: " + solution.canPartition(nums1, target1));
        System.out.println("Expected: false");
        System.out.println();

        // Test Case 2: Simple case with possible partition
        int[] nums2 = {2, 3, 6};
        int target2 = 6;
        System.out.println("Test Case 2:");
        System.out.println("Input: nums = " + Arrays.toString(nums2) + ", target = " + target2);
        System.out.println("Output: " + solution.canPartition(nums2, target2));
        System.out.println("Expected: true");
        System.out.println();

        // Test Case 3: Case with all same numbers
        int[] nums3 = {2, 2, 2, 2};
        int target3 = 4;
        System.out.println("Test Case 3:");
        System.out.println("Input: nums = " + Arrays.toString(nums3) + ", target = " + target3);
        System.out.println("Output: " + solution.canPartition(nums3, target3));
        System.out.println("Expected: true");
        System.out.println();

        // Test Case 4: Case with target = 1 and all numbers > 1
        int[] nums4 = {2, 3, 4, 5};
        int target4 = 1;
        System.out.println("Test Case 4:");
        System.out.println("Input: nums = " + Arrays.toString(nums4) + ", target = " + target4);
        System.out.println("Output: " + solution.canPartition(nums4, target4));
        System.out.println("Expected: false");
        System.out.println();

        // Test Case 5: Valid case with distinct numbers and possible partition
        int[] nums5 = {2, 3, 4, 6};
        int target5 = 12;
        System.out.println("Test Case 5:");
        System.out.println("Input: nums = " + Arrays.toString(nums5) + ", target = " + target5);
        System.out.println("Output: " + solution.canPartition(nums5, target5));
        System.out.println("Expected: true");
        System.out.println();
    }
}
