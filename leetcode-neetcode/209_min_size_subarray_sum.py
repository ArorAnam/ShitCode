def minSubarrayLen(target: int, nums: list[int]) -> int:
    if not nums:
        return 0
    
    left = 0
    right = 0
    min_len = float('inf')
    current_sum = 0
    
    while right < len(nums):
        current_sum += nums[right]
        
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
        
        right += 1
    
    return min_len if min_len != float('inf') else 0

# Time complexity: O(n)
# Space complexity: O(1)