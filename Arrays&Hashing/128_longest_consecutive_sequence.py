def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)
    nums = set(nums)
    max_len = 0
    while nums:
        first = last = nums.pop()
        while first - 1 in nums:
            first -= 1
            nums.remove(first)
        while last + 1 in nums:
            last += 1
            nums.remove(last)
        max_len = max(max_len, last - first + 1)
    return max_len

# Time: O(n)
# Space: O(n)
from typing import List
# Solution 2
def longestConsecutive_2(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak